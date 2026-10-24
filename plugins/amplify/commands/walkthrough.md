---
description: "Write a code walkthrough for the human reviewer (P13)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

BUILD stage - code walkthrough. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
Write `sdlc/work-items/<ID>/code-walkthrough.md` for a reviewer who has not seen the code: architecture in 5 lines,
request flow, each module and why it exists, where the security controls are (file:line), the riskiest code and why,
how to run it. Commit `docs(<ID>): code walkthrough`.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
