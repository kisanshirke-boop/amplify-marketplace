---
description: "Run the independent verifier subagent (P14)"
argument-hint: "[work-item-id] [your extra words]"
---
TEST stage - independent verification. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
Start the `verifier` subagent on this work item. Do not summarise or soften its result.
Save its answer unchanged to `sdlc/work-items/<ID>/evidence/verifier-report.md`, also save the HTML test report with
`python -m pytest -v --cov=app --cov-report=term-missing --html=sdlc/work-items/<ID>/evidence/test-report.html --self-contained-html`,
and commit `test(<ID>): verifier report and test evidence`. If the verdict is FAIL, list what must be fixed.

Arguments: $ARGUMENTS
