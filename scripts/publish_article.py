#!/usr/bin/env python3
"""
publish_article.py — Bionic Banker Article Publisher
Reads a markdown draft from drafts/, converts to HTML, updates articles.html
"""

import sys
import os
import re
import yaml
import markdown
from datetime import datetime

# ── Config ────────────────────────────────────────────────────────────────────

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFTS_DIR = os.path.join(REPO_ROOT, "drafts")
ARTICLES_HTML = os.path.join(REPO_ROOT, "articles.html")

# Tag pill color map — matches existing site styles
TAG_COLORS = {
    "ai": "tag-purple",
    "blockchain": "tag-blue",
    "defi": "tag-cyan",
    "finance": "tag-amber",
    "aml": "tag-red",
    "thoughts": "tag-gray",
    "gaming": "tag-green",
    "privacy": "tag-cyan",
    "regulatory": "tag-amber",
    "builder": "tag-purple",
    "syos": "tag-purple",
    "nexus": "tag-purple",
    "crypto": "tag-blue",
    "zkp": "tag-cyan",
    "physics": "tag-cyan",
    "nobelprice": "tag-amber",
}

# ── Frontmatter parser ────────────────────────────────────────────────────────

def parse_frontmatter(content):
    """Extract YAML frontmatter and body from markdown content."""
    if not content.startswith("---"):
        print("ERROR: No YAML frontmatter found. Draft must start with ---")
        sys.exit(1)

    end = content.find("---", 3)
    if end == -1:
        print("ERROR: Frontmatter not closed with ---")
        sys.exit(1)

    fm_raw = content[3:end].strip()
    body = content[end+3:].strip()

    try:
        fm = yaml.safe_load(fm_raw)
    except yaml.YAMLError as e:
        print(f"ERROR: Bad YAML frontmatter: {e}")
        sys.exit(1)

    required = ["title", "lede", "tags", "data_tags", "read_time", "section"]
    for field in required:
        if field not in fm:
            print(f"ERROR: Missing required frontmatter field: '{field}'")
            sys.exit(1)

    return fm, body

# ── Markdown → HTML body ──────────────────────────────────────────────────────

def md_to_html_body(md_text):
    """Convert markdown body to HTML, adding Bionic Banker article classes."""
    md = markdown.Markdown(extensions=["extra", "nl2br"])
    raw_html = md.convert(md_text)

    # Wrap <p> tags are already there from markdown
    # Add pull-quote support: > blockquotes → pull-quote divs
    raw_html = re.sub(
        r'<blockquote>\s*<p>(.*?)</p>\s*</blockquote>',
        r'<div class="pull-quote">\1</div>',
        raw_html,
        flags=re.DOTALL
    )

    # Insight boxes: any <p> that starts with 🔑 gets insight-box treatment
    def make_insight(m):
        inner = m.group(1).strip().lstrip("🔑").strip()
        return f'<div class="insight-box"><div class="label">🔑 Key Insight</div><p>{inner}</p></div>'
    raw_html = re.sub(r'<p>🔑\s*(.*?)</p>', make_insight, raw_html, flags=re.DOTALL)

    return raw_html

# ── Tag pills HTML ────────────────────────────────────────────────────────────

def make_tag_pills(tags_str):
    """Convert comma-separated tags string to tag pill HTML."""
    tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    pills = []
    for tag in tags:
        color_key = tag.lower().replace(" ", "").replace("-", "")
        color = TAG_COLORS.get(color_key, "tag-gray")
        pills.append(f'          <span class="tag-pill {color}">{tag}</span>')
    return "\n".join(pills)

# ── Full article HTML ─────────────────────────────────────────────────────────

