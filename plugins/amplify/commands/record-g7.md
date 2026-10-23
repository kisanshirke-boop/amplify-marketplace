---
description: "Record the release after Gate G7 and tag it (P21, G7)"
argument-hint: "[work-item-id] [your extra words]"
---
GATE G7 - record the release. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`. The arguments must name the release approver and the change ticket; if not, STOP and ask.
Confirm the deploy.yml release run succeeded (ask me for the run URL). Set release-record.md Status "Released" with approver,
date, run URL and change ticket. Commit `approve(G7): release <ID> v<x.y.z> by <name>`, then create the tag `v<x.y.z>` (I confirm the push).

Arguments: $ARGUMENTS
