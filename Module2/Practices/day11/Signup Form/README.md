# Validated, Persistent Signup Form

A simple signup form that validates a name and an Ethiopian phone number, shows clear error messages, and saves valid entries to `localStorage` as JSON, restored on reload.

## How to run

1. Open `index.html` in a web browser.
2. Enter a name and phone number.
3. Click **Sign Up**.
4. The form validates, saves the entry, and updates the counter.
5. Reload the page — the counter remains.

## Validation rules

- Name must be at least 2 characters.
- Phone must match `09xxxxxxxx` or `+2519xxxxxxxx`.

## Storage

- Valid entries are stored in `localStorage` under the key `signups` as a JSON array.
- Corrupt or missing data is handled safely with `try/catch` and a fallback to an empty array.