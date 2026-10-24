---
description: "List the Amplify rules, skills, hooks and verifier Claude can see (R1)"
argument-hint: "[work-item-id] [your extra words]"
---
READINESS - check that the Amplify rails are loaded in this session.

Without changing any file, list in a short table:
1. The project rules you loaded (CLAUDE.md) - name the artifact chain and the protected paths it describes.
2. The skills you can use (expect `opm-web-standards`).
3. The subagents you can start (expect `verifier`).
4. The hooks that run on this project (expect sync_repo at session start, protect_paths on Edit/Write and log_activity on prompts, tools and stops).
5. The /amplify commands available to me.
6. The work item from `amplify.json` (id, name, risk tier) and whether `sdlc/work-items/<ID>/business-request.md` exists.
Finish with one line: RAILS OK, or RAILS MISSING followed by what is missing.

Arguments: $ARGUMENTS
