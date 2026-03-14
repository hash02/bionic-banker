"""
Auto-Push Script - bionic-banker repo
Stages, commits, and pushes uncommitted changes.
Skips .env/secret files. Handles merge conflicts gracefully.
"""
import os
import subprocess
import sys
from datetime import datetime

REPO_DIR = r"C:\Users\himan\OneDrive\hash 2026\bionic-banker"
OUTBOX = r"C:\Users\himan\OneDrive\hash 2026\clode code\OUTBOX.md"
DATE_STR = datetime.now().strftime("%Y-%m-%d %H:%M")

SKIP_PATTERNS = [".env", "credentials", "secret", ".key", ".pem", "token"]


def run(cmd, cwd=REPO_DIR):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=True)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def log_outbox(msg):
    if os.path.exists(OUTBOX):
        with open(OUTBOX, "a", encoding="utf-8") as f:
            f.write(f"\n\n## Auto-Push - {DATE_STR}\n{msg}\n")


def main():
    if not os.path.isdir(REPO_DIR):
        print(f"Repo not found: {REPO_DIR}")
        sys.exit(1)

    code, status, _ = run("git status --porcelain")
    if not status:
        print("No changes to push.")
        sys.exit(0)

    changed_files = [line[3:] for line in status.split("\n") if line.strip()]
    print(f"Found {len(changed_files)} changed file(s)")

    safe_files = []
    skipped = []
    for f in changed_files:
        if any(p in f.lower() for p in SKIP_PATTERNS):
            skipped.append(f)
        else:
            safe_files.append(f)

    if skipped:
        print(f"Skipping sensitive files: {', '.join(skipped)}")

    if not safe_files:
        print("Only sensitive files changed - nothing to push.")
        sys.exit(0)

    for f in safe_files:
        run(f'git add "{f}"')

    if len(safe_files) <= 5:
        file_list = ", ".join(os.path.basename(f) for f in safe_files)
    else:
        file_list = f"{len(safe_files)} files"
    commit_msg = f"Auto-push: updated {file_list}"

    code, out, err = run(f'git commit -m "{commit_msg}"')
    if code != 0:
        print(f"Commit failed: {err}")
        log_outbox(f"Commit FAILED: {err}")
        sys.exit(1)
    print(f"Committed: {commit_msg}")

    code, out, err = run("git push origin main")
    if code != 0:
        if "conflict" in err.lower() or "rejected" in err.lower():
            print("Push rejected (likely merge conflict). NOT force-pushing.")
            print(f"Error: {err}")
            log_outbox(f"Push REJECTED (merge conflict): {err}\nChanges committed locally but not pushed.")
            sys.exit(1)
        else:
            print(f"Push failed: {err}")
            log_outbox(f"Push FAILED: {err}")
            sys.exit(1)

    result = f"Pushed {len(safe_files)} file(s): {commit_msg}"
    if skipped:
        result += f"\nSkipped sensitive: {', '.join(skipped)}"
    print(result)
    log_outbox(result)


if __name__ == "__main__":
    main()
