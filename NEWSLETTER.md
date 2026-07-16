# Newsletter signups

The **Subscribe** form (`_includes/subscribe-form.html`) collects email
addresses for the blog's new-post newsletter.

## Where signups go today

Submitted emails are stored in a **Google Sheet**, written by a **Google Apps
Script Web App**. The Web App URL lives in `_config.yml`:

```yaml
newsletter_endpoint: "https://script.google.com/macros/s/.../exec"
```

On submit, the form does a `fetch` POST (form-urlencoded, `mode: 'no-cors'`) of
the `email` field to that endpoint. The Apps Script `doPost(e)` reads
`e.parameter.email` and appends `[timestamp, email]` as a new row.

Because Apps Script Web Apps don't return usable CORS headers, the browser sees
an *opaque* response — we can't read status or body. The accepted pattern is to
treat a resolved `fetch` promise as success (and a rejected promise, e.g. a
network failure, as an error).

## How to check the signups

1. Open the Google Sheet backing the Apps Script (from the same Google account
   that owns the script → **Extensions ▸ Apps Script** shows the bound project).
2. Each row is `[timestamp, email]`; the newest signups are at the bottom.
3. To export, use **File ▸ Download** (CSV) or import into your email tool.

If the endpoint ever changes (re-deploying the script mints a new `/exec` URL),
update `newsletter_endpoint` in `_config.yml`.

## Disabling the form

Set `newsletter_endpoint: ""` in `_config.yml`. The include then hides the form
and shows a "coming soon" message instead of breaking.

## Swapping to a real email service provider

To move off the Google Sheet onto a hosted provider (Buttondown, Mailchimp,
ConvertKit, etc.):

1. Create a form/audience with the provider and copy their embed snippet or form
   `action` endpoint.
2. Either:
   - **Simplest:** replace `newsletter_endpoint` in `_config.yml` with the
     provider's POST endpoint (if it accepts a form-urlencoded `email` field,
     the existing JS handler may work as-is), **or**
   - Replace the `<form>` / `<script>` in `_includes/subscribe-form.html` with
     the provider's official embed snippet.
3. Rebuild and test a signup end-to-end.

An RSS feed is also available at `/feed.xml` (via `jekyll-feed`) for readers and
RSS-to-email tools.
