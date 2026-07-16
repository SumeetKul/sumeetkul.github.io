#!/usr/bin/env python3
"""Turn a raw markdown draft into a fully-formed Jekyll post.

The owner writes a plain markdown file (plus any images) inside a per-post
folder under ``_drafts_raw/<name>/`` and pushes. This script does the rest:

* reads the title (from a ``title:`` line or the first ``# H1``),
* stamps today's date and builds a slug,
* copies the draft's images into ``assets/images/blog/<slug>/`` and rewrites
  the relative image paths in the body to point there,
* writes ``_posts/YYYY-MM-DD-<slug>.md`` with full Jekyll front matter
  (layout, title, date, tags, categories, excerpt/description), and
* deletes the processed raw draft folder.

Usage:
    python scripts/publish_draft.py                 # process every draft folder
    python scripts/publish_draft.py _drafts_raw/my-post   # process one folder

Tags: if the raw markdown contains a ``tags: a, b`` line near the top they are
used (lowercased and de-duplicated). Otherwise the post is written with an
empty tag list and a TODO comment -- tags are never guessed automatically.
"""

from __future__ import annotations

import datetime as _dt
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DRAFTS_DIR = REPO_ROOT / "_drafts_raw"
POSTS_DIR = REPO_ROOT / "_posts"
BLOG_IMG_DIR = REPO_ROOT / "assets" / "images" / "blog"

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".tif", ".tiff"}

# Canonical tag vocabulary (see AUDIT.md). Draft tags are matched against this
# case-insensitively so that, e.g., "Astrophotography" folds into the existing
# "astrophotography" tag rather than creating a near-duplicate.
KNOWN_TAGS = [
    "astrophotography",
    "science-writing",
    "science-communication",
    "research",
    "gravitational-waves",
    "multimedia",
]

# Markdown image: ![alt](path "optional title")
IMG_MD_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<path>[^)\s]+)(?P<rest>\s+[^)]*)?\)")
# HTML <img src="path">
IMG_HTML_RE = re.compile(r"""(<img\b[^>]*?\bsrc\s*=\s*)(['"])(?P<path>[^'"]+)\2""", re.IGNORECASE)

META_LINE_RE = re.compile(r"^(title|tags|date|description|excerpt|categories)\s*:\s*(.*)$", re.IGNORECASE)
H1_RE = re.compile(r"^#\s+(.+?)\s*#*\s*$")


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "post"


def normalize_tags(raw: str) -> list[str]:
    seen: list[str] = []
    for part in re.split(r"[,\n]", raw):
        tag = slugify(part)
        if not tag:
            continue
        # Fold onto a known tag if one matches case-insensitively.
        for known in KNOWN_TAGS:
            if tag == known:
                tag = known
                break
        if tag not in seen:
            seen.append(tag)
    return seen


def find_markdown(folder: Path) -> Path | None:
    preferred = folder / "post.md"
    if preferred.is_file():
        return preferred
    candidates = sorted(p for p in folder.glob("*.md") if p.is_file())
    return candidates[0] if candidates else None


def is_local_path(path: str) -> bool:
    """True for a relative image reference that lives alongside the draft."""
    path = path.strip()
    if not path:
        return False
    if path.startswith(("http://", "https://", "//", "/", "data:", "mailto:")):
        return False
    if "{" in path or "}" in path:  # Liquid tag, leave alone
        return False
    return True


def parse_draft(md_path: Path) -> tuple[str, list[str] | None, str]:
    """Return (title, tags_or_None, body_without_meta_lines)."""
    lines = md_path.read_text(encoding="utf-8-sig").splitlines()

    title: str | None = None
    tags: list[str] | None = None
    body_lines: list[str] = []
    meta_zone = True  # only strip meta lines before the first real content

    for line in lines:
        stripped = line.strip()
        if meta_zone:
            if not stripped:
                # keep blank lines out of the leading meta block
                continue
            m = META_LINE_RE.match(stripped)
            if m:
                key, val = m.group(1).lower(), m.group(2).strip()
                if key == "title" and title is None:
                    title = val.strip("'\" ")
                elif key == "tags":
                    tags = normalize_tags(val)
                # date/description/etc. meta lines are dropped; they are
                # regenerated below.
                continue
            h1 = H1_RE.match(stripped)
            if h1:
                if title is None:
                    title = h1.group(1).strip()
                meta_zone = False
                # Do not emit the H1 into the body: the layout renders the
                # title from front matter as the page <h1>.
                continue
            # First real content line ends the meta zone.
            meta_zone = False
            body_lines.append(line)
        else:
            body_lines.append(line)

    if title is None:
        title = md_path.parent.name.replace("-", " ").replace("_", " ").strip().title()

    body = "\n".join(body_lines).strip() + "\n"
    return title, tags, body


