#!/usr/bin/env python3
"""Generate missing hero images + insert thumbnails for 4 articles."""
import sys, os
sys.path.insert(0, os.path.expanduser('~/bionic-banker'))
from generate_images import generate_article_image

MISSING = [
    {"slug": "claude-proxy-api", "title": "Claude Max as Your Personal API", "tags": ["AI", "Economics", "Code"], "template": "circuit"},
    {"slug": "roast-gallery", "title": "Roast Gallery: Suspicious Wallets Roasted", "tags": ["AML", "Blockchain", "AI"], "template": "network"},
    {"slug": "agent-architecture", "title": "Folder Agent Architecture", "tags": ["AI", "Systems", "Architecture"], "template": "grid"},
    {"slug": "aml-roaster", "title": "The AML Roaster Engine", "tags": ["AML", "AI", "Blockchain"], "template": "circuit"},
]

output_dir = os.path.expanduser("~/bionic-banker/blog-visuals/png")

for article in MISSING:
    path = generate_article_image(article, output_dir)
    print(f"Generated: {path}")

# Now insert thumbnails into articles/index.html for these 4
import re

SLUG_MAP = {a['slug']: f"{a['slug']}-hero.png" for a in MISSING}

articles_page = os.path.expanduser('~/bionic-banker/articles/index.html')
with open(articles_page, 'r') as f:
    content = f.read()

def add_thumb(match):
    opening = match.group(1)
    slug = match.group(2)
    rest = match.group(3)
    if 'card-thumb' in rest:
        return match.group(0)
    img_file = SLUG_MAP.get(slug)
    if not img_file:
        return match.group(0)
    thumb = f'<div class="card-thumb"><img src="/blog-visuals/png/{img_file}" alt="" loading="lazy" width="1200" height="630"></div>'
    return opening + thumb + rest

pattern = r'(<a\s+href="/blog/([^"]+)"\s+class="article-card[^"]*"[^>]*>)(.*?</a>)'
content_new = re.sub(pattern, add_thumb, content, flags=re.DOTALL)

with open(articles_page, 'w') as f:
    f.write(content_new)

# Count new thumbs
added = content_new.count('card-thumb') - content.count('card-thumb')
print(f"Added {added} new thumbnails to articles page")
