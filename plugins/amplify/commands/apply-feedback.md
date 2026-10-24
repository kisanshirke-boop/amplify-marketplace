---
description: "Apply show & tell feedback to spec and mock-up (P07)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

DESIGN stage - apply the show & tell feedback I give in the arguments or in `mockups/show-and-tell-feedback.md`. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
Record each feedback item, update spec.md (new version, Decisions log, mark "Changes intent?") and the mock-up
(new version), then commit `design(<ID>): show & tell feedback applied`. If the intent changes, tell me to run /amplify:update-intent.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
