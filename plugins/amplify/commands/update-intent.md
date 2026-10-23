---
description: "Re-version the intent after a design decision changed it (P05, G1)"
argument-hint: "[work-item-id] [your extra words]"
---
DESIGN stage - a decision in spec.md changes the intent. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
1. Find the decision(s) marked "Changes intent? Yes" in the spec Decisions log.
2. Update intent.md accordingly: new minor version, Version history row, Status back to "Clarified".
3. Commit `intent(<ID>): v1.x updated after design decision <D-xx>` and tell me it needs re-acceptance at G1.

Arguments: $ARGUMENTS