def first_paragraph(body: str) -> str:
    for block in re.split(r"\n\s*\n", body):
        text = block.strip()
        if not text or text.startswith(("#", "!", "<", "|", ">", "-", "*", "```")):
            continue
        text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)      # strip images
        text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)   # keep link text
        text = re.sub(r"<[^>]+>", "", text)                    # strip inline html
        text = re.sub(r"[*_`#]", "", text)                     # strip md emphasis
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            return text
    return ""


def yaml_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def rewrite_images(body: str, slug: str, folder: Path, dest_dir: Path) -> tuple[str, list[Path]]:
    """Copy locally-referenced images and rewrite their paths. Returns (body, copied)."""
    copied: list[Path] = []
    web_prefix = f"/assets/images/blog/{slug}"

    def copy_one(rel_path: str) -> str | None:
        rel = rel_path.strip().split("#", 1)[0].split("?", 1)[0]
        src = (folder / rel).resolve()
        try:
            src.relative_to(folder.resolve())
        except ValueError:
            return None  # escapes the draft folder; leave untouched
        if not src.is_file() or src.suffix.lower() not in IMAGE_EXTS:
            return None
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / src.name
        shutil.copy2(src, dest)
        copied.append(dest)
        return f"{web_prefix}/{src.name}"

    def md_sub(m: re.Match) -> str:
        path = m.group("path")
        if not is_local_path(path):
            return m.group(0)
        new = copy_one(path)
        if new is None:
            return m.group(0)
        rest = m.group("rest") or ""
        return f"![{m.group('alt')}]({new}{rest})"

    def html_sub(m: re.Match) -> str:
        path = m.group("path")
        if not is_local_path(path):
            return m.group(0)
        new = copy_one(path)
        if new is None:
            return m.group(0)
        return f"{m.group(1)}{m.group(2)}{new}{m.group(2)}"

    body = IMG_MD_RE.sub(md_sub, body)
    body = IMG_HTML_RE.sub(html_sub, body)
    return body, copied


def publish(folder: Path) -> Path | None:
    md_path = find_markdown(folder)
    if md_path is None:
        print(f"  skip {folder.name}: no markdown file found")
        return None

    title, tags, body = parse_draft(md_path)
    slug = slugify(title)
    today = _dt.date.today().isoformat()
    dest_img_dir = BLOG_IMG_DIR / slug

    body, copied = rewrite_images(body, slug, folder, dest_img_dir)
    description = first_paragraph(body)

    if tags:
        tags_line = "tags: [" + ", ".join(tags) + "]"
    else:
        tags_line = "tags: []  # TODO: add tags"

    front_matter = [
        "---",
        "layout: post",
        f'title: "{yaml_escape(title)}"',
        f"date: {today}",
        tags_line,
        "categories: blog",
    ]
    if description:
        front_matter.append(f'description: "{yaml_escape(description)}"')
        front_matter.append(f'excerpt: "{yaml_escape(description)}"')
    front_matter.append("---")

    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    post_path = POSTS_DIR / f"{today}-{slug}.md"
    post_path.write_text("\n".join(front_matter) + "\n\n" + body, encoding="utf-8")

    shutil.rmtree(folder)

    print(f"  published {folder.name} -> {post_path.relative_to(REPO_ROOT)}"
          f" ({len(copied)} image(s) copied)")
    return post_path


def draft_folders() -> list[Path]:
    if not DRAFTS_DIR.is_dir():
        return []
    return sorted(
        p for p in DRAFTS_DIR.iterdir()
        if p.is_dir() and not p.name.startswith(".") and find_markdown(p) is not None
    )


def main(argv: list[str]) -> int:
    targets = [Path(a).resolve() for a in argv[1:]] if len(argv) > 1 else draft_folders()
    if not targets:
        print("No raw drafts to publish.")
        return 0
    published = 0
    for folder in targets:
        if not folder.is_dir():
            print(f"  skip {folder}: not a directory")
            continue
        if publish(folder) is not None:
            published += 1
    print(f"Done. {published} draft(s) published.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
