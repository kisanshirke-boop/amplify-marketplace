---
description: "Draft the intent from the business request, then interview me (P01)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

PLAN stage - draft the intent. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.

1. Read `sdlc/work-items/<ID>/business-request.md` and the template `sdlc/templates/intent-template.md`.
   Follow the template's structure exactly, including the Document control table.
2. Create `sdlc/work-items/<ID>/intent.md` - Version 0.1, Status "Draft". Product Owner: as named in the business request.
3. Write in business language only. Do not propose technology, screens or design.
4. Do not guess. Anything missing or ambiguous goes into "Open questions"
   (aim for the 8-12 questions that matter: users and access, data, rules, privacy, AI use, scope, success).
5. Commit only that file: `intent(<ID>): draft v0.1 from business request`
6. Then ask me the open questions ONE AT A TIME. Wait for my answer before asking the next one.
7. When every question is answered: record the answers, set Version 0.2 and Status "Clarified", add a
   Version history row, summarise what changed, and commit: `intent(<ID>): v0.2 clarified with product owner`
Never set a status to Accepted, Approved, Signed or Released on your own - only record a decision the named human states in this prompt.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
