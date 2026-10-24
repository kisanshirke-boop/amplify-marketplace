---
description: "Record Gate G6 - UAT signed by the business user (P19, G6)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

GATE G6 - record UAT sign-off. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`. The arguments must name the business user who signed and the build tested; if not, STOP and ask.
Record each case result as told, set uat-signoff.md Status "Signed" with name and date, Version history row.
Commit only the uat files: `approve(G6): UAT <ID> signed by <name>`
First check the document: if its Document control already shows Status "Signed" with an approver and date (the decision was recorded in Amplify AI Build Studio), run `git pull`, say so, change nothing and stop.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
