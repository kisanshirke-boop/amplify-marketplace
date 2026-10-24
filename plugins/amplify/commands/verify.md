---
description: "Run the independent verifier subagent (P14)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

TEST stage - independent verification. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
Start the `verifier` subagent on this work item. Do not summarise or soften its result.
Save its answer unchanged to `sdlc/work-items/<ID>/evidence/verifier-report.md`, also save the HTML test report with
`python -m pytest -v --cov=app --cov-report=term-missing --html=sdlc/work-items/<ID>/evidence/test-report.html --self-contained-html`,
and commit `test(<ID>): verifier report and test evidence`. If the verdict is FAIL, list what must be fixed.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
