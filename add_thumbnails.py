#!/usr/bin/env python3
"""Add hero image thumbnails to article cards on homepage + articles page."""
import re
import os

# Map blog slugs to their hero image files
SLUG_TO_IMAGE = {
    'aml-engine': 'aml-engine-hero.png',
    'nexus-agent': 'nexus-agent-hero.png',
    'syos': 'syos-hero.png',
    'syos-falsification': 'syos-falsification-hero.png',
    'anchor-problem': 'anchor-problem-hero.png',
    'zkp-explained': 'zkp-explained-hero.png',
    'tornado-cash': 'tornado-cash-hero.png',
    'defi': 'defi-hero.png',
    'aave': 'aave-hero.png',
    'uniswap': 'uniswap-hero.png',
    'paypal': 'paypal-hero.png',
    'extreme-fear': 'extreme-fear-hero.png',
    'blockchain-trends': 'blockchain-trends-hero.png',
    'how-to-start-crypto': 'how-to-start-crypto-hero.png',
    'gen-z-finance': 'gen-z-finance-hero.png',
    'fintech': 'fintech-hero.png',
    'physics-of-ai': 'physics-of-ai-hero.png',
    'ai-memory-system': 'ai-memory-system-hero.png',
    'kill-agent': 'kill-agent-hero.png',
    'memory-case-study': 'memory-case-study-hero.png',
    'folder-agent': 'folder-agent-hero.png',
    'folder-agent-part2': 'folder-agent-part2-hero.png',
    'the-anchor': 'the-anchor-hero.png',
    'agent-evolution': 'agent-evolution-hero.png',
    'agent-replacement': 'agent-replacement-hero.png',
}

def add_thumbnails_to_html(filepath):
    """Insert thumbnail <img> right after <a> opening tag for article cards."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    changes = 0
    
    # Pattern: <a href="/blog/SLUG" class="article-card...">
    # Insert: <div class="card-thumb"><img src="/blog-visuals/png/SLUG-hero.png" alt="..." loading="lazy"></div>
    def replace_card(match):
        nonlocal changes
        full_match = match.group(0)
        slug = match.group(1)
        
        # Skip if already has a thumbnail
        if 'card-thumb' in full_match:
            return full_match
        
        img_file = SLUG_TO_IMAGE.get(slug)
        if not img_file:
            return full_match
        
        # Find the end of the opening <a> tag
        a_end = full_match.find('>') + 1
        if a_end <= 0:
            return full_match
        
        thumb_html = f'<div class="card-thumb"><img src="/blog-visuals/png/{img_file}" alt="" loading="lazy" width="1200" height="630"></div>'
        result = full_match[:a_end] + thumb_html + full_match[a_end:]
        changes += 1
        return result
    
    # Match article cards with blog links
    # Captures: <a href="/blog/SLUG" class="article-card..."> followed by content up to </a>
    pattern = r'(<a\s+href="/blog/([^"]+)"\s+class="article-card[^"]*"[^>]*>)(.*?</a>)'
    content = re.sub(pattern, lambda m: add_thumb(m, SLUG_TO_IMAGE), content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    return changes

def add_thumb(match, slug_map):
    """Add thumbnail to an article card match."""
    opening_tag = match.group(1)
    slug = match.group(2)
    rest = match.group(3)
    
    # Skip if already has thumbnail
    if 'card-thumb' in rest:
        return match.group(0)
    
    img_file = slug_map.get(slug)
    if not img_file:
        return match.group(0)
    
    thumb = f'<div class="card-thumb"><img src="/blog-visuals/png/{img_file}" alt="" loading="lazy" width="1200" height="630"></div>'
    return opening_tag + thumb + rest

def add_css():
    """Add card thumbnail CSS to global.css."""
    css_path = os.path.expanduser('~/bionic-banker/styles/global.css')
    with open(css_path, 'r') as f:
        css = f.read()
    
    if 'card-thumb' in css:
        print("CSS already has card-thumb styles")
        return
    
    thumb_css = """
/* ── Article Card Thumbnails ── */
.card-thumb {
  width: 100%;
  aspect-ratio: 1200 / 630;
  overflow: hidden;
  border-radius: 10px 10px 0 0;
  margin: -1.25rem -1.25rem 1rem -1.25rem;
  width: calc(100% + 2.5rem);
}
.card-thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}
.article-card:hover .card-thumb img,
.article-card-featured:hover .card-thumb img {
  transform: scale(1.05);
}
@media (max-width: 768px) {
  .card-thumb {
    margin: -1rem -1rem 0.75rem -1rem;
    width: calc(100% + 2rem);
    border-radius: 8px 8px 0 0;
  }
}
"""
    # Insert before the closing comment or at end
    css += thumb_css
    
    with open(css_path, 'w') as f:
        f.write(css)
    
    # Also sync to dist
    dist_css = os.path.expanduser('~/bionic-banker/dist/styles/global.css')
    if os.path.exists(os.path.dirname(dist_css)):
        with open(dist_css, 'w') as f:
            f.write(css)
    
    # Also sync nested copy
    nested = os.path.expanduser('~/bionic-banker/styles/styles/global.css')
    if os.path.exists(os.path.dirname(nested)):
        with open(nested, 'w') as f:
            f.write(css)
    
    print("Added card-thumb CSS to global.css + synced copies")

def main():
    add_css()
    
    # Process articles page
    articles_page = os.path.expanduser('~/bionic-banker/articles/index.html')
    if os.path.exists(articles_page):
        with open(articles_page, 'r') as f:
            content = f.read()
        
        pattern = r'(<a\s+href="/blog/([^"]+)"\s+class="article-card[^"]*"[^>]*>)(.*?</a>)'
        
        count = 0
        def replacer(m):
            nonlocal count
            result = add_thumb(m, SLUG_TO_IMAGE)
            if result != m.group(0):
                count += 1
            return result
        
        content = re.sub(pattern, replacer, content, flags=re.DOTALL)
        
        with open(articles_page, 'w') as f:
            f.write(content)
        print(f"articles/index.html: {count} thumbnails added")
    
    # Process homepage
    homepage = os.path.expanduser('~/bionic-banker/index.html')
    if os.path.exists(homepage):
        with open(homepage, 'r') as f:
            content = f.read()
        
        pattern = r'(<a\s+href="/blog/([^"]+)"\s+class="article-card[^"]*"[^>]*>)(.*?</a>)'
        
        count = 0
        def replacer2(m):
            nonlocal count
            result = add_thumb(m, SLUG_TO_IMAGE)
            if result != m.group(0):
                count += 1
            return result
        
        content = re.sub(pattern, replacer2, content, flags=re.DOTALL)
        
        with open(homepage, 'w') as f:
            f.write(content)
        print(f"index.html: {count} thumbnails added")

if __name__ == '__main__':
    main()
