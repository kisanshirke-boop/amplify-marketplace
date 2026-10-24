---
description: "Draft the spec from the accepted intent (P03)"
argument-hint: "[work-item-id] [your extra words]"
---
SYNC FIRST: run `git pull --ff-only` so you work on the latest version, including gate decisions recorded in Amplify AI Build Studio. If it fails (local changes or a diverged branch), stop and tell me what to do.

DESIGN stage - draft the specification. Work item: the ID given in the arguments below if any, otherwise the `id` in `amplify.json` at the repository root. Its folder is `sdlc/work-items/<ID>/`.

1. Check `intent.md` has Status "Accepted". If not, stop and say so.
2. Read `sdlc/templates/spec-template.md` and the `opm-web-standards` skill. Follow the template exactly.
3. Create `sdlc/work-items/<ID>/spec.md` Version 0.1 Status "Draft": functional requirements FR-xx, each with
   Given/When/Then acceptance criteria AC-x.y, non-functional requirements, data, roles, and a Decisions log.
4. Use only technologies on the permitted list in the skill. Put open design questions in the Decisions log.
5. Commit only spec.md: `spec(<ID>): draft v0.1 from accepted intent`
6. Ask me open decisions one at a time. Never set a status to Accepted, Approved, Signed or Released on your own - only record a decision the named human states in this prompt.

SYNC LAST: after your final commit run `git push -u origin HEAD` (I confirm the push), so GitHub and Amplify AI Build Studio show the new version. If the push is rejected, run `git pull --rebase`, then push again.

Arguments: $ARGUMENTS
