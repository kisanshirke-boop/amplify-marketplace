---
description: "Re-version the intent after a design decision changed it (P05, G1)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

DESIGN stage - a decision in spec.md changes the intent. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
1. Find the decision(s) marked "Changes intent? Yes" in the spec Decisions log.
2. Update intent.md accordingly: new minor version, Version history row, Status back to "Clarified".
3. Commit `intent(<ID>): v1.x updated after design decision <D-xx>` and tell me it needs re-acceptance at G1.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