def build_article_html(fm, body_html, output_filename):
    """Generate full article HTML page."""
    tags_html = make_tag_pills(fm["tags"])
    date_str = fm.get("date", datetime.now().strftime("%Y-%m-%d"))
    read_time = fm["read_time"]
    title = fm["title"]
    lede = fm["lede"]

    # Build tag string for meta display (· separated)
    tag_display = fm["tags"].replace(",", " ·").strip()

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Bionic Banker</title>
  <meta name="description" content="{lede}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet" />
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-YS428H3H44"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-YS428H3H44');</script>
  <style>
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
    :root{{--bg:#050508;--bg2:#0b0b0f;--bg3:#111116;--accent:#1fa068;--accent-glow:rgba(31,160,104,0.10);--text:#f0f0f5;--text-2:#a0a0b0;--text-3:#606070;--b1:rgba(255,255,255,0.10);--radius:12px;}}
    html{{scroll-behavior:smooth;}}
    h1,h2,h3,h4,.nav-logo,.article-header h1{{font-family:'Bricolage Grotesque','Inter',sans-serif;letter-spacing:-0.025em;}}body{{font-family:'Plus Jakarta Sans',sans-serif;background:var(--bg);color:var(--text);line-height:1.6;-webkit-font-smoothing:antialiased;}}
    a{{color:inherit;text-decoration:none;}}
    nav{{position:sticky;top:0;z-index:100;background:rgba(5,5,8,0.92);backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,0.06);padding:0 2rem;height:56px;display:flex;align-items:center;justify-content:space-between;}}
    .nav-logo{{font-size:1.1rem;font-weight:700;letter-spacing:-0.02em;}}
    .nav-logo span{{color:rgba(255,255,255,0.55);}}
    .nav-back{{font-size:0.85rem;color:var(--text-muted);transition:color 0.2s;}}
    .nav-back:hover{{color:var(--accent);}}
    .nav-right {{display:flex;align-items:center;gap:1.75rem;}}
    .nav-links {{display:flex;gap:1.5rem;list-style:none;}}
    .nav-links a {{font-size:0.82rem;color:rgba(255,255,255,0.4);font-weight:500;transition:color 0.18s;}}
    .nav-links a:hover {{color:rgba(255,255,255,0.7);}}
    .nav-cta {{font-size:0.76rem;font-weight:600;background:transparent;border:1px solid rgba(255,255,255,0.10);color:rgba(255,255,255,0.55);padding:0.3rem 0.85rem;border-radius:8px;transition:border-color 0.2s,color 0.2s;}}
    .nav-cta:hover {{border-color:rgba(255,255,255,0.16);color:rgba(255,255,255,0.8);}}
    .article-header{{max-width:760px;margin:0 auto;padding:3rem 2rem 2rem;}}
    .article-meta{{display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem;flex-wrap:wrap;}}
    .article-tag{{font-size:0.72rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:var(--accent);background:var(--accent-glow);border:1px solid var(--border);border-radius:999px;padding:0.25rem 0.75rem;}}
    .article-date{{font-size:0.82rem;color:var(--text-dim);}}
    .article-header h1{{font-size:clamp(1.75rem,4vw,2.8rem);font-weight:800;letter-spacing:-0.04em;line-height:1.15;margin-bottom:1.25rem;}}
    .lede{{font-size:1.1rem;color:var(--text-muted);line-height:1.7;border-left:3px solid rgba(255,255,255,0.18);padding-left:1.25rem;margin-bottom:2rem;}}
    .author-bar{{display:flex;align-items:center;gap:1rem;padding:1rem 0;border-top:1px solid var(--border);border-bottom:1px solid rgba(255,255,255,0.06);margin-bottom:2.5rem;}}
    .author-avatar{{width:44px;height:44px;border-radius:50%;background:var(--bg3);border:2px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:1.1rem;font-weight:700;color:var(--accent);flex-shrink:0;}}
    .author-info .name{{font-size:0.9rem;font-weight:600;}}
    .author-info .title{{font-size:0.78rem;color:var(--text-dim);}}
    .article-body{{max-width:760px;margin:0 auto;padding:0 2rem 5rem;}}
    .article-body p{{font-size:1.05rem;line-height:1.88;color:#cccce0;margin-bottom:1.75rem;}}
    .article-body h2{{font-size:1.45rem;font-weight:700;letter-spacing:-0.02em;color:var(--text);margin:3.5rem 0 1.25rem;padding-top:1.5rem;border-top:1px solid var(--border);}}
    .article-body h3{{font-size:1.15rem;font-weight:600;color:var(--text);margin:2rem 0 0.75rem;}}
    .article-body ul,.article-body ol{{margin:0 0 1.75rem 1.5rem;color:#cccce0;}}
    .article-body li{{font-size:1.05rem;line-height:1.75;margin-bottom:0.35rem;}}
    .article-body a{{color:var(--accent);text-decoration:underline;text-underline-offset:3px;}}
    .article-body code{{font-family:'Courier New',monospace;font-size:0.88em;background:var(--bg3);border:1px solid var(--border);border-radius:4px;padding:0.1em 0.4em;}}
    .article-body pre{{background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;margin:2rem 0;overflow-x:auto;}}
    .article-body pre code{{background:none;border:none;padding:0;font-size:0.9rem;}}
    .pull-quote{{background:var(--accent-glow);border-left:4px solid rgba(255,255,255,0.18);border-radius:0 var(--radius) var(--radius) 0;padding:1.5rem 2rem;margin:2.5rem 0;font-size:1.1rem;font-weight:500;color:var(--text);line-height:1.65;font-style:italic;}}
    .insight-box{{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;margin:2rem 0;}}
    .insight-box .label{{font-size:0.72rem;font-weight:600;text-transform:uppercase;letter-spacing:0.1em;color:#1fa068;margin-bottom:0.75rem;}}
    .insight-box p{{font-size:0.95rem!important;margin-bottom:0!important;line-height:1.65!important;}}
    .article-newsletter{{background:var(--bg2);border:1px solid var(--border);border-radius:16px;padding:2.5rem;text-align:center;margin:3rem 0;}}
    .article-newsletter h3{{font-size:1.3rem;font-weight:700;margin-bottom:0.5rem;margin-top:0;}}
    .article-newsletter p{{color:var(--text-muted)!important;font-size:0.9rem!important;margin-bottom:1.5rem!important;}}
    .btn-primary{{display:inline-block;background:var(--accent);color:#fff;font-size:0.9rem;font-weight:600;padding:0.75rem 1.75rem;border-radius:var(--radius);transition:opacity 0.2s;}}
    .btn-primary:hover{{opacity:0.88;}}
    footer{{border-top:1px solid var(--border);padding:2rem;text-align:center;}}
    .footer-copy{{font-size:0.8rem;color:var(--text-dim);}}
    h1,h2,h3 {{text-shadow:0 0 40px rgba(255,255,255,0.14);}}
    .nav-logo {{text-shadow:0 0 32px rgba(255,255,255,0.18);}}
    .lede {{text-shadow:0 0 28px rgba(255,255,255,0.10);}}
    @media(max-width:640px){{.article-header,.article-body{{padding-left:1.25rem;padding-right:1.25rem;}}}}
  </style>
</head>
<body>

  <nav>
    <a href="index.html" class="nav-logo">Bionic <span>Banker</span></a>
    <div class="nav-right">
      <ul class="nav-links">
        <li><a href="articles.html">All Articles</a></li>
        <li><a href="index.html#about">About</a></li>
      </ul>
      <a href="index.html#newsletter" class="nav-cta">Subscribe</a>
    </div>
  </nav>

  <div class="article-header">
    <div class="article-meta">
      <span class="article-tag">{tag_display}</span>
      <span class="article-date">{date_str} · {read_time} read</span>
    </div>
    <h1>{title}</h1>
    <p class="lede">{lede}</p>
    <div class="author-bar">
      <div class="author-avatar">H</div>
      <div class="author-info">
        <div class="name">HASH — The Bionic Banker</div>
        <div class="title">Computer Engineer · Financial Advisor · Blockchain Builder</div>
      </div>
    </div>
  </div>

  <div class="article-body">

{body_html}

    <div class="article-newsletter">
      <h3>More from Bionic Banker</h3>
      <p>Tech, finance, blockchain, and building in public — from inside the industry.</p>
      <a href="index.html#newsletter" class="btn-primary">Subscribe</a>
    </div>

  </div>

  <footer>
    <p class="footer-copy">© {datetime.now().year} Bionic Banker · Built by HASH</p>
  </footer>

</body>
</html>
'''
    return html

# ── Build article card for articles.html ─────────────────────────────────────

def build_article_card(fm, output_filename):
    """Generate the article card HTML snippet for articles.html."""
    tags_list = [t.strip() for t in fm["tags"].split(",") if t.strip()]

    pills = []
    for tag in tags_list:
        color_key = tag.lower().replace(" ", "").replace("-", "")
        color = TAG_COLORS.get(color_key, "tag-gray")
        pills.append(f'          <span class="tag-pill {color}">{tag}</span>')
    pills_html = "\n".join(pills)

    data_tags = fm["data_tags"].strip()
    title = fm["title"]
    lede = fm["lede"]
    read_time = fm["read_time"]

    card = f'''      <a href="{output_filename}" class="article-card" data-tags="{data_tags}">
        <div class="article-tags">
{pills_html}
        </div>
        <h3>{title}</h3>
        <p>{lede}</p>
        <div class="card-footer"><span class="read-more">Read →</span><span class="read-time">{read_time}</span></div>
      </a>'''

    return card

# ── Update articles.html ──────────────────────────────────────────────────────

def update_articles_html(card_html, section):
    """Insert new article card into the correct section of articles.html."""
    with open(ARTICLES_HTML, "r", encoding="utf-8") as f:
        content = f.read()

    section_lower = section.lower().strip()

    # Map section name to the comment marker in articles.html
    section_markers = {
        "deep dives": "<!-- ── DEEP DIVES ── -->",
        "thoughts": "<!-- ── THOUGHTS ── -->",
    }

    marker = section_markers.get(section_lower)

    if marker and marker in content:
        # Insert card right after the section-divider div that follows the marker
        # Find: marker → section-divider → insert card here
        divider_pattern = re.escape(marker) + r'(\s*<div class="section-divider">.*?</div>)'
        match = re.search(divider_pattern, content, re.DOTALL)
        if match:
            insert_pos = match.end()
            content = content[:insert_pos] + "\n\n" + card_html + "\n" + content[insert_pos:]
        else:
            # Fallback: insert after the marker itself
            insert_pos = content.find(marker) + len(marker)
            content = content[:insert_pos] + "\n\n" + card_html + "\n" + content[insert_pos:]
    else:
        # No section match — insert before first article-card (at the top)
        first_card = content.find('<a href=')
        if first_card != -1:
            content = content[:first_card] + card_html + "\n\n      " + content[first_card:]
        else:
            print("WARNING: Could not find insertion point in articles.html")
            return

    with open(ARTICLES_HTML, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ articles.html updated — card added to '{section}' section")

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage: python publish_article.py <draft_filename.md>")
        sys.exit(1)

    draft_file = sys.argv[1]
    draft_path = os.path.join(DRAFTS_DIR, draft_file)

    if not os.path.exists(draft_path):
        print(f"ERROR: Draft not found: {draft_path}")
        sys.exit(1)

    print(f"📄 Reading draft: {draft_file}")

    with open(draft_path, "r", encoding="utf-8") as f:
        raw = f.read()

    fm, body_md = parse_frontmatter(raw)
    print(f"✅ Frontmatter parsed — title: {fm['title']}")

    # Output filename: same stem as draft, .html extension
    stem = os.path.splitext(draft_file)[0]
    output_filename = f"{stem}.html"
    output_path = os.path.join(REPO_ROOT, output_filename)

    body_html = md_to_html_body(body_md)
    print(f"✅ Markdown converted — {len(body_html)} chars of HTML")

    article_html = build_article_html(fm, body_html, output_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(article_html)
    print(f"✅ Article written: {output_filename}")

    card_html = build_article_card(fm, output_filename)
    update_articles_html(card_html, fm["section"])

    print(f"\n🚀 Done. Files to commit:")
    print(f"   - {output_filename}")
    print(f"   - articles.html")

if __name__ == "__main__":
    main()
