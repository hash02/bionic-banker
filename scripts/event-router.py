"""
Event Router - bionicbanker.tech
Central dispatcher: maps events → actions.
The brain of Level 4 reactive automation.

Usage:
  python scripts/event-router.py --event new_article --target my-post.html
  python scripts/event-router.py --event health_fail --detail "Article count mismatch"
  python scripts/event-router.py --event push_success --detail "Deployed 2 files"
  python scripts/event-router.py --event stale_detected --detail "TASK-025 idle 12 days"
  python scripts/event-router.py --event pattern_detected --detail "headings failed 5x"
  python scripts/event-router.py --event rule_proposed --detail "Auto-fix empty headings" --target content-audit-auto.py
  python scripts/event-router.py --event rule_activated --detail "Empty heading rule added" --target content-audit-auto.py

Events: new_article, health_fail, push_success, stale_detected (L4)
        pattern_detected, rule_proposed, rule_activated (L5)

Modes: --local (Windows paths) | --repo (relative paths for GitHub Actions)
"""
import os, sys, subprocess, io
from datetime import datetime

# Fix Windows console encoding (skip if already wrapped or on CI)
try:
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
except Exception:
    pass

NOW = datetime.now()
DATE_STR = NOW.strftime("%Y-%m-%d")
TIME_STR = NOW.strftime("%Y-%m-%d %H:%M")

MODE = "repo" if "--repo" in sys.argv else "local"

# Parse args
event = None
target = None
detail = None
args = sys.argv[1:]
i = 0
while i < len(args):
    if args[i] == "--event" and i + 1 < len(args):
        event = args[i + 1]; i += 2
    elif args[i] == "--target" and i + 1 < len(args):
        target = args[i + 1]; i += 2
    elif args[i] == "--detail" and i + 1 < len(args):
        detail = args[i + 1]; i += 2
    else:
        i += 1

if not event:
    print("Error: --event required")
    print("Events: new_article, health_fail, push_success, stale_detected")
    sys.exit(1)

# Paths
if MODE == "local":
    WS = r"C:\Users\himan\OneDrive\hash 2026"
    BB = os.path.join(WS, "bionic-banker")
    OUTBOX = os.path.join(WS, "clode code", "OUTBOX.md")
    INBOX = os.path.join(WS, "clode code", "INBOX.md")
    SESSLOG = os.path.join(WS, "SESSION_LOG.md")
    MEMORY = os.path.join(WS, "memory")
else:
    BB = os.getcwd()
    WS = BB
    OUTBOX = os.path.join(BB, "memory", "outbox-events.md")
    INBOX = None  # Don't modify INBOX from repo mode
    SESSLOG = None  # SESSION_LOG not in repo
    MEMORY = os.path.join(BB, "memory")

os.makedirs(MEMORY, exist_ok=True)

def append_file(path, content):
    """Append content to a file, creating it if it doesn't exist."""
    if not path:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    mode_flag = "a" if os.path.exists(path) else "w"
    with open(path, mode_flag, encoding="utf-8") as f:
        f.write(content)

