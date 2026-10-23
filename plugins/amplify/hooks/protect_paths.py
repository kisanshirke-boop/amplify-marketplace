"""Approval gate (Gate G4) - runs automatically BEFORE Claude edits or writes any file.

Registered by the amplify plugin (hooks/hooks.json) under "PreToolUse" for the Edit / Write / MultiEdit tools.
Claude Code sends this script a JSON description of the edit on standard input.

Protected paths (pipelines, infrastructure, governed templates, Claude's own guard-rails):
  - branch name has NO change ticket (CHG-####)  ->  "deny": the edit is blocked
  - branch name HAS a change ticket              ->  "ask":  a human must approve the edit
  - any other file                               ->  no output: normal permissions apply

If anything goes wrong inside this script, it BLOCKS (exit code 2). A gate must never fail open.
"""
import datetime
import json
import os
import re
import subprocess
import sys

PROTECTED = re.compile(
    r"(^|/)(\.github/workflows|infra|sdlc/templates|\.claude/hooks)/"
    r"|(^|/)\.claude/settings(\.local)?\.json$"
)


def decide(file_path, branch):
    path = file_path.replace("\\", "/")
    if not PROTECTED.search(path):
        return None
    ticket = re.search(r"CHG-\d+", branch or "")
    if ticket:
        return "ask", f"Protected path under {ticket.group(0)}: a human must approve this edit."
    return "deny", (
        "Protected path (pipelines, infrastructure, templates or guard-rails). "
        "Create a branch whose name contains a change ticket (CHG-####) first."
    )


def current_branch():
    project = os.environ.get("CLAUDE_PROJECT_DIR", ".")
    result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                            cwd=project, capture_output=True, text=True, check=False)
    return result.stdout.strip()


def log_gate(decision, file_path, branch, session):
    """Best effort: record the gate decision in the activity log. Never affects the decision."""
    try:
        project = os.environ.get("CLAUDE_PROJECT_DIR", ".")
        try:
            shown = os.path.relpath(file_path, project).replace("\\", "/")
        except ValueError:
            shown = file_path
        now = datetime.datetime.now()
        log_dir = os.path.join(project, "sdlc", "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, f"agent-activity-{now:%Y-%m-%d}.md")
        with open(log_file, "a", encoding="utf-8") as handle:
            handle.write(f"- {now:%H:%M:%S} [{session}] GATE   **{decision.upper()}** edit of `{shown}` "
                         f"(branch `{branch}`)\n")
    except Exception:  # noqa: BLE001 - logging must never break the gate
        pass


def main():
    event = json.load(sys.stdin)
    file_path = event.get("tool_input", {}).get("file_path", "")
    branch = current_branch()
    verdict = decide(file_path, branch)
    if verdict is None:
        return 0
    decision, reason = verdict
    log_gate(decision, file_path, branch, (event.get("session_id") or "------")[:6])
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                             "permissionDecision": decision,
                                             "permissionDecisionReason": reason}}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001 - fail CLOSED: exit 2 blocks the tool call
        print(f"protect_paths hook failed, blocking for safety: {exc}", file=sys.stderr)
        sys.exit(2)
