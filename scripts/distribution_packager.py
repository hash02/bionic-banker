#!/usr/bin/env python3
"""Create a platform-native Bionic distribution pack for one article slug.

This is deterministic scaffolding, not an autoposter.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG_SRC = ROOT / "_astro-source" / "src" / "content" / "blog"
PACK_ROOT = ROOT / "distribution" / "packs"


def read_article(slug: str) -> tuple[str, str, list[str]]:
    p = BLOG_SRC / f"{slug}.md"
    if not p.exists():
        raise SystemExit(f"Article not found: {p}")
    text = p.read_text()
    title = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', text, re.M)
    desc = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', text, re.M)
    tags = re.search(r'^tags:\s*\[(.*?)\]', text, re.M)
    tag_list = []
    if tags:
        tag_list = [t.strip().strip('"\'') for t in tags.group(1).split(',') if t.strip()]
    return (title.group(1) if title else slug.replace('-', ' ').title(), desc.group(1) if desc else '', tag_list)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--claim", default="")
    ap.add_argument("--question", default="")
    ap.add_argument("--visual", default="")
    args = ap.parse_args()

    title, desc, tags = read_article(args.slug)
    url = f"https://bionicbanker.tech/blog/{args.slug}/"
    claim = args.claim or desc or title
    question = args.question or "What output would you never let through without a human evidence check?"
    visual = args.visual or f"social-assets/linkedin-ready/{args.slug}/"
    out = PACK_ROOT / args.slug
    today = dt.datetime.now().astimezone().isoformat(timespec="seconds")

    hashtags = ["#AIGovernance", "#ModelRisk", "#AICompliance", "#FintechRisk", "#OperationalRisk", "#EnterpriseAI"]

    write(out / "linkedin.md", f"""# LinkedIn package — {title}

Image / asset:
`{visual}`

## Caption

{claim}

Here is the mistake to watch:

teams will treat a confident AI output like a reviewed source packet.

The better question is not:

“Does this sound right?”

It is:

“What would prove this claim false?”

Use the control model:

1. exact claim
2. source trail
3. freshness
4. relevance
5. falsifier
6. reviewer
7. saved audit trail

{question}

{' '.join(hashtags)}
""")

    write(out / "first-comment.md", f"""Full source / checklist:
{url}
""")

    write(out / "x-thread.md", f"""# X thread package — {title}

1/ {claim}

2/ The failure mode is simple: confident AI text can start looking like evidence before anyone checks source, freshness, relevance, or approval.

3/ The control model: claim -> source -> freshness -> relevance -> falsifier -> reviewer -> trail.

4/ The question is not whether the answer sounds right. The question is what would prove it false.

5/ Longer checklist: {url}
""")

    write(out / "reddit-answer.md", f"""# Reddit-safe answer draft — {title}

If this comes up in a relevant subreddit, lead with the answer, not the link.

AI outputs in finance/risk workflows should be treated as drafts until a human can identify the exact claim, supporting source, freshness, relevance, possible falsifier, reviewer, and saved audit trail.

Do not post this as promotion. Only add the Bionic link if the community rules allow it and the link directly helps the discussion.

Optional link if allowed:
{url}
""")

    write(out / "devto-hashnode-angle.md", f"""# Dev.to / Hashnode angle — {title}

Tutorial angle:

Build a simple AI-output evidence checklist for finance/risk workflows.

Sections:

1. Why AI answers are not evidence.
2. Extracting claims from model output.
3. Attaching source trails.
4. Recording reviewer decisions.
5. Saving an audit packet.
6. Boundary: not legal/compliance advice.

Source article:
{url}
""")

    write(out / "pre-post-checklist.md", f"""# Pre-post checklist — {title}

- [ ] Hook is a recognizable mistake.
- [ ] Visual is readable on mobile.
- [ ] Caption has one clear control model.
- [ ] Link is in first comment, not main body.
- [ ] Practitioner question exists.
- [ ] Hashtags are sharp and limited.
- [ ] Platform rules/norms checked.
- [ ] Metrics ledger row prepared.
- [ ] Stop conditions reviewed.
- [ ] No private machinery exposed.
- [ ] No legal/investment/tax/compliance determination.
""")

    write(out / "metrics-row.yaml", f"""date: {today}
platform: linkedin
post_url:
topic: {title!r}
format: sharp single-image post + short caption + first-comment link
hook: {claim!r}
visual_path: {visual!r}
caption_path: {str(out / 'linkedin.md')!r}
article_url: {url!r}
posted_at_local:
metrics:
  impressions_2h:
  impressions_24h:
  impressions_7d:
  reactions:
  comments:
  reposts:
  saves:
  profile_views:
  new_followers:
qualitative:
  best_comment:
  who_engaged:
  what_worked:
  what_failed:
  next_test:
""")

    print(out)


if __name__ == "__main__":
    main()
