#!/usr/bin/env bash
# ============================================================
# SITE VALIDATOR — Run before every git push (R-035 enforcement)
# Catches the structural drift that breaks the site on deploy.
#
# Usage: bash scripts/validate-site.sh
# Exit 0 = safe to push. Exit 1 = fix issues first.
# ============================================================
set -uo pipefail

SITE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
ERRORS=0
WARNINGS=0

red()    { echo -e "\033[0;31m$1\033[0m"; }
yellow() { echo -e "\033[0;33m$1\033[0m"; }
green()  { echo -e "\033[0;32m$1\033[0m"; }

error()   { ERRORS=$((ERRORS + 1)); red "  ERROR: $1"; }
warn()    { WARNINGS=$((WARNINGS + 1)); yellow "  WARN:  $1"; }
ok()      { green "  OK:    $1"; }

echo "=========================================="
echo "  Bionic Banker Site Validator"
echo "=========================================="
echo ""

# Exclude non-article pages from article-specific checks
SKIP_PAGES="index.html|articles.html|dashboard.html|preview-layout.html|dashboard.astro|intelligence.html|agent-architecture.html|ai.html|system-pulse.html"

# ============================================================
# CHECK 1: styles.css version consistency
# ============================================================
echo "--- CHECK 1: styles.css version ---"
VERSIONS=$(grep -oh 'styles\.css?v=[0-9]*' "$SITE_DIR"/*.html 2>/dev/null | sort -u)
VERSION_COUNT=$(echo "$VERSIONS" | wc -l)

if [ "$VERSION_COUNT" -gt 1 ]; then
    error "Multiple styles.css versions found:"
    grep -l 'styles\.css' "$SITE_DIR"/*.html | while read f; do
        ver=$(grep -oh 'styles\.css?v=[0-9]*' "$f" | head -1)
        echo "         $(basename $f): ${ver:-no version}"
    done | sort -t: -k2 | uniq -c -f1 | head -5
else
    ok "All pages use same styles.css version: $VERSIONS"
fi

# Pages missing styles.css entirely
NO_CSS=$(grep -rL 'styles\.css' "$SITE_DIR"/*.html 2>/dev/null | xargs -I{} basename {} | grep -vE "$SKIP_PAGES" || true)
if [ -n "$NO_CSS" ]; then
    error "Pages missing styles.css: $NO_CSS"
fi

# ============================================================
# CHECK 2: Navigation consistency
# ============================================================
echo "--- CHECK 2: Navigation ---"
NAV_JS_COUNT=$(grep -rl 'nav\.js' "$SITE_DIR"/*.html 2>/dev/null | wc -l)
INLINE_NAV=$(grep -rl '<nav' "$SITE_DIR"/*.html 2>/dev/null | xargs -I{} basename {} | while read f; do
    if ! grep -q 'nav\.js' "$SITE_DIR/$f" 2>/dev/null; then echo "$f"; fi
done)
TOTAL_HTML=$(ls "$SITE_DIR"/*.html 2>/dev/null | wc -l)

if [ -n "$INLINE_NAV" ]; then
    warn "Pages with inline nav (not using nav.js): $INLINE_NAV"
fi
ok "$NAV_JS_COUNT / $TOTAL_HTML pages load nav.js"

# ============================================================
# CHECK 3: Required meta tags on article pages
# ============================================================
echo "--- CHECK 3: Meta tags (articles only) ---"
for f in "$SITE_DIR"/*.html; do
    name=$(basename "$f")
    echo "$name" | grep -qE "$SKIP_PAGES" && continue

    # GA tracking
    grep -q "G-YS428H3H44" "$f" || warn "$name missing Google Analytics"

    # OG tags
    grep -q 'og:title' "$f" || warn "$name missing og:title"

    # Twitter card
    grep -q 'twitter:card' "$f" || warn "$name missing twitter:card"

    # Canonical URL
    grep -q 'rel="canonical"' "$f" || warn "$name missing canonical URL"

    # Viewport
    grep -q 'viewport' "$f" || error "$name missing viewport meta (mobile broken)"

    # Charset
    grep -qi 'charset' "$f" || error "$name missing charset declaration"
done
ok "Meta tag check complete"

# ============================================================
# CHECK 4: Font loading
# ============================================================
echo "--- CHECK 4: Fonts ---"
NO_FONTS=$(grep -rL 'Bricolage' "$SITE_DIR"/*.html 2>/dev/null | xargs -I{} basename {} | grep -vE "$SKIP_PAGES" || true)
if [ -n "$NO_FONTS" ]; then
    warn "Pages missing Bricolage font: $NO_FONTS"
fi

# ============================================================
# CHECK 5: Footer consistency
# ============================================================
echo "--- CHECK 5: Footer ---"
NO_FOOTER=$(grep -rL '<footer' "$SITE_DIR"/*.html 2>/dev/null | xargs -I{} basename {} | grep -vE "$SKIP_PAGES" || true)
if [ -n "$NO_FOOTER" ]; then
    warn "Pages missing footer: $NO_FOOTER"
fi

# ============================================================
# CHECK 6: Iframe sources exist
# ============================================================
echo "--- CHECK 6: Iframe sources ---"
IFRAME_SRCS=$(grep -roh 'src="blog-visuals/[^"]*"' "$SITE_DIR"/*.html 2>/dev/null | sort -u)
while IFS= read -r src; do
    [ -z "$src" ] && continue
    path=$(echo "$src" | sed 's/src="//;s/"//')
    if [ ! -f "$SITE_DIR/$path" ]; then
        error "Iframe source missing: $path"
    fi
done <<< "$IFRAME_SRCS"
ok "Iframe source check complete"

# ============================================================
# CHECK 7: Article count in articles.html
# ============================================================
echo "--- CHECK 7: Article count ---"
DECLARED_COUNT=$(grep -o '[0-9]* pieces' "$SITE_DIR/articles.html" 2>/dev/null | grep -o '[0-9]*')
CARD_COUNT=$(grep -c 'class="article-card"' "$SITE_DIR/articles.html" 2>/dev/null || echo 0)
if [ "$DECLARED_COUNT" != "$CARD_COUNT" ]; then
    error "articles.html says '$DECLARED_COUNT pieces' but has $CARD_COUNT article cards"
else
    ok "Article count matches: $DECLARED_COUNT"
fi

# ============================================================
# CHECK 8: Dead references
# ============================================================
echo "--- CHECK 8: Dead references ---"
DEAD_PATTERNS="100\.94\.167\.23|vic1hash@|clode.code|hash02-workspace"
DEAD_FOUND=$(grep -rl "$DEAD_PATTERNS" "$SITE_DIR"/*.html 2>/dev/null | xargs -I{} basename {} || true)
if [ -n "$DEAD_FOUND" ]; then
    error "Pages contain dead references (old IPs/paths): $DEAD_FOUND"
fi

# ============================================================
# RESULTS
# ============================================================
echo ""
echo "=========================================="
if [ "$ERRORS" -gt 0 ]; then
    red "  FAILED: $ERRORS errors, $WARNINGS warnings"
    red "  Fix errors before pushing!"
    exit 1
elif [ "$WARNINGS" -gt 0 ]; then
    yellow "  PASSED with $WARNINGS warnings"
    echo "  Safe to push, but consider fixing warnings."
    exit 0
else
    green "  PASSED: All checks clean!"
    exit 0
fi
