---
description: "Critical review of the spec before show & tell (P04)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

DESIGN stage - critical review of `sdlc/work-items/<ID>/spec.md`. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
Review it as a sceptical architect: testability of every AC, missing error and edge cases, security and privacy
(opm-web-standards), traceability to the intent, scope creep. Give a table Severity / Section / Finding / Proposed fix.
Then apply only the fixes I confirm, raise the version, add a Version history row, set Status "In review" and commit
`spec(<ID>): v0.x review findings applied`.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
