---
description: "Implement the next plan step with tests in the loop (P12)"
argument-hint: "[work-item-id] [your extra words]"
---
BUILD stage - implement. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
1. plan.md must be Approved. Take the next unticked step only (or the step number given in the arguments).
2. Implement it with tests. Run `python -m pytest -q` and `python -m ruff check .`; fix until both pass.
3. Append an entry to `build-journal.md` (template in sdlc/templates/), tick the step in plan.md.
4. Commit `feat(<ID>): step <n> - <title>`. Then stop and tell me what changed and what is next.
Any deviation from the plan: record it under Deviations in plan.md BEFORE making it, and tell me.

Arguments: $ARGUMENTS
