---
description: "Write the implementation plan (use plan mode) (P09)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

BUILD stage - implementation plan. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`. Work in plan mode (Shift+Tab) until I accept.
1. spec.md must be Approved. Read it, CLAUDE.md and `sdlc/templates/plan-template.md`.
2. Write `sdlc/work-items/<ID>/plan.md` Version 0.1 Status "Draft": small steps of a few hours each, every step with the
   files it touches, the tests that prove it and its verification command; Definition of Done; risks; Deviations section empty.
3. Map every FR/AC to at least one step. Commit `plan(<ID>): draft v0.1`.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
