---
name: opm-web-standards
description: OPmobility standards for internal web applications - permitted technologies, security and privacy, delivery, and UX/brand. Use whenever writing or reviewing an intent, spec, plan, mock-up, code or pull request for any OPmobility web application.
---
# OPmobility internal web application standards

Version 1.0 (demo edition) · Owner: D&IS Global Practice – Digital Solutions & AI · Applies to every internal web application built with Claude.

When a request conflicts with these standards, do **not** silently resolve it: raise it as a question, propose options, and record the decision in the spec's decisions log.

## 1. Permitted technologies

| Layer | Permitted (Phase 1) | Not permitted without architecture approval |
|---|---|---|
| Language / framework | Python 3.12+ with Flask 3; or Node.js 20+ with Express | Other frameworks |
| Data | SQLite for prototypes and demos; Azure SQL for production | Other databases, ORMs not listed |
| Front end | Server-rendered HTML (Jinja templates) + the OPmobility CSS in `references/brand-tokens.css` | JavaScript frameworks (React, Angular, Vue); CSS frameworks; external CDNs |
| Forms / CSRF | Flask-WTF | Hand-written CSRF logic |
| Testing | pytest, pytest-cov, pytest-html | – |
| Code quality | ruff | – |
| Hosting (target) | Azure App Service | Other hosting |
| Identity (production) | Microsoft Entra ID single sign-on with app roles | Local user databases in production |
| Source control and CI/CD | GitHub, GitHub Actions | – |

## 2. Security and privacy

- **Least data:** collect only the personal data the business need requires; state purpose and retention in the spec.
- **Business contact data is personal data (GDPR):** restrict who can change it; keep it only while needed; use fictitious data in demos and tests.
- **Authorisation:** every data-changing action (create, edit, delete) is restricted to the authorised role and is checked on the server, not only hidden in the UI.
- **Injection:** parameterised SQL only. Never build SQL with string formatting.
- **Output:** escape all output (Jinja autoescape on). No `|safe` on user data.
- **Forms:** CSRF protection on every form. State-changing actions use POST, never GET.
- **Secrets:** from environment variables only; never in code, tests or the repository.
- **Logging:** log events (e.g. "contact 12 updated"), never personal data values.
- **Errors:** show a friendly message; never show stack traces to users.
- **Dependencies:** only those in `requirements.txt`; no packages outside the permitted list.

## 3. Delivery

- Work flows through the artifact chain: intent -> spec -> plan -> code, with human gates G1-G7.
- Small steps; each step proven by tests before the next starts. Every route has at least one test.
- Minimum test coverage 80 %; lint clean (ruff).
- Every change reaches Production only via: pull request review -> Quality check -> business UAT -> release approval.
- Evidence (test report, verifier report, UAT sign-off) is stored in the work item folder.

## 4. UX and brand

1. **Language:** English for all user-facing text. Plain, short labels; sentence case.
2. **Brand:** use the colours, fonts and spacing defined in `references/brand-tokens.css`. Do not invent new colours.
3. **Layout:** every screen follows `references/ux-template.html` so that all OPmobility internal applications look the same:
   - dark brand header with the OPmobility wordmark area (left) and the application name;
   - role badge in the header (e.g. "Read-only" / "Editor");
   - page title, then a toolbar (search on the left, primary action on the right);
   - content in white cards; data in tables with a header row and hover highlight;
   - forms: one column, label above field, required fields marked *, help text under the field, errors in red under the field;
   - buttons: one primary action per screen (brand blue), secondary (outline), destructive (red, always with confirmation);
   - footer: "Internal use only · OPmobility D&IS" and the application version.
4. **Accessibility:** WCAG 2.1 AA contrast; every input has a label; keyboard usable; visible focus outline.
5. **Responsive:** usable on a laptop and a 10-inch tablet.
6. **Messages:** confirm every successful change ("Contact saved."); empty states explain what to do next.

### Reference files (read them before designing screens)
- `references/brand-tokens.css` – colour, font and spacing tokens. **The values are placeholders until confirmed against the official OPmobility brand guidelines** (see the comment at the top of the file).
- `references/ux-template.html` – the reference screen layout and components. Open it in a browser to see it.
- `references/previous-apps/` – screenshots or HTML of earlier OPmobility applications, used to refine this template.
