---
description: "Implement the next plan step with tests in the loop (P12)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

BUILD stage - implement. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
1. plan.md must be Approved. Take the next unticked step only (or the step number given in the arguments).
2. Implement it with tests. Run `python -m pytest -q` and `python -m ruff check .`; fix until both pass.
3. Append an entry to `build-journal.md` (template in sdlc/templates/), tick the step in plan.md.
4. Commit `feat(<ID>): step <n> - <title>`. Then stop and tell me what changed and what is next.
Any deviation from the plan: record it under Deviations in plan.md BEFORE making it, and tell me.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
