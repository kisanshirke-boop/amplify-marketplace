---
description: "Run the release gate check and prepare the release record (P20)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

DEPLOY stage - release record. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.
1. Run `python tools/release_gate_check.py <ID>` and show the table.
2. Write `release/release-record.md` from its template, Status "Planned", with the gate check output, version, build and change ticket.
3. Commit `release(<ID>): release record v<x.y.z> planned`. The release itself is Gate G7: a release approver runs deploy.yml.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
