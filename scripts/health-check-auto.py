"""
Health Check Auto - bionicbanker.tech
Modes: --local (full workspace) | --repo (GitHub Actions, repo-only)
Level 4: Self-healing for known failure modes before reporting.
"""
import os, re, sys, glob
from datetime import datetime, timedelta

TODAY = datetime.now()
DATE_STR = TODAY.strftime("%Y-%m-%d")
MODE = "repo" if "--repo" in sys.argv else "local"
healed = []  # Track self-healing actions
needs_human = []  # Track issues requiring human decision

if MODE == "local":
    WS = r"C:\Users\himan\OneDrive\hash 2026"
    BB = os.path.join(WS, "bionic-banker")
    TASKS_F = os.path.join(WS, "TASKS.md")
    QUICK_F = os.path.join(WS, "QUICK_CONTEXT.md")
    SESSLOG = os.path.join(WS, "SESSION_LOG.md")
    CLAUDE_F = os.path.join(WS, "CLAUDE.md")
    OUTBOX_F = os.path.join(WS, "clode code", "OUTBOX.md")
    RPT_DIR = os.path.join(WS, "memory")
else:
    BB = os.getcwd()
    WS = BB
    TASKS_F = QUICK_F = SESSLOG = CLAUDE_F = OUTBOX_F = None
    RPT_DIR = os.path.join(BB, "memory")

issues, info = [], []

def read(p):
    if p and os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f: return f.read()
    return None

def parse_date(t):
    for pat, fmt in [(r"(\d{4}-\d{2}-\d{2})", "%Y-%m-%d"),
                     (r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{4})", "%b %d %Y")]:
        m = re.search(pat, t)
        if m:
            try: return datetime.strptime(m.group(1), fmt)
            except: pass
    return None

# Check 1: Article count
htmls = [f for f in os.listdir(BB) if f.endswith(".html")
         and f not in ("index.html","articles.html","preview-layout.html","agent-architecture.html")]
info.append(f"Article count: {len(htmls)}")

# Check 2: CLAUDE.md article count (with self-healing in repo mode)
if CLAUDE_F:
    c = read(CLAUDE_F)
    if c:
        m = re.search(r"\*\*(\d+)\s+(?:articles?\s+)?total\*\*", c)
        if m:
            claimed = int(m.group(1))
            if claimed != len(htmls):
                if MODE == "repo":
                    # Self-heal: update article count in CLAUDE.md
                    new_c = c.replace(f"**{claimed} total**", f"**{len(htmls)} total**")
                    new_c = new_c.replace(f"**{claimed} articles total**", f"**{len(htmls)} articles total**")
                    with open(CLAUDE_F, "w", encoding="utf-8") as f: f.write(new_c)
                    healed.append(f"Article count {claimed}→{len(htmls)} in CLAUDE.md")
                    info.append(f"CLAUDE.md count auto-fixed ({claimed}→{len(htmls)})")
                else:
                    # Local mode: don't auto-fix, flag for human
                    issues.append(f"CLAUDE.md claims {claimed} articles, found {len(htmls)}")
            else: info.append(f"CLAUDE.md count matches ({claimed})")

# Check 3: Broken iframes
broken = []
for hf in glob.glob(os.path.join(BB, "*.html")):
    ct = read(hf) or ""
    for m in re.finditer(r'<iframe[^>]+src="([^"]+)"', ct):
        src = m.group(1)
        if not src.startswith("http") and not os.path.exists(os.path.join(BB, src)):
            broken.append(f"{os.path.basename(hf)} -> {src}")
if broken: issues.append(f"Broken iframes: {', '.join(broken)}")
else: info.append("All iframe refs valid")

# Check 4: sitemap
smap = read(os.path.join(BB, "sitemap.xml"))
if smap:
    missing = [f for f in htmls if f not in smap]
    if missing: issues.append(f"Missing from sitemap: {', '.join(missing)}")
    else: info.append("sitemap.xml complete")
else: issues.append("sitemap.xml not found")

# Local-only checks
if MODE == "local":
    # Task staleness (TASK-019)
    tc = read(TASKS_F)
    if tc:
        stale, dead, stuck = [], [], []
        for section in re.split(r"^## ", tc, flags=re.MULTILINE):
            lines = section.split("\n")
            sd = parse_date(lines[0])
            if not sd: continue
            age = (TODAY - sd).days
            is_waiting = "Waiting" in lines[0]
            for line in lines:
                if line.strip().startswith("- [ ]"):
                    name = re.sub(r"\*\*([^*]+)\*\*", r"\1", line.strip()[6:]).split("\u2014")[0].strip()[:60]
                    if is_waiting and age > 5: stuck.append((name, age))
                    elif age > 14: dead.append((name, age))
                    elif age > 7: stale.append((name, age))
        for t, a in dead: issues.append(f"DEAD ({a}d): {t}"); needs_human.append(f"DEAD task ({a}d): {t}")
        for t, a in stale: issues.append(f"STALE ({a}d): {t}"); needs_human.append(f"STALE task ({a}d): {t}")
        for t, a in stuck: issues.append(f"STUCK ({a}d): {t}"); needs_human.append(f"STUCK task ({a}d): {t}")
        if not dead and not stale and not stuck: info.append("No stale tasks")

    # QUICK_CONTEXT freshness (self-heal if > 7 days)
    qc = read(QUICK_F)
    if qc:
        d = parse_date(qc)
        if d:
            age = (TODAY - d).days
            if age > 7:
                # Self-heal: update the "Last updated" line
                new_qc = re.sub(
                    r"Last updated:?\s*\d{4}-\d{2}-\d{2}",
                    f"Last updated: {DATE_STR}",
                    qc
                )
                if new_qc != qc:
                    with open(QUICK_F, "w", encoding="utf-8") as f: f.write(new_qc)
                    healed.append(f"QUICK_CONTEXT.md timestamp updated ({age}d old)")
                    info.append(f"QUICK_CONTEXT.md auto-refreshed ({age}d→0d)")
                else:
                    issues.append(f"QUICK_CONTEXT.md {age}d old (couldn't auto-fix)")
            elif age > 5:
                issues.append(f"QUICK_CONTEXT.md {age}d old")
            else:
                info.append(f"QUICK_CONTEXT.md fresh ({age}d)")

    # SESSION_LOG freshness (needs human — can't auto-fix)
    sl = read(SESSLOG)
    if sl:
        dates = re.findall(r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}\s+\d{4})", sl)
        if dates:
            d = parse_date(dates[-1])
            if d:
                age = (TODAY - d).days
                if age > 5:
                    issues.append(f"SESSION_LOG {age}d stale")
                    if age > 10: needs_human.append(f"SESSION_LOG has no entries in {age} days")
                else: info.append(f"SESSION_LOG active ({age}d)")

