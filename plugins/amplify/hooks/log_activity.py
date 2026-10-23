"""Activity log ("flight recorder") - runs automatically on these Claude Code events:

  UserPromptSubmit  -> PROMPT  what the human asked
  PostToolUse       -> TOOL    every tool Claude used (file read/edit, command, search, subagent)
  Stop              -> DONE    end of Claude's turn, with the first line of its reply

Registered in .claude/settings.json. Writes one readable line per event to
sdlc/logs/agent-activity-<YYYY-MM-DD>.md. Lines from a subagent are tagged, e.g. [verifier].

Optional: when AMPLIFY_STUDIO_URL and AMPLIFY_INGEST_TOKEN are set (user env or managed settings "env"),
the same line is also sent to the Studio so the Activity tab shows it live.

Unlike the protect_paths gate, this hook must NEVER block Claude: whatever happens,
it prints nothing and exits 0 ("fail open" is correct for logging, wrong for a gate).
"""
import datetime
import json
import os
import sys
import urllib.request

MAX = 160  # characters kept per entry


def short(text, limit=MAX):
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[: limit - 3] + "..."


def rel(path, project):
    try:
        return os.path.relpath(path, project).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def describe_tool(event, project):
    name = event.get("tool_name", "?")
    data = event.get("tool_input", {}) or {}
    if "file_path" in data:
        return f"{name:<9} `{rel(data['file_path'], project)}`"
    if name in ("Bash", "PowerShell"):
        return f"{name:<9} `{short(data.get('command', ''), 120)}`"
    if name in ("Grep", "Glob"):
        return f"{name:<9} pattern `{short(data.get('pattern', ''), 80)}`"
    if name in ("Task", "Agent"):
        who = data.get("subagent_type") or data.get("agent_type") or "subagent"
        return f"{name:<9} started subagent **{who}**: {short(data.get('description', ''), 80)}"
    if name == "Skill":
        return f"{name:<9} loaded skill **{data.get('skill') or data.get('name', '?')}**"
    if name == "WebFetch":
        return f"{name:<9} {short(data.get('url', ''), 100)}"
    return name


def entry_for(event, project):
    kind = event.get("hook_event_name", "")
    if kind == "UserPromptSubmit":
        return f"PROMPT {short(event.get('prompt', ''))}"
    if kind == "PostToolUse":
        return f"TOOL   {describe_tool(event, project)}"
    if kind in ("Stop", "SubagentStop"):
        reply = (event.get("last_assistant_message") or "").strip().splitlines()
        first = short(reply[0], 120) if reply else ""
        return f"DONE   turn finished. {first}".rstrip()
    return f"EVENT  {kind}"


def write_line(line, project, session):
    now = datetime.datetime.now()
    log_dir = os.path.join(project, "sdlc", "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"agent-activity-{now:%Y-%m-%d}.md")
    new_file = not os.path.exists(log_file)
    with open(log_file, "a", encoding="utf-8") as handle:
        if new_file:
            handle.write(f"# Agent activity log - {now:%Y-%m-%d}\n\n"
                         "Written automatically by .claude/hooks/log_activity.py\n\n")
        handle.write(f"- {now:%H:%M:%S} [{session}] {line}\n")


def send_to_studio(line, project, session):
    """Best effort, 2-second timeout. The work item id comes from amplify.json in the project root."""
    url, token = os.environ.get("AMPLIFY_STUDIO_URL"), os.environ.get("AMPLIFY_INGEST_TOKEN")
    if not url or not token:
        return
    with open(os.path.join(project, "amplify.json"), encoding="utf-8") as handle:
        app_id = json.load(handle)["id"]
    kind = next((word for word in line.split() if not word.startswith("[")), "TOOL")
    body = json.dumps({"kind": kind, "text": f"[{session}] {line}"}).encode("utf-8")
    req = urllib.request.Request(f"{url.rstrip('/')}/api/ingest/{app_id}/activity", data=body, method="POST",
                                 headers={"Content-Type": "application/json", "X-Amplify-Token": token})
    urllib.request.urlopen(req, timeout=2).close()


def main():
    event = json.load(sys.stdin)
    project = os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or "."
    session = (event.get("session_id") or "------")[:6]
    agent = event.get("agent_type")
    line = entry_for(event, project)
    if agent:
        line = f"[{agent}] {line}"
    write_line(line, project, session)
    send_to_studio(line, project, session)


if __name__ == "__main__":
    try:
        main()
    except Exception:  # noqa: BLE001 - logging must never block Claude
        pass
    sys.exit(0)
