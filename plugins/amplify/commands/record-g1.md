---
description: "Record Gate G1 - intent accepted by the named Product Owner (P02, G1)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

GATE G1 - record the Product Owner's acceptance of the intent. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
The arguments name the approver, e.g. `/amplify:record-g1 QI-015 accepted by Jane Doe`. If no approver name is given, STOP and ask.

1. In `sdlc/work-items/<ID>/intent.md` set Version to 1.0 (or the next major) and Status to "Accepted".
2. Fill "Accepted by" and "Accepted on" (today) exactly as given; tick the Gate G1 checklist; Decision "Accepted".
3. Add a Version history row. Change nothing else.
4. Commit only intent.md: `approve(G1): intent <ID> v1.0 accepted by <name>`
5. Show the Document control table and the commit hash.
First check the document: if its Document control already shows Status "Accepted" with an approver and date (the decision was recorded in Amplify AI Build Studio), run `git pull`, say so, change nothing and stop.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
