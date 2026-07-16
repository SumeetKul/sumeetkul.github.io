# `_drafts_raw/` — drop raw drafts here

This folder is **excluded from the Jekyll build** (see `exclude:` in `_config.yml`),
so nothing here is published directly.

To publish a post, create a sub-folder named after your post and drop a markdown
file (`post.md`) plus any images it uses inside it:

```
_drafts_raw/
  my-post-title/
    post.md
    photo1.jpg
    photo2.png
```

Reference images with simple relative filenames in `post.md`, e.g.
`![a description](photo1.jpg)`. When you push, the
`Publish raw drafts` GitHub Action runs `scripts/publish_draft.py`, which turns
your draft into a dated post under `_posts/`, copies the images into
`assets/images/blog/<slug>/`, rewrites the image paths, and deletes the draft
folder.

See **[POSTING.md](../POSTING.md)** at the repo root for the full guide and an
example. This README is ignored by the publish script (only sub-folders that
contain a markdown file are processed).
