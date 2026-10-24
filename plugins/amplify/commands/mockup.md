---
description: "Build a clickable HTML mock-up from the spec (P06)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

DESIGN stage - clickable mock-up for show & tell. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
1. Read spec.md and the `opm-web-standards` skill (UX rules and references/brand-tokens.css).
2. Create ONE self-contained file `sdlc/work-items/<ID>/mockups/<app-slug>-mockup.html` - no external CDN, inline CSS and JS,
   fictitious data only, every main screen reachable with clicks, small yellow annotations naming the FR each screen covers.
3. Commit `design(<ID>): clickable mock-up v0.1`. Tell me which FRs are visible and which are not.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
