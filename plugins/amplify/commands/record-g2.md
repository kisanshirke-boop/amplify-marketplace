---
description: "Record Gate G2 - spec approved by PO and Architect (P08, G2)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

GATE G2 - record approval of the specification. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
The arguments must name the approvers (Product Owner and Architect). If not, STOP and ask.
1. Check intent.md is Accepted and no decision is open in spec.md. If not, stop and list what is open.
2. Set spec.md Version 1.0, Status "Approved", approvers and date as given; Version history row; nothing else.
3. Commit only spec.md: `approve(G2): spec <ID> v1.0 approved by <names>`
First check the document: if its Document control already shows Status "Approved" with an approver and date (the decision was recorded in Amplify AI Build Studio), run `git pull`, say so, change nothing and stop.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
