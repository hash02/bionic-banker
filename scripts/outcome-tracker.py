"""
Outcome Tracker - bionicbanker.tech
Logs audit/health-check failures to memory/outcomes.json.
Detects recurring patterns (3+ = flag, 5+ = escalate).
Part of Level 5 Adaptive agent infrastructure.

Usage:
  python scripts/outcome-tracker.py --source content-audit --report memory/content-audit-2026-03-08.md
  python scripts/outcome-tracker.py --source health-check --report memory/health-check-auto-2026-03-08.md
  python scripts/outcome-tracker.py --source manual --check "JSON-LD" --detail "Missing structured data" --file "aave.html"
  python scripts/outcome-tracker.py --stats
"""
import os, sys, json, re, io
from datetime import datetime

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

NOW = datetime.now()
DATE_STR = NOW.strftime("%Y-%m-%d")
TIME_STR = NOW.strftime("%Y-%m-%dT%H:%M:%S")

BB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY = os.path.join(BB, "memory")
OUTCOMES_FILE = os.path.join(MEMORY, "outcomes.json")
SCRIPTS = os.path.join(BB, "scripts")

os.makedirs(MEMORY, exist_ok=True)


def load_outcomes():
    """Load existing outcomes.json or create empty structure."""
    if os.path.exists(OUTCOMES_FILE):
        with open(OUTCOMES_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Warning: outcomes.json corrupted, starting fresh")
    return {"outcomes": [], "patterns": [], "stats": {"total_outcomes": 0, "total_patterns": 0, "last_updated": TIME_STR}}


def save_outcomes(data):
    """Save outcomes.json."""
    data["stats"]["last_updated"] = TIME_STR
    data["stats"]["total_outcomes"] = len(data["outcomes"])
    data["stats"]["total_patterns"] = len(data["patterns"])
    with open(OUTCOMES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def next_id(prefix, items):
    """Generate next sequential ID."""
    nums = []
    for item in items:
        key = "id" if "id" in item else "pattern_id"
        val = item.get(key, "")
        if val.startswith(prefix):
            try:
                nums.append(int(val.split("-")[-1]))
            except ValueError:
                pass
    return f"{prefix}-{(max(nums) + 1) if nums else 1:03d}"


def is_duplicate(data, source, filename, check_name, date):
    """Check if this exact outcome already exists (same file+check+date)."""
    for o in data["outcomes"]:
        if (o.get("source") == source and
            o.get("file") == filename and
            o.get("check_name") == check_name and
            o.get("timestamp", "").startswith(date)):
            return True
    return False


def add_outcome(data, source, filename, check_name, detail):
    """Add a single outcome entry (with dedup)."""
    if is_duplicate(data, source, filename, check_name, DATE_STR):
        return False

    outcome = {
        "id": next_id("outcome", data["outcomes"]),
        "timestamp": TIME_STR,
        "source": source,
        "file": filename,
        "check_name": check_name,
        "detail": detail,
        "resolved": False
    }
    data["outcomes"].append(outcome)
    return True


def parse_content_audit(report_path):
    """Parse content-audit-auto.py markdown report for failures."""
    if not os.path.exists(report_path):
        print(f"Error: report not found: {report_path}")
        return []

    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    failures = []
    current_file = None

    for line in content.split("\n"):
        # Match failure headers: ### ⚠️ filename — X issue(s)
        header = re.match(r"^### ⚠️\s+(\S+\.html)\s+—", line)
        if header:
            current_file = header.group(1)
            continue

        # Match pass headers (reset current_file)
        if re.match(r"^### ✅", line):
            current_file = None
            continue

        # Match failure details: - **check_name:** detail
        if current_file:
            detail_match = re.match(r"^- \*\*(.+?):\*\*\s+(.+)$", line)
            if detail_match:
                check_name = detail_match.group(1).strip()
                detail = detail_match.group(2).strip()
                failures.append((current_file, check_name, detail))

    return failures


def parse_health_check(report_path):
    """Parse health-check-auto.py markdown report for failures."""
    if not os.path.exists(report_path):
        print(f"Error: report not found: {report_path}")
        return []

    with open(report_path, "r", encoding="utf-8") as f:
        content = f.read()

    failures = []

    for line in content.split("\n"):
        # Health check failures look like: - ⚠️ description or - ❌ description
        fail_match = re.match(r"^- [⚠️❌]\s*(.+)$", line)
        if fail_match:
            detail = fail_match.group(1).strip()
            # Extract check type from detail
            if "article count" in detail.lower():
                failures.append(("CLAUDE.md", "article count", detail))
            elif "stale" in detail.lower() or "STALE" in detail:
                failures.append(("workspace", "staleness", detail))
            elif "iframe" in detail.lower():
                failures.append(("site", "broken iframe", detail))
            elif "sitemap" in detail.lower():
                failures.append(("sitemap.xml", "sitemap", detail))
            elif "DEAD" in detail:
                failures.append(("workspace", "dead task", detail))
            else:
                failures.append(("workspace", "health", detail))

    return failures


def detect_patterns(data):
    """Scan outcomes for recurring patterns. 3+ = detect, 5+ = escalate."""
    # Group unresolved outcomes by check_name
    groups = {}
    for o in data["outcomes"]:
        if o.get("resolved"):
            continue
        key = o["check_name"]
        if key not in groups:
            groups[key] = []
        groups[key].append(o)

    new_patterns = 0
    updated_patterns = 0

    for check_name, outcomes in groups.items():
        # Get unique dates
        unique_dates = set(o["timestamp"][:10] for o in outcomes)
        if len(unique_dates) < 3:
            continue

        affected_files = sorted(set(o["file"] for o in outcomes))
        first_seen = min(o["timestamp"][:10] for o in outcomes)
        last_seen = max(o["timestamp"][:10] for o in outcomes)
        count = len(outcomes)

        # Check if pattern already exists
        existing = None
        for p in data["patterns"]:
            if p["check_name"] == check_name:
                existing = p
                break

        if existing:
            # Update existing pattern
            if existing["status"] not in ("rejected", "rule_activated"):
                existing["occurrences"] = count
                existing["last_seen"] = last_seen
                existing["affected_files"] = affected_files
                updated_patterns += 1
        else:
            # Create new pattern
            pattern = {
                "pattern_id": next_id("pattern", data["patterns"]),
                "check_name": check_name,
                "occurrences": count,
                "first_seen": first_seen,
                "last_seen": last_seen,
                "affected_files": affected_files,
                "status": "detected",
                "proposed_rule": None
            }
            data["patterns"].append(pattern)
            new_patterns += 1

    return new_patterns, updated_patterns


def fire_pattern_events(data):
    """Fire event-router for newly detected patterns."""
    router = os.path.join(SCRIPTS, "event-router.py")
    if not os.path.exists(router):
        print("Warning: event-router.py not found, skipping event dispatch")
        return

    for p in data["patterns"]:
        if p["status"] == "detected" and p["occurrences"] >= 3:
            priority = "high" if p["occurrences"] >= 5 else "normal"
            detail = f"{p['check_name']} failed {p['occurrences']} times across {', '.join(p['affected_files'])} (priority: {priority})"
            print(f"[FIRE] pattern_detected: {detail}")

            # Only fire if event-router supports pattern_detected
            try:
                import subprocess
                result = subprocess.run(
                    [sys.executable, router, "--event", "pattern_detected", "--detail", detail],
                    capture_output=True, text=True, cwd=BB
                )
                if result.returncode == 0:
                    print(f"  Event routed successfully")
                else:
                    # Event type not yet added — that's TASK-034
                    print(f"  Event routing skipped (pattern_detected not yet in router)")
            except Exception as e:
                print(f"  Event routing failed: {e}")


def print_stats(data):
    """Print current outcome/pattern summary."""
    print(f"\n{'='*50}")
    print(f"OUTCOME TRACKER — Stats")
    print(f"{'='*50}")
    print(f"Total outcomes:  {len(data['outcomes'])}")
    print(f"  Resolved:      {sum(1 for o in data['outcomes'] if o.get('resolved'))}")
    print(f"  Unresolved:    {sum(1 for o in data['outcomes'] if not o.get('resolved'))}")
    print(f"Total patterns:  {len(data['patterns'])}")
    print(f"  Detected:      {sum(1 for p in data['patterns'] if p['status'] == 'detected')}")
    print(f"  Proposed:      {sum(1 for p in data['patterns'] if p['status'] == 'proposed')}")
    print(f"  Approved:      {sum(1 for p in data['patterns'] if p['status'] == 'approved')}")
    print(f"  Rejected:      {sum(1 for p in data['patterns'] if p['status'] == 'rejected')}")
    print(f"  Activated:     {sum(1 for p in data['patterns'] if p['status'] == 'rule_activated')}")
    print(f"Last updated:    {data['stats'].get('last_updated', 'never')}")
    print(f"{'='*50}")

    if data["patterns"]:
        print(f"\nPatterns:")
        for p in data["patterns"]:
            status_icon = {"detected": "🔍", "proposed": "📝", "approved": "✅", "rejected": "❌", "rule_activated": "⚡"}.get(p["status"], "?")
            print(f"  {status_icon} {p['pattern_id']}: {p['check_name']} — {p['occurrences']}x — [{p['status']}]")
            print(f"     Files: {', '.join(p['affected_files'][:5])}")


def main():
    args = sys.argv[1:]

    # Parse CLI args
    source = None
    report = None
    check = None
    detail = None
    filename = None
    show_stats = "--stats" in args

    i = 0
    while i < len(args):
        if args[i] == "--source" and i + 1 < len(args):
            source = args[i + 1]; i += 2
        elif args[i] == "--report" and i + 1 < len(args):
            report = args[i + 1]; i += 2
        elif args[i] == "--check" and i + 1 < len(args):
            check = args[i + 1]; i += 2
        elif args[i] == "--detail" and i + 1 < len(args):
            detail = args[i + 1]; i += 2
        elif args[i] == "--file" and i + 1 < len(args):
            filename = args[i + 1]; i += 2
        else:
            i += 1

    data = load_outcomes()

    # Stats only
    if show_stats:
        print_stats(data)
        return

    if not source:
        print("Error: --source required (content-audit | health-check | manual)")
        print("  or use --stats to view current state")
        sys.exit(1)

    # Process based on source
    added = 0

    if source == "content-audit":
        if not report:
            print("Error: --report required for content-audit source")
            sys.exit(1)
        # Support glob-like path (find latest report)
        if "*" in report:
            import glob
            matches = sorted(glob.glob(os.path.join(BB, report) if not os.path.isabs(report) else report))
            if not matches:
                print(f"No files match: {report}")
                sys.exit(1)
            report = matches[-1]  # Latest
            print(f"Using latest report: {os.path.basename(report)}")

        report_path = report if os.path.isabs(report) else os.path.join(BB, report)
        failures = parse_content_audit(report_path)
        print(f"Parsed {len(failures)} failure(s) from content audit")
        for fname, check_name, det in failures:
            if add_outcome(data, source, fname, check_name, det):
                added += 1
                print(f"  + {fname}: {check_name}")
            else:
                print(f"  = {fname}: {check_name} (already tracked)")

    elif source == "health-check":
        if not report:
            print("Error: --report required for health-check source")
            sys.exit(1)
        if "*" in report:
            import glob
            matches = sorted(glob.glob(os.path.join(BB, report) if not os.path.isabs(report) else report))
            if not matches:
                print(f"No files match: {report}")
                sys.exit(1)
            report = matches[-1]
            print(f"Using latest report: {os.path.basename(report)}")

        report_path = report if os.path.isabs(report) else os.path.join(BB, report)
        failures = parse_health_check(report_path)
        print(f"Parsed {len(failures)} failure(s) from health check")
        for fname, check_name, det in failures:
            if add_outcome(data, source, fname, check_name, det):
                added += 1
                print(f"  + {fname}: {check_name}")
            else:
                print(f"  = {fname}: {check_name} (already tracked)")

    elif source == "manual":
        if not check or not detail:
            print("Error: --check and --detail required for manual source")
            sys.exit(1)
        fname = filename or "unknown"
        if add_outcome(data, source, fname, check, detail):
            added += 1
            print(f"  + {fname}: {check}")
        else:
            print(f"  = {fname}: {check} (already tracked)")

    else:
        print(f"Error: unknown source '{source}' (use content-audit | health-check | manual)")
        sys.exit(1)

    print(f"\n{added} new outcome(s) added")

    # Detect patterns
    new_p, updated_p = detect_patterns(data)
    if new_p or updated_p:
        print(f"Patterns: {new_p} new, {updated_p} updated")
        fire_pattern_events(data)

    # Save
    save_outcomes(data)
    print(f"Saved to {OUTCOMES_FILE}")

    # Print stats
    print_stats(data)


if __name__ == "__main__":
    main()