def handle_new_article():
    """Run content audit on the target file."""
    if not target:
        print("Error: --target required for new_article event")
        sys.exit(1)

    print(f"[EVENT] new_article: {target}")
    script = os.path.join(BB, "scripts", "content-audit-auto.py")
    if not os.path.exists(script):
        print(f"Error: content-audit-auto.py not found at {script}")
        sys.exit(1)

    # Run content audit in --changed mode
    result = subprocess.run(
        [sys.executable, script, "--changed"],
        capture_output=True, text=True, cwd=BB
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

    # Log the event
    append_file(
        OUTBOX if MODE == "local" else os.path.join(MEMORY, "outbox-events.md"),
        f"\n## [EVENT] New Article Detected — {TIME_STR}\n- File: {target}\n- Content audit executed\n"
    )

def handle_health_fail():
    """Alert OUTBOX and flag in INBOX."""
    desc = detail or "Unknown health check failure"
    print(f"[EVENT] health_fail: {desc}")

    # Write to OUTBOX
    append_file(
        OUTBOX,
        f"\n## ⚠️ Health Check Failed — {TIME_STR}\n- {desc}\n- Action required: review and fix\n"
    )

    # Flag in INBOX (local mode only — INBOX is a workspace file)
    if INBOX and MODE == "local":
        append_file(
            INBOX,
            f"\n## ⚠️ AUTO-FLAG: Health Check Failure — {DATE_STR}\n- {desc}\n- Routed by event-router.py\n"
        )

    print(f"Alert written to OUTBOX")

def handle_push_success():
    """Log to SESSION_LOG."""
    desc = detail or "Push completed"
    print(f"[EVENT] push_success: {desc}")

    if SESSLOG:
        append_file(
            SESSLOG,
            f"\n- **{DATE_STR}** [AUTO] {desc}\n"
        )
        print(f"Logged to SESSION_LOG")
    else:
        # Repo mode — log to memory
        append_file(
            os.path.join(MEMORY, "outbox-events.md"),
            f"\n## [LOG] Push Success — {TIME_STR}\n- {desc}\n"
        )
        print("Logged to memory/outbox-events.md")

def handle_stale_detected():
    """Write recommendation to OUTBOX."""
    desc = detail or "Staleness detected"
    print(f"[EVENT] stale_detected: {desc}")

    append_file(
        OUTBOX,
        f"\n## 📋 Staleness Alert — {TIME_STR}\n- {desc}\n- Recommendation: review and update or close\n"
    )
    print("Recommendation written to OUTBOX")


def handle_pattern_detected():
    """L5: Pattern detected by outcome tracker. Write to OUTBOX + proposals."""
    desc = detail or "Recurring pattern detected"
    print(f"[EVENT] pattern_detected: {desc}")

    # Write to OUTBOX
    append_file(
        OUTBOX,
        f"\n## 🔍 Pattern Detected — {TIME_STR}\n- {desc}\n- Action: rule-proposer.py will generate a fix proposal\n"
    )

    # Write raw observation to proposals.md
    proposals_path = os.path.join(MEMORY, "proposals.md") if MODE == "repo" else os.path.join(WS, "bionic-banker", "memory", "proposals.md")
    if not os.path.exists(proposals_path):
        append_file(proposals_path, "# Rule Proposals — L5 Adaptive\n\n> HASH marks proposals [APPROVED] or [REJECTED] inline.\n\n---\n")
    append_file(
        proposals_path,
        f"\n## OBSERVATION — {DATE_STR}\n- {desc}\n- Awaiting rule-proposer.py to generate formal proposal\n"
    )
    print("Pattern logged to OUTBOX + proposals.md")


def handle_rule_proposed():
    """L5: Rule proposer generated a new rule. Alert OUTBOX."""
    desc = detail or "New rule proposed"
    tgt = target or "unknown"
    print(f"[EVENT] rule_proposed: {desc}")

    append_file(
        OUTBOX,
        f"\n## 📝 Rule Proposed — {TIME_STR}\n- {desc}\n- Target: {tgt}\n- Action: HASH review needed in memory/proposals.md\n"
    )
    print("Proposal alert written to OUTBOX")


def handle_rule_activated():
    """L5: Rule approved and implemented. Log everywhere."""
    desc = detail or "Rule activated"
    tgt = target or "unknown"
    print(f"[EVENT] rule_activated: {desc}")

    # Log to OUTBOX
    append_file(
        OUTBOX,
        f"\n## ⚡ Rule Activated — {TIME_STR}\n- {desc}\n- Target: {tgt}\n- The agent just improved itself.\n"
    )

    # Log to SESSION_LOG (local mode)
    if SESSLOG:
        append_file(
            SESSLOG,
            f"\n- **{DATE_STR}** [L5-AUTO] Rule activated: {desc} → {tgt}\n"
        )
        print("Logged to SESSION_LOG")
    else:
        append_file(
            os.path.join(MEMORY, "outbox-events.md"),
            f"\n## [L5] Rule Activated — {TIME_STR}\n- {desc}\n- Target: {tgt}\n"
        )
        print("Logged to memory/outbox-events.md")


# Route events
ROUTES = {
    "new_article": handle_new_article,
    "health_fail": handle_health_fail,
    "push_success": handle_push_success,
    "stale_detected": handle_stale_detected,
    "pattern_detected": handle_pattern_detected,
    "rule_proposed": handle_rule_proposed,
    "rule_activated": handle_rule_activated,
}

handler = ROUTES.get(event)
if handler:
    handler()
    print(f"\n✅ Event '{event}' routed successfully")
else:
    print(f"Error: unknown event '{event}'")
    print(f"Valid events: {', '.join(ROUTES.keys())}")
    sys.exit(1)
