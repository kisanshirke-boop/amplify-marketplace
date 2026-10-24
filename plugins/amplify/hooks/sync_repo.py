"""Start-of-session sync - runs automatically when a Claude Code session starts (SessionStart hook).

Pulls the latest commits of the current branch (fast-forward only), so decisions recorded in Amplify AI Build
Studio - gate approvals that update intent.md, spec.md, plan.md ... - are on the laptop before the next
/amplify command runs. Prints one line that Claude sees as session context.

Fails open: if there is no network, no upstream, local changes or a diverged history, it changes nothing
and says what to do. It never blocks the session.
"""
import os
import subprocess
import sys


def git(*args, timeout=25):
    project = os.environ.get("CLAUDE_PROJECT_DIR", ".")
    out = subprocess.run(["git", *args], cwd=project, capture_output=True, text=True, timeout=timeout, check=False)
    return out.returncode, (out.stdout + out.stderr).strip()


def main():
    code, branch = git("rev-parse", "--abbrev-ref", "HEAD")
    if code != 0:
        return
    code, upstream = git("rev-parse", "--abbrev-ref", "@{u}")
    if code != 0:
        print(f"Amplify sync: branch '{branch}' has no upstream yet - push it once with `git push -u origin HEAD`.")
        return
    if git("fetch", "--quiet")[0] != 0:
        print("Amplify sync: could not reach GitHub - working on the local copy; pull before the next /amplify command.")
        return
    _, behind = git("rev-list", "--count", f"HEAD..{upstream}")
    _, ahead = git("rev-list", "--count", f"{upstream}..HEAD")
    if behind.strip() in ("", "0"):
        note = f" ({ahead.strip()} local commit(s) not pushed yet - push them)" if ahead.strip() not in ("", "0") else ""
        print(f"Amplify sync: '{branch}' is up to date with {upstream}{note}.")
        return
    code, msg = git("pull", "--ff-only", "--quiet")
    if code == 0:
        print(f"Amplify sync: pulled {behind.strip()} new commit(s) from {upstream} (e.g. gate approvals from the Studio).")
    else:
        print(f"Amplify sync: {behind.strip()} new commit(s) on {upstream} could not be fast-forwarded "
              f"({msg.splitlines()[-1] if msg else 'local changes or diverged history'}). "
              "Ask the developer to commit or stash local changes, then run `git pull --rebase`.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001 - a sync helper must never block the session
        print(f"Amplify sync skipped: {exc}")
    sys.exit(0)
