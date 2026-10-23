---
description: "Record Gate G1 - intent accepted by the named Product Owner (P02, G1)"
argument-hint: "[work-item-id] [your extra words]"
---
GATE G1 - record the Product Owner's acceptance of the intent. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
The arguments name the approver, e.g. `/amplify:record-g1 QI-015 accepted by Jane Doe`. If no approver name is given, STOP and ask.

1. In `sdlc/work-items/<ID>/intent.md` set Version to 1.0 (or the next major) and Status to "Accepted".
2. Fill "Accepted by" and "Accepted on" (today) exactly as given; tick the Gate G1 checklist; Decision "Accepted".
3. Add a Version history row. Change nothing else.
4. Commit only intent.md: `approve(G1): intent <ID> v1.0 accepted by <name>`
5. Show the Document control table and the commit hash.

Arguments: $ARGUMENTS
