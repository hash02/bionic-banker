#!/usr/bin/env python3
"""Local public-post duplicate guard.

Usage:
  python scripts/post_ledger_check.py --caption-file distribution/package.md --article-url URL --carousel-asset PATH

This is intentionally local-first: it checks the ledger before any browser/live LinkedIn action.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "distribution" / "post-ledger.json"


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"#[\w-]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def digest(text: str) -> str:
    return hashlib.sha256(normalize(text).encode()).hexdigest()[:16]


def extract_post_copy(text: str) -> str:
    if "## Post copy" in text and "## Carousel upload order" in text:
        start = text.index("## Post copy") + len("## Post copy")
        end = text.index("## Carousel upload order")
        return text[start:end].strip()
    return text.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--caption-file", required=True)
    parser.add_argument("--article-url", default="")
    parser.add_argument("--carousel-asset", default="")
    args = parser.parse_args()

    caption = extract_post_copy(Path(args.caption_file).read_text())
    caption_hash = digest(caption)
    ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {"posts": []}

    blockers = []
    for post in ledger.get("posts", []):
        if post.get("caption_hash") == caption_hash:
            blockers.append(f"same caption_hash as {post.get('linkedin_url') or post.get('title')}")
        if args.article_url and post.get("article_url") == args.article_url:
            blockers.append(f"same article_url as {post.get('linkedin_url') or post.get('title')}")
        if args.carousel_asset and post.get("carousel_asset") == args.carousel_asset:
            blockers.append(f"same carousel_asset as {post.get('linkedin_url') or post.get('title')}")

    print(json.dumps({"caption_hash": caption_hash, "blockers": blockers}, indent=2))
    return 1 if blockers else 0


if __name__ == "__main__":
    sys.exit(main())
