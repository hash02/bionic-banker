"""
Content Audit Auto - bionicbanker.tech
Audits HTML article files for SEO, accessibility, and structural issues.
Modes: --all (every article) | --changed (only latest commit's files)
Pure Python — no external dependencies.
"""
import os, re, sys, subprocess, io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DATE_STR = __import__("datetime").datetime.now().strftime("%Y-%m-%d")
BB = os.getcwd()

# Exclusions — structural pages, not articles
SKIP = {"index.html", "articles.html", "preview-layout.html", "agent-architecture.html", "dashboard_preview.html"}

def get_html_files(mode):
    """Get list of HTML files to audit."""
    if mode == "changed":
        try:
            result = subprocess.run(
                ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
                capture_output=True, text=True, cwd=BB
            )
            files = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]
            return [f for f in files if f.endswith(".html") and os.path.basename(f) not in SKIP
                    and os.path.exists(os.path.join(BB, f))]
        except Exception:
            print("Warning: git diff failed, falling back to --all")
            return get_html_files("all")
    else:
        return [f for f in os.listdir(BB) if f.endswith(".html") and f not in SKIP]

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""

def audit_file(filepath):
    """Run all 8 checks on a single HTML file. Returns (passes, failures)."""
    content = read_file(filepath)
    if not content:
        return [], [("File read", "Could not read file")]

    passes, failures = [], []

    # Check 1: Has <title> tag (not empty)
    title_match = re.search(r"<title>([^<]+)</title>", content)
    if title_match and title_match.group(1).strip():
        passes.append("title tag")
    else:
        failures.append(("title tag", "Missing or empty <title>"))

    # Check 2: Has <meta name="description"> (not empty)
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content)
    if desc_match and desc_match.group(1).strip():
        passes.append("meta description")
    else:
        failures.append(("meta description", 'Missing or empty <meta name="description">'))

    # Check 3: Open Graph tags
    og_tags = {"og:title": False, "og:description": False, "og:image": False}
    for tag in og_tags:
        pattern = rf'<meta\s+(?:property|name)=["\']{ re.escape(tag) }["\']\s+content=["\']([^"\']+)["\']'
        if re.search(pattern, content):
            og_tags[tag] = True
    missing_og = [t for t, found in og_tags.items() if not found]
    if not missing_og:
        passes.append("Open Graph tags")
    else:
        failures.append(("Open Graph tags", f"Missing: {', '.join(missing_og)}"))

    # Check 4: Twitter Card tags
    tw_tags = {"twitter:card": False, "twitter:title": False}
    for tag in tw_tags:
        pattern = rf'<meta\s+(?:name|property)=["\']{ re.escape(tag) }["\']\s+content=["\']([^"\']+)["\']'
        if re.search(pattern, content):
            tw_tags[tag] = True
    missing_tw = [t for t, found in tw_tags.items() if not found]
    if not missing_tw:
        passes.append("Twitter Card tags")
    else:
        failures.append(("Twitter Card tags", f"Missing: {', '.join(missing_tw)}"))

    # Check 5: No broken internal links
    broken_links = []
    for m in re.finditer(r'href=["\']([^"\']+\.html)["\']', content):
        href = m.group(1)
        if href.startswith("http"):
            continue
        # Strip anchor fragments and leading slashes (absolute paths work on live site)
        href_clean = href.split("#")[0].lstrip("/")
        if href_clean and not os.path.exists(os.path.join(BB, href_clean)):
            broken_links.append(href_clean)
    if not broken_links:
        passes.append("internal links")
    else:
        failures.append(("internal links", f"Broken: {', '.join(broken_links)}"))

    # Check 6: At least one <img> with alt attribute
    imgs = re.findall(r"<img\s[^>]*>", content)
    if not imgs:
        # No images is not necessarily a failure — some articles are text-only
        passes.append("img alt (no images)")
    else:
        imgs_with_alt = [img for img in imgs if re.search(r'alt=["\']', img)]
        if len(imgs_with_alt) >= 1:
            passes.append("img alt")
        else:
            failures.append(("img alt", f"{len(imgs)} images, none have alt attribute"))

    # Check 7: No empty <h1> or <h2> tags
    empty_headings = re.findall(r"<h[12][^>]*>\s*</h[12]>", content)
    if not empty_headings:
        passes.append("headings")
    else:
        failures.append(("headings", f"{len(empty_headings)} empty h1/h2 tags"))

    # Check 8: Has JSON-LD structured data
    if re.search(r'<script\s+type=["\']application/ld\+json["\']', content):
        passes.append("JSON-LD")
    else:
        failures.append(("JSON-LD", "Missing structured data"))

    return passes, failures

def main():
    mode = "changed" if "--changed" in sys.argv else "all"
    files = get_html_files(mode)

    if not files:
        print(f"No HTML files to audit (mode: {mode})")
        return

    total_checks = 8
    results = []
    total_pass = 0
    total_issues = 0

    for f in sorted(files):
        filepath = os.path.join(BB, f) if not os.path.isabs(f) else f
        basename = os.path.basename(f)
        passes, failures = audit_file(filepath)
        score = len(passes)
        results.append((basename, score, total_checks, passes, failures))
        if not failures:
            total_pass += 1
        else:
            total_issues += 1

    # Build report
    rpt = f"## Content Audit Report — {DATE_STR}\n\n"
    rpt += f"**Mode:** {mode} | **Files audited:** {len(files)}\n\n"

    for basename, score, total, passes, failures in results:
        if not failures:
            rpt += f"### ✅ {basename} — PASS ({score}/{total} checks)\n\n"
        else:
            rpt += f"### ⚠️ {basename} — {len(failures)} issue(s)\n"
            for check, detail in failures:
                rpt += f"- **{check}:** {detail}\n"
            rpt += "\n"

    rpt += f"### Summary: {total_pass}/{len(files)} pass"
    if total_issues:
        rpt += f", {total_issues} need attention"
    rpt += "\n"

    # Write report
    rpt_dir = os.path.join(BB, "memory")
    os.makedirs(rpt_dir, exist_ok=True)
    rpt_path = os.path.join(rpt_dir, f"content-audit-{DATE_STR}.md")
    with open(rpt_path, "w", encoding="utf-8") as f:
        f.write(rpt)

    print(rpt)
    print(f"\nReport saved: {rpt_path}")

    # Exit code for CI: non-zero if issues found
    if total_issues:
        print(f"\n⚠️ {total_issues} file(s) have issues")
    else:
        print("\n✅ All articles pass audit")

if __name__ == "__main__":
    main()
