"""Self-test for the hooks. Run from the project folder:   python .claude/hooks/selftest_hook.py

It feeds the hooks exactly the JSON that Claude Code sends, and checks what they do.
Always test the DENY path: a gate that has never been seen to block is not a gate.
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
GATE = os.path.join(HERE, "protect_paths.py")
LOGGER = os.path.join(HERE, "log_activity.py")
sys.path.insert(0, HERE)
from protect_paths import decide  # noqa: E402

CASES = [
    ("app/routes.py", "feature/CH-001-contact-hub", None),
    ("sdlc/work-items/CH-001-contact-hub/intent.md", "feature/CH-001-contact-hub", None),
    (".github/workflows/ci.yml", "feature/CH-001-contact-hub", "deny"),
    ("sdlc/templates/intent-template.md", "feature/CH-001-contact-hub", "deny"),
    (".claude/hooks/protect_paths.py", "feature/CH-001-contact-hub", "deny"),
    (".claude/settings.json", "main", "deny"),
    (".github/workflows/ci.yml", "change/CHG-1001-nightly-tests", "ask"),
    ("C:\\Demo\\contact-hub\\.github\\workflows\\deploy.yml", "main", "deny"),
]


def run(script, payload, env=None):
    return subprocess.run([sys.executable, script], input=payload, capture_output=True,
                          text=True, check=False, env=env)


SANDBOX = tempfile.mkdtemp()  # keeps test entries out of the real activity log
SANDBOX_ENV = dict(os.environ, CLAUDE_PROJECT_DIR=SANDBOX)

ok = True
print("1) Gate decision rules (protect_paths.py)")
for path, branch, expected in CASES:
    got = decide(path, branch)
    got = got[0] if got else None
    passed = got == expected
    ok &= passed
    print(f"   {'PASS' if passed else 'FAIL'}  {path[:46]:<46} {branch[:30]:<30} -> {got or 'allowed'}")

print("2) Live gate call, exactly as Claude Code makes it")
edit = json.dumps({"hook_event_name": "PreToolUse", "tool_name": "Edit",
                   "tool_input": {"file_path": ".github/workflows/deploy.yml"}})
live = run(GATE, edit, SANDBOX_ENV)
print(f"   exit code: {live.returncode}   decision: "
      f"{'deny' if 'deny' in live.stdout else 'ask' if 'ask' in live.stdout else 'none'}")
ok &= live.returncode == 0 and '"permissionDecision"' in live.stdout

print("3) Broken input must BLOCK the edit (exit code 2) - the gate never fails open")
bad = run(GATE, "this is not json", SANDBOX_ENV)
print(f"   exit code: {bad.returncode}  (expected 2)")
ok &= bad.returncode == 2

print("4) Activity log hook writes a line and never blocks")
with tempfile.TemporaryDirectory() as tmp:
    env = dict(os.environ, CLAUDE_PROJECT_DIR=tmp)
    prompt = json.dumps({"hook_event_name": "UserPromptSubmit", "session_id": "selftest",
                         "prompt": "Readiness self-test prompt"})
    first = run(LOGGER, prompt, env)
    broken = run(LOGGER, "not json", env)
    logs = os.listdir(os.path.join(tmp, "sdlc", "logs"))
    written = bool(logs) and "Readiness self-test prompt" in open(
        os.path.join(tmp, "sdlc", "logs", logs[0]), encoding="utf-8").read()
print(f"   line written: {written}   exit codes: {first.returncode}, {broken.returncode} (expected 0, 0)")
ok &= written and first.returncode == 0 and broken.returncode == 0

verdict = "ALL CHECKS PASSED - the hooks are working" if ok else "SOMETHING FAILED - do not rely on the hooks yet"
print("\nRESULT:", verdict)
sys.exit(0 if ok else 1)
