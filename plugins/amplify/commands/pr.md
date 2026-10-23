---
description: "Open a traceable pull request (P16, G5)"
argument-hint: "[work-item-id] [your extra words]"
---
DEPLOY stage - pull request. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
1. Write `sdlc/work-items/<ID>/pr-description.md` from `sdlc/templates/pr-description-template.md`
   (traceability table with versions and gate approvals, evidence, deviations, reviewer focus).
2. Commit `docs(<ID>): PR description`, push, and open the PR with `gh pr create --body-file` (or give me the text to paste).
3. Remind me: the author cannot approve; a reviewer approves at G5 after the Claude policy review.

Arguments: $ARGUMENTS
