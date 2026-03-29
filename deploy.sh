#!/usr/bin/env bash
# deploy.sh — Build Astro site and deploy to Cloudflare Pages via git push
# Usage: ./deploy.sh
# [WUKONG]
set -euo pipefail

REPO_ROOT="/home/hash/bionic-banker"
ASTRO_SRC="${REPO_ROOT}/_astro-source"
DIST_DIR="${ASTRO_SRC}/dist"
TIMESTAMP="$(date '+%Y-%m-%d %H:%M')"

echo "=== bionicbanker.tech deploy — ${TIMESTAMP} ==="

# --- Step 1: Build ---
echo ""
echo "[1/5] Building Astro site..."
cd "${ASTRO_SRC}"
npm run build
echo "      Build complete."

# --- Step 2: Verify dist exists ---
if [ ! -d "${DIST_DIR}" ]; then
    echo "ERROR: dist/ directory not found after build. Aborting."
    exit 1
fi

# --- Step 3: Copy built output to repo root ---
echo ""
echo "[2/5] Copying dist/ contents to repo root..."
# cp -a overlays dist contents onto repo root without deleting unrelated files
cp -a "${DIST_DIR}/." "${REPO_ROOT}/"
echo "      Files copied."

# --- Step 4: Stage and commit ---
echo ""
echo "[3/5] Staging changes..."
cd "${REPO_ROOT}"
git add -A

# Check if there are actually changes to commit
if git diff --cached --quiet; then
    echo "      No changes detected — nothing to deploy."
    exit 0
fi

echo ""
echo "[4/5] Committing..."
git commit -m "$(cat <<EOF
deploy: rebuild site ${TIMESTAMP}
EOF
)"

# --- Step 5: Push ---
echo ""
echo "[5/5] Pushing to origin/main..."
git push origin main

echo ""
echo "=== Deploy complete — ${TIMESTAMP} ==="
echo "    Site will update shortly at https://bionicbanker.tech"
