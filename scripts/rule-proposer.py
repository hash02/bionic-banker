"""
Rule Proposer - bionicbanker.tech
Reads outcome-tracker patterns, generates rule proposals for HASH to approve.
Part of Level 5 Adaptive agent infrastructure.

Usage:
  python scripts/rule-proposer.py              # Process all detected patterns → generate proposals
  python scripts/rule-proposer.py --check      # Check for HASH's approval decisions
  python scripts/rule-proposer.py --status     # Print current proposals and statuses
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
PROPOSALS_FILE = os.path.join(MEMORY, "proposals.md")
SCRIPTS = os.path.join(BB, "scripts")


# Known pattern → proposal mappings
RULE_TEMPLATES = {
    "headings": {
        "title": "Auto-remove empty heading tags",
        "fix": "Add auto-fix to content-audit-auto.py that detects and removes empty <h1></h1> and <h2></h2> tags (WordPress migration artifacts with no content).",
        "risk": "Low — empty headings have no visible content, removing them improves SEO and accessibility.",
        "target": "content-audit-auto.py"
    },
    "meta description": {
        "title": "Auto-generate missing meta descriptions",
        "fix": "Add script to extract first 155 characters of article body text and inject as <meta name=\"description\"> for articles missing it.",
        "risk": "Low — auto-generated descriptions are better than no description. Can be manually refined later.",
        "target": "seo-inject.py"
    },
    "img alt": {
        "title": "Flag images without alt text for manual review",
        "fix": "Add auto-fix that generates placeholder alt text from image filename/context and injects it. Flag for HASH's review in proposals.md.",
        "risk": "Medium — auto-generated alt text may not be accurate. Better than empty alt, but needs human review.",
        "target": "content-audit-auto.py"
    },
    "internal links": {
        "title": "Auto-detect renamed files and suggest updated links",
        "fix": "Cross-reference broken href targets with current file list using fuzzy matching. If a close match exists (e.g., 'defi-guide.html' → 'defi.html'), propose the updated link.",
        "risk": "Low — suggestions only, no auto-replacement without approval.",
        "target": "content-audit-auto.py"
    },
    "JSON-LD": {
        "title": "Auto-inject JSON-LD using seo-inject.py",
        "fix": "Run seo-inject.py on articles missing JSON-LD structured data. This logic already exists — just needs to be triggered automatically on detection.",
        "risk": "Low — seo-inject.py is battle-tested (ran on all 16 articles in Batch 5).",
        "target": "seo-inject.py"
    },
    "Open Graph tags": {
        "title": "Auto-inject missing OG tags",
        "fix": "Extend seo-inject.py to add missing og:title and og:description from existing <title> and <meta description> tags.",
        "risk": "Low — data already exists in the HTML, just needs OG tag wrappers.",
        "target": "seo-inject.py"
    },
    "Twitter Card tags": {
        "title": "Auto-inject missing Twitter Card tags",
        "fix": "Extend seo-inject.py to add twitter:card (summary_large_image) and twitter:title from existing metadata.",
        "risk": "Low — same pattern as OG tag injection.",
        "target": "seo-inject.py"
    },
    "article count": {
        "title": "Auto-sync article count in CLAUDE.md",
        "fix": "Health check already self-heals this. Propose making it a permanent pre-push check so the count never drifts.",
        "risk": "Low — health-check-auto.py already does this in repo mode.",
        "target": "health-check-auto.py"
    },
    "staleness": {
        "title": "Auto-flag stale tasks for archival",
        "fix": "When a task stays STALE (>7d) for 3+ consecutive health checks, auto-move it to a 'Stale Archive' section in TASKS.md instead of repeatedly flagging it.",
        "risk": "Medium — could archive tasks HASH still intends to do. Requires approval per task.",
        "target": "health-check-auto.py"
    },
}


def load_outcomes():
    if os.path.exists(OUTCOMES_FILE):
        with open(OUTCOMES_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Error: outcomes.json corrupted")
                sys.exit(1)
    else:
        print("Error: outcomes.json not found. Run outcome-tracker.py first.")
        sys.exit(1)


def save_outcomes(data):
    data["stats"]["last_updated"] = TIME_STR
    with open(OUTCOMES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_proposals():
    """Load proposals.md content."""
    if os.path.exists(PROPOSALS_FILE):
        with open(PROPOSALS_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def next_rule_num(proposals_content):
    """Find the next RULE-XXX number."""
    nums = [int(m) for m in re.findall(r"RULE-(\d+)", proposals_content)]
    return max(nums) + 1 if nums else 1


def generate_proposal(pattern, rule_num):
    """Generate a proposal markdown block for a pattern."""
    check = pattern["check_name"]
    template = RULE_TEMPLATES.get(check, None)

    if template:
        title = template["title"]
        fix = template["fix"]
        risk = template["risk"]
        tgt = template["target"]
    else:
        title = f"Investigate recurring {check} failures"
        fix = f"The '{check}' check has failed {pattern['occurrences']} times across {', '.join(pattern['affected_files'])}. Investigate root cause and propose a targeted fix."
        risk = "Unknown — needs investigation before implementation."
        tgt = "content-audit-auto.py"

    proposal = f"""
