# Newsletter signups

The "Subscribe" form (rendered from `_includes/subscribe-form.html`) collects
email addresses and stores them in a **Google Sheet** via a **Google Apps Script
Web App**.

## How it works today

- The Web App URL lives in `_config.yml` under `newsletter_endpoint`.
- On submit, the form validates the email client-side and POSTs it as
  form-urlencoded data (`email=...`) to that endpoint using `fetch` with
  `mode: 'no-cors'`.
- The Apps Script's `doPost(e)` reads `e.parameter.email` and appends
  `[timestamp, email]` as a new row to the sheet, returning
  `{ result: "success" }`.
- Because Apps Script Web Apps don't send usable CORS headers, the `no-cors`
  response is *opaque* — the browser can't read it. This is expected: once the
  `fetch` promise resolves we treat it as success and show
  "Thanks — you're subscribed!". A rejected promise (e.g. offline) shows an
  inline error and re-enables the button.

## Checking who signed up

Open the Google Sheet backing the Apps Script Web App. Each row is one signup:
column A is the timestamp, column B is the email address. (The sheet is owned by
the same Google account that deployed the Apps Script project; manage or
re-deploy the script from that account's Apps Script dashboard.)

## Swapping to a real email service provider later

When you're ready to move off the Google Sheet to a dedicated ESP, you only need
to touch two things:

1. **`_config.yml`** — set `newsletter_endpoint` to the provider's form/POST
   endpoint (or set it to `""` to fall back to the "coming soon" message while
   you migrate).
2. **`_includes/subscribe-form.html`** — replace the JS submit handler with the
   provider's embed snippet, or point the same `fetch` at the new endpoint and
   adjust the field names to match what the provider expects.

Common providers and their embed/endpoint docs:

- **Buttondown** — <https://buttondown.email/> (action
  `https://buttondown.email/api/emails/embed-subscribe/USERNAME`)
- **Mailchimp** — <https://mailchimp.com/> (embedded form action URL)
- **ConvertKit** — <https://convertkit.com/> (form action URL)

Most ESPs give you a ready-made HTML form snippet you can paste directly in
place of the current form + script block.
