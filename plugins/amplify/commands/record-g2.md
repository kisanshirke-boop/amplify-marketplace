---
description: "Record Gate G2 - spec approved by PO and Architect (P08, G2)"
argument-hint: "[work-item-id] [your extra words]"
---
GATE G2 - record approval of the specification. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
The arguments must name the approvers (Product Owner and Architect). If not, STOP and ask.
1. Check intent.md is Accepted and no decision is open in spec.md. If not, stop and list what is open.
2. Set spec.md Version 1.0, Status "Approved", approvers and date as given; Version history row; nothing else.
3. Commit only spec.md: `approve(G2): spec <ID> v1.0 approved by <names>`

Arguments: $ARGUMENTS