## RULE-{rule_num:03d} — [PENDING]
**Pattern:** {check} check failed {pattern['occurrences']} times ({pattern['first_seen']} to {pattern['last_seen']})
**Affected files:** {', '.join(pattern['affected_files'])}
**Proposed fix:** {title} — {fix}
**Risk:** {risk}
**Target script:** {tgt}

**To approve:** Change [PENDING] to [APPROVED] above
**To reject:** Change [PENDING] to [REJECTED] and optionally add a reason below

---
"""
    return proposal, tgt


def process_patterns(data):
    """Generate proposals for detected patterns that haven't been proposed yet."""
    proposals_content = load_proposals()

    # Initialize proposals.md if it doesn't exist
    if not proposals_content:
        proposals_content = "# Rule Proposals — L5 Adaptive\n\n> HASH marks proposals [APPROVED] or [REJECTED] inline.\n\n---\n"

    new_proposals = 0
    rule_num = next_rule_num(proposals_content)

    for pattern in data["patterns"]:
        if pattern["status"] != "detected":
            continue

        proposal_text, target = generate_proposal(pattern, rule_num)
        proposals_content += proposal_text

        # Update pattern status
        pattern["status"] = "proposed"
        pattern["proposed_rule"] = f"RULE-{rule_num:03d}"

        # Fire event
        fire_event("rule_proposed",
                   f"RULE-{rule_num:03d}: {RULE_TEMPLATES.get(pattern['check_name'], {}).get('title', pattern['check_name'])}",
                   target)

        print(f"  📝 RULE-{rule_num:03d}: {pattern['check_name']} → proposal generated")
        rule_num += 1
        new_proposals += 1

    if new_proposals:
        with open(PROPOSALS_FILE, "w", encoding="utf-8") as f:
            f.write(proposals_content)
        print(f"\n{new_proposals} new proposal(s) written to {PROPOSALS_FILE}")
    else:
        print("No new patterns to propose rules for.")

    return new_proposals


def check_approvals(data):
    """Check proposals.md for HASH's [APPROVED]/[REJECTED] decisions."""
    proposals_content = load_proposals()
    if not proposals_content:
        print("No proposals.md found.")
        return 0

    changes = 0

    for pattern in data["patterns"]:
        if pattern["status"] != "proposed":
            continue

        rule_id = pattern.get("proposed_rule")
        if not rule_id:
            continue

        # Check if HASH has marked it
        approved = re.search(rf"## {re.escape(rule_id)} — \[APPROVED\]", proposals_content)
        rejected = re.search(rf"## {re.escape(rule_id)} — \[REJECTED\]", proposals_content)

        if approved:
            pattern["status"] = "approved"
            print(f"  ✅ {rule_id} ({pattern['check_name']}): APPROVED by HASH")
            fire_event("rule_activated",
                       f"{rule_id}: {pattern['check_name']} — approved, ready for implementation",
                       RULE_TEMPLATES.get(pattern["check_name"], {}).get("target", "unknown"))
            changes += 1
        elif rejected:
            pattern["status"] = "rejected"
            print(f"  ❌ {rule_id} ({pattern['check_name']}): REJECTED by HASH")
            changes += 1

    if changes:
        print(f"\n{changes} approval decision(s) processed")
    else:
        print("No new approval decisions found in proposals.md")

    return changes


def fire_event(event_type, detail_text, target_text=None):
    """Fire event through event-router.py."""
    router = os.path.join(SCRIPTS, "event-router.py")
    if not os.path.exists(router):
        print(f"  Warning: event-router.py not found")
        return

    import subprocess
    cmd = [sys.executable, router, "--event", event_type, "--detail", detail_text]
    if target_text:
        cmd.extend(["--target", target_text])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=BB)
        if result.returncode != 0:
            print(f"  Warning: event routing returned non-zero")
    except Exception as e:
        print(f"  Warning: event routing failed: {e}")


def print_status(data):
    """Print current proposal statuses."""
    proposals_content = load_proposals()

    print(f"\n{'='*50}")
    print(f"RULE PROPOSER — Status")
    print(f"{'='*50}")

    if not data["patterns"]:
        print("No patterns detected yet.")
        print(f"{'='*50}")
        return

    for p in data["patterns"]:
        status_icon = {
            "detected": "🔍 Awaiting proposal",
            "proposed": "📝 Awaiting HASH review",
            "approved": "✅ Approved — ready to implement",
            "rejected": "❌ Rejected",
            "rule_activated": "⚡ Active rule"
        }.get(p["status"], "? Unknown")

        rule_id = p.get("proposed_rule", "—")
        print(f"\n  {rule_id}: {p['check_name']}")
        print(f"    Status: {status_icon}")
        print(f"    Occurrences: {p['occurrences']}x ({p['first_seen']} → {p['last_seen']})")
        print(f"    Files: {', '.join(p['affected_files'][:5])}")

    print(f"\n{'='*50}")


def main():
    args = sys.argv[1:]
    mode_check = "--check" in args
    mode_status = "--status" in args

    data = load_outcomes()

    if mode_status:
        print_status(data)
        return

    if mode_check:
        print("Checking for HASH's approval decisions...")
        changes = check_approvals(data)
        save_outcomes(data)
        return

    # Default: process detected patterns → generate proposals
    print("Processing detected patterns...")
    new = process_patterns(data)
    save_outcomes(data)
    print_status(data)


if __name__ == "__main__":
    main()