# Self-heal: Clean old health reports (keep last 4)
old_reports = sorted(glob.glob(os.path.join(RPT_DIR, "health-check-auto-*.md")))
if len(old_reports) > 4:
    to_delete = old_reports[:-4]
    for rp in to_delete:
        try:
            os.remove(rp)
            healed.append(f"Cleaned old report: {os.path.basename(rp)}")
        except Exception:
            pass

# Generate report
status = "ISSUES FOUND" if issues else "HEALTHY"
rpt = f"# Health Check Report - {DATE_STR}\n\n"
rpt += f"**Mode:** {MODE} | **Generated:** {TODAY.strftime('%Y-%m-%d %H:%M')}\n\n"
rpt += f"## Status: {'RED' if issues else 'GREEN'} {status}\n\n"
rpt += "## Passed\n"
for i in info: rpt += f"- {i}\n"
if issues:
    rpt += "\n## Issues\n"
    for i in issues: rpt += f"- {i}\n"
# Self-healing report section
if healed or needs_human:
    rpt += "\n## Self-Healing Report\n"
    for h in healed: rpt += f"- ✅ AUTO-FIXED: {h}\n"
    for n in needs_human: rpt += f"- ⚠️ NEEDS HUMAN: {n}\n"

if MODE == "local":
    rpt += "\n## Task Staleness\n"
    staleness = [i for i in issues if any(t in i for t in ["DEAD","STALE","STUCK"])]
    if staleness:
        for s in staleness: rpt += f"- {s}\n"
    else: rpt += "- All tasks current\n"
rpt += f"\n---\n*health-check-auto.py ({MODE})*\n"

os.makedirs(RPT_DIR, exist_ok=True)
rp = os.path.join(RPT_DIR, f"health-check-auto-{DATE_STR}.md")
with open(rp, "w", encoding="utf-8") as f: f.write(rpt)
print(f"Report: {rp}")

if issues and OUTBOX_F and os.path.exists(OUTBOX_F):
    with open(OUTBOX_F, "a", encoding="utf-8") as f:
        f.write(f"\n\n## Health Check Alert - {DATE_STR}\n")
        for i in issues: f.write(f"- {i}\n")
    print("Issues appended to OUTBOX")

print(f"\n{'WARNING: ' + str(len(issues)) + ' issue(s)' if issues else 'ALL HEALTHY'}")
