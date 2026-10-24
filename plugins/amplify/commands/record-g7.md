---
description: "Record the release after Gate G7 and tag it (P21, G7)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

GATE G7 - record the release. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`. The arguments must name the release approver and the change ticket; if not, STOP and ask.
Confirm the deploy.yml release run succeeded (ask me for the run URL). Set release-record.md Status "Released" with approver,
date, run URL and change ticket. Commit `approve(G7): release <ID> v<x.y.z> by <name>`, then create the tag `v<x.y.z>` (I confirm the push).
First check the document: if its Document control already shows Status "Released" with an approver and date (the decision was recorded in Amplify AI Build Studio), run `git pull`, say so, change nothing and stop.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
