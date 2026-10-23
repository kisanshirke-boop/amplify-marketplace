---
description: "Record Gate G3 - plan approved by the engineer (P10, G3)"
argument-hint: "[work-item-id] [your extra words]"
---
GATE G3 - record approval of the plan. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`. The arguments must name the approving engineer / tech lead; if not, STOP and ask.
Set plan.md Version 1.0, Status "Approved", approver and date as given, Version history row, nothing else.
Commit only plan.md: `approve(G3): plan <ID> v1.0 approved by <name>`

Arguments: $ARGUMENTS
