---
description: "Write UAT cases and the sign-off sheet (P18)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

DEPLOY stage - UAT. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
From spec.md write `uat/uat-cases.md` (cases UAT-xx traced to FR-xx, steps in business language, expected result)
and `uat/uat-signoff.md` Status "Pending" from their templates. Commit `uat(<ID>): UAT cases and sign-off sheet`.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
