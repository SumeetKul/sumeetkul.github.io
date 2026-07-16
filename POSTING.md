# How to publish a blog post

Writing a new post takes three steps: **write markdown**, **drop in images**,
**push**. Everything else — the date, the Jekyll front matter, moving images
into place, fixing image links — happens automatically.

## 1. Create a folder for your post

Inside `_drafts_raw/`, make a new folder named after your post (any short,
descriptive name works — it does not have to match the title exactly):

```
_drafts_raw/
  chasing-the-eclipse/
    post.md
    totality.jpg
    diamond-ring.jpg
```

Put your writing in a file called **`post.md`** and put every image the post
uses in the **same folder**.

## 2. Write `post.md`

Write plain markdown. Reference images by their **plain filename** — no paths,
no `assets/...`, just the name of the file sitting next to `post.md`:

```markdown
title: Chasing the Great Eclipse
tags: astrophotography, science-writing

# Chasing the Great Eclipse

I drove nine hours into the path of totality, and it was worth every mile.
The temperature dropped, the birds went quiet, and then the Sun disappeared.

![The moment of totality](totality.jpg)

As the Moon slid away, the "diamond ring" flared on the Sun's edge:

![The diamond ring effect](diamond-ring.jpg)
```

Notes:

- **Title** — the first `# Heading` is used as the title. You can instead put a
  `title:` line at the very top (as above); if both are present, the `title:`
  line wins. The heading is *not* repeated in the post body (the page shows the
  title automatically).
- **Tags** *(optional)* — add a `tags:` line near the top with comma-separated
  tags, e.g. `tags: astrophotography, moon`. They are lowercased and
  de-duplicated, and folded onto the site's existing tags where they match.
  If you omit the line, the post is created with `tags: []` and a
  `# TODO: add tags` note so you can fill them in later. **Tags are never
  guessed for you.**
- **Description/excerpt** — generated automatically from your first paragraph.
- **Date** — set automatically to the day the post is published.

The site's existing tag vocabulary is: `astrophotography`, `science-writing`,
`science-communication`, `research`, `gravitational-waves`, `multimedia`.
Reuse these where they fit so tags stay tidy (you can always add new ones).

## 3. Push

Commit the new folder and push to `master`:

```bash
git add _drafts_raw/chasing-the-eclipse
git commit -m "Draft: Chasing the Great Eclipse"
git push
```

The **Publish raw drafts** GitHub Action then:

1. runs `scripts/publish_draft.py`,
2. creates `_posts/YYYY-MM-DD-chasing-the-great-eclipse.md` with full front
   matter,
3. copies your images to `assets/images/blog/chasing-the-great-eclipse/` and
   rewrites the links in the post,
4. deletes `_drafts_raw/chasing-the-eclipse/`, and
5. commits all of that back to `master`.

A minute or two later the post is live on the blog. Run `git pull` afterwards to
get the generated post onto your machine.

## Doing it locally (optional)

You can run the same conversion yourself instead of waiting for the Action:

```bash
python scripts/publish_draft.py                       # all drafts
python scripts/publish_draft.py _drafts_raw/my-post   # one draft
```

Then commit the generated `_posts/` file and `assets/images/blog/` images.
