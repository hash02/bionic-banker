#!/usr/bin/env python3
"""
verify_twofile.py — R-039 enforcement for bionic-banker.

WHY this exists:
    bionicbanker.tech is served by Cloudflare Pages git-integration.
    CF Pages serves the committed `dist/` at repo root AS-IS. It does NOT
    rebuild Astro on push. That means any content fix is TWO files:

        1. Source:  _astro-source/src/pages/<name>.astro
                    _astro-source/src/content/blog/<slug>.md
                    _astro-source/public/dashboard-data/<file>.json
        2. Built:   <name>/index.html
                    blog/<slug>/index.html
                    dashboard-data/<file>.json

    Source alone = regression bait (next Dell rebuild overwrites).
    Built alone = reaches prod, but next rebuild regresses.
    Both = permanent fix.

WHAT this script does:
    Takes a base ref (default: origin/main) and HEAD, diffs the files
    changed, and for each changed file in a source or built location,
    asserts the paired file was also changed. Reports mismatches.

    Exit codes:
        0 = clean, all source↔built pairs balanced (or N/A)
        1 = mismatch found, human review needed
        2 = internal error

USAGE:
    # local pre-push check
    python tools/verify_twofile.py

    # CI: check a PR branch against main
    python tools/verify_twofile.py --base origin/main --head HEAD

    # explicit file list (useful for GitHub Actions)
    python tools/verify_twofile.py --files file1 file2 ...

    # allow mismatch without exit 1 (warn-only mode)
    python tools/verify_twofile.py --warn-only

EXEMPTIONS (no pair required):
    - Pure CSS/SCSS edits in source (style-only, no content)
    - Astro component files (_astro-source/src/components/**)
    - Astro layouts (_astro-source/src/layouts/**)
    - Astro config / astro.config.mjs
    - Scripts under tools/ or blog-visuals/ (infographic sources)
    - README.md, LICENSE, .gitignore, package.json, etc.
    - Assets under _astro-source/public/ (copied as-is by Astro)
    - Content under _astro-source/src/content/ schema/config files
    - Widget HTML pages under widgets/ (hand-authored, no Astro source)
    - TV dashboard under tv/ (hand-authored)
    - .github/workflows/** (this file's own home)

R-039 reference: CLAUDE.md + MISTAKES.md (§M-039, Apr 17 2026).
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable


# ---------------------------------------------------------------------------
# Path mapping rules — source path → expected built path (and vice versa)
# ---------------------------------------------------------------------------

# A mapping rule: (regex to match a source file, function producing built path)
# Each rule is checked in order; first match wins.

SRC_TO_BUILT_RULES: list[tuple[re.Pattern, callable]] = [
    # Astro pages: _astro-source/src/pages/<slug>.astro -> <slug>/index.html
    # Special case: index.astro -> index.html (root)
    (
        re.compile(r"^_astro-source/src/pages/(?P<slug>[^/]+)\.astro$"),
        lambda m: "index.html" if m["slug"] == "index" else f"{m['slug']}/index.html",
    ),
    # Astro nested pages: _astro-source/src/pages/<dir>/<slug>.astro -> <dir>/<slug>/index.html
    (
        re.compile(r"^_astro-source/src/pages/(?P<path>.+)\.astro$"),
        lambda m: f"{m['path']}/index.html",
    ),
    # Blog content: _astro-source/src/content/blog/<slug>.md -> blog/<slug>/index.html
    (
        re.compile(r"^_astro-source/src/content/blog/(?P<slug>[^/]+)\.md$"),
        lambda m: f"blog/{m['slug']}/index.html",
    ),
    # Dashboard data: _astro-source/public/dashboard-data/<file> -> dashboard-data/<file>
    (
        re.compile(r"^_astro-source/public/dashboard-data/(?P<file>.+)$"),
        lambda m: f"dashboard-data/{m['file']}",
    ),
]

# ---------------------------------------------------------------------------
# Exemptions — files that don't need a paired counterpart at all
# ---------------------------------------------------------------------------

EXEMPT_PATTERNS = [
    re.compile(r"^_astro-source/src/components/.*"),
    re.compile(r"^_astro-source/src/layouts/.*"),
    re.compile(r"^_astro-source/src/content/config\..*"),
    re.compile(r"^_astro-source/astro\.config\..*"),
    re.compile(r"^_astro-source/tailwind\.config\..*"),
    re.compile(r"^_astro-source/package(-lock)?\.json$"),
    re.compile(r"^_astro-source/tsconfig\.json$"),
    re.compile(r"^_astro-source/public/(?!dashboard-data/).*"),  # other public assets
    re.compile(r"^_astro-source/src/.*\.css$"),
    re.compile(r"^_astro-source/src/.*\.scss$"),
    re.compile(r"^_astro-source/src/styles/.*"),
    re.compile(r"^tools/.*"),
    re.compile(r"^blog-visuals/.*"),
    re.compile(r"^\.github/.*"),
    re.compile(r"^widgets/.*"),  # hand-authored, no Astro source
    re.compile(r"^tv/.*"),  # hand-authored
    re.compile(r"^README(\..*)?$"),
    re.compile(r"^LICENSE$"),
    re.compile(r"^\.gitignore$"),
    re.compile(r"^package(-lock)?\.json$"),
    re.compile(r"^\.gitattributes$"),
    re.compile(r"^CNAME$"),
    re.compile(r"^_headers$"),
    re.compile(r"^_redirects$"),
]


def is_exempt(path: str) -> bool:
    return any(p.match(path) for p in EXEMPT_PATTERNS)


# ---------------------------------------------------------------------------
# Source <-> Built classification
# ---------------------------------------------------------------------------

def is_source(path: str) -> bool:
    return path.startswith("_astro-source/")


def is_built_root(path: str) -> bool:
    """A file at repo root that CF Pages serves directly (built Astro output)."""
    if is_source(path):
        return False
    if is_exempt(path):
        return False
    # Built pages live at <slug>/index.html, blog/<slug>/index.html,
    # dashboard-data/<file>, etc. Plus the root index.html.
    if path == "index.html":
        return True
    if re.match(r"^[^/]+/index\.html$", path):
        return True
    if re.match(r"^blog/[^/]+/index\.html$", path):
        return True
    if path.startswith("dashboard-data/"):
        return True
    # Other /_astro/ hashed bundles etc are built by Astro too
    if path.startswith("_astro/"):
        return True
    return False


def expected_built(src_path: str) -> str | None:
    """Given a source path, return the expected built path (or None if no mapping)."""
    for pattern, fn in SRC_TO_BUILT_RULES:
        m = pattern.match(src_path)
        if m:
            return fn(m)
    return None


def expected_source_candidates(built_path: str) -> list[str]:
    """Given a built path, return plausible source paths (multiple, since rules are 1:N reverse)."""
    candidates: list[str] = []

    # <slug>/index.html <- _astro-source/src/pages/<slug>.astro
    m = re.match(r"^([^/]+)/index\.html$", built_path)
    if m:
        slug = m.group(1)
        candidates.append(f"_astro-source/src/pages/{slug}.astro")

    # nested: <dir>/<slug>/index.html <- _astro-source/src/pages/<dir>/<slug>.astro
    m = re.match(r"^([^/]+)/([^/]+)/index\.html$", built_path)
    if m and m.group(1) != "blog":
        candidates.append(f"_astro-source/src/pages/{m.group(1)}/{m.group(2)}.astro")

    # blog/<slug>/index.html <- _astro-source/src/content/blog/<slug>.md
    m = re.match(r"^blog/([^/]+)/index\.html$", built_path)
    if m:
        slug = m.group(1)
        candidates.append(f"_astro-source/src/content/blog/{slug}.md")

    # dashboard-data/<file> <- _astro-source/public/dashboard-data/<file>
    if built_path.startswith("dashboard-data/"):
        candidates.append(f"_astro-source/public/{built_path}")

    # root index.html <- _astro-source/src/pages/index.astro
    if built_path == "index.html":
        candidates.append("_astro-source/src/pages/index.astro")

    return candidates


# ---------------------------------------------------------------------------
# Git diff
# ---------------------------------------------------------------------------

def git_changed_files(base: str, head: str) -> list[str]:
    try:
        out = subprocess.check_output(
            ["git", "diff", "--name-only", f"{base}...{head}"],
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"[verify_twofile] git diff failed: {e}", file=sys.stderr)
        sys.exit(2)
    return [line.strip() for line in out.splitlines() if line.strip()]


def repo_file_exists(path: str, ref: str = "HEAD") -> bool:
    try:
        subprocess.check_output(
            ["git", "cat-file", "-e", f"{ref}:{path}"],
            stderr=subprocess.DEVNULL,
        )
        return True
    except subprocess.CalledProcessError:
        return False


# ---------------------------------------------------------------------------
# Main check
# ---------------------------------------------------------------------------

def check(changed: Iterable[str], head_ref: str = "HEAD") -> list[str]:
    """Return a list of mismatch messages. Empty list = clean."""
    changed_set = set(changed)
    problems: list[str] = []

    for path in sorted(changed_set):
        if is_exempt(path):
            continue

        # Source side: expect matching built file also changed
        if is_source(path):
            built = expected_built(path)
            if built is None:
                # Source file but no mapping rule (e.g. new directory type).
                # Don't flag — might be an Astro addition we don't know about yet.
                continue
            if built not in changed_set:
                # Check if the built file even exists in the tree. If it doesn't,
                # this might be a brand-new page that hasn't been built yet (legit
                # for a feature branch that will be rebuilt on Dell). Flag as WARN.
                exists = repo_file_exists(built, head_ref)
                severity = "WARN" if not exists else "FAIL"
                problems.append(
                    f"[{severity}] source {path} changed but built {built} "
                    f"{'does not exist' if not exists else 'was not changed'}"
                )
            continue

        # Built side: expect at least one matching source file also changed
        if is_built_root(path):
            # Skip Astro-generated hashed bundles in _astro/ — they rebuild from source
            if path.startswith("_astro/"):
                continue
            candidates = expected_source_candidates(path)
            if not candidates:
                continue
            if not any(c in changed_set for c in candidates):
                # Check if any candidate source exists in tree
                existing = [c for c in candidates if repo_file_exists(c, head_ref)]
                if existing:
                    problems.append(
                        f"[FAIL] built {path} changed but matching source "
                        f"({', '.join(existing)}) was not changed — "
                        f"next rebuild will regress"
                    )
                else:
                    # No source exists — might be hand-authored (widgets/tv already exempt).
                    # Don't flag root HTML without source; may be legacy.
                    pass

    return problems


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(description="R-039 twofile check for bionic-banker")
    p.add_argument("--base", default="origin/main", help="base git ref (default: origin/main)")
    p.add_argument("--head", default="HEAD", help="head git ref (default: HEAD)")
    p.add_argument("--files", nargs="*", help="explicit file list (skips git diff)")
    p.add_argument("--warn-only", action="store_true", help="exit 0 even if mismatches found")
    args = p.parse_args()

    if args.files:
        changed = args.files
    else:
        changed = git_changed_files(args.base, args.head)

    if not changed:
        print("[verify_twofile] no files changed — clean")
        return 0

    print(f"[verify_twofile] checking {len(changed)} changed file(s)...")
    problems = check(changed, head_ref=args.head)

    if not problems:
        print("[verify_twofile] ✓ all source↔built pairs balanced (R-039 satisfied)")
        return 0

    print(f"\n[verify_twofile] ✗ R-039 violations ({len(problems)}):\n")
    for msg in problems:
        print(f"  {msg}")
    print()
    print("R-039: bionicbanker.tech is served by Cloudflare Pages git-integration.")
    print("       CF Pages serves committed dist/ at repo root as-is (no Astro rebuild).")
    print("       Content fixes require BOTH the source template AND the built output.")
    print("       See CLAUDE.md + MISTAKES.md §M-039.")

    if args.warn_only:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
