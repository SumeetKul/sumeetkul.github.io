# Newsletter signups

The **Subscribe** form (`_includes/subscribe-form.html`) collects email
addresses for the blog's new-post newsletter.

## Where signups go today

On submit, the form **dual-writes** each email, in parallel, to two places:

1. **Google Sheet** (backup log) — written by a **Google Apps Script Web App**.
2. **Buttondown** (<https://buttondown.com/the.sumeetsonian>) — the actual
   service used to compose and send the newsletter.

### (a) Google Sheet backup log

The Web App URL lives in `_config.yml`:

```yaml
newsletter_endpoint: "https://script.google.com/macros/s/.../exec"
```

The form does a `fetch` POST (form-urlencoded, `mode: 'no-cors'`) of the `email`
field to that endpoint. The Apps Script `doPost(e)` reads `e.parameter.email`
and appends `[timestamp, email]` as a new row. This is an intentional backup log
and stays as-is.

### (b) Buttondown (the sending service)

Buttondown is where the newsletter is actually composed and sent. The form also
POSTs the same `email` to Buttondown's public, no-API-key **embed-subscribe**
endpoint. Only the username is stored in `_config.yml` (non-secret); the URL is
built from it in the Liquid template:

```yaml
buttondown_username: "the.sumeetsonian"
```

→ `https://buttondown.com/api/emails/embed-subscribe/the.sumeetsonian`

**Double opt-in:** Buttondown likely has double opt-in enabled by default, so a
new subscriber may receive a **confirmation email** and won't be fully
subscribed until they click the link in it. This is expected — don't be
surprised if the Sheet has an email that isn't yet confirmed in Buttondown. You
can change this in the Buttondown settings if you prefer single opt-in.

### Opaque responses (both endpoints)

Neither endpoint returns usable CORS headers, so the browser sees *opaque*
responses — we can't read status or body. The accepted pattern is to treat a
resolved `fetch` promise as success (and a rejected promise, e.g. a network
failure, as an error). The success/thank-you message is keyed off the Google
Sheet request.

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

## Checking Buttondown subscribers

Log in at <https://buttondown.com/the.sumeetsonian> to see the subscriber list,
compose issues, and send the newsletter. Remember that double opt-in means a
subscriber only appears as confirmed once they click the confirmation email.

## Changing the Buttondown account

If the Buttondown username ever changes, update `buttondown_username` in
`_config.yml`; the embed-subscribe URL is derived from it automatically. Setting
it to `""` disables the second (Buttondown) write while leaving the Google Sheet
backup log intact.

An RSS feed is also available at `/feed.xml` (via `jekyll-feed`) for readers and
RSS-to-email tools.
