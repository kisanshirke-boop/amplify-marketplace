---
description: "Record Gate G3 - plan approved by the engineer (P10, G3)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

GATE G3 - record approval of the plan. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`. The arguments must name the approving engineer / tech lead; if not, STOP and ask.
Set plan.md Version 1.0, Status "Approved", approver and date as given, Version history row, nothing else.
Commit only plan.md: `approve(G3): plan <ID> v1.0 approved by <name>`
First check the document: if its Document control already shows Status "Approved" with an approver and date (the decision was recorded in Amplify AI Build Studio), run `git pull`, say so, change nothing and stop.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
