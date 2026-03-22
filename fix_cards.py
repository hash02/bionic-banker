#!/usr/bin/env python3
"""Fix card thumbnails: constrain height, remove from featured, fix tag colors."""
import re, os

# 1. Fix CSS — constrain card-thumb height, hide on featured
css_path = os.path.expanduser('~/bionic-banker/styles/global.css')
with open(css_path, 'r') as f:
    css = f.read()

# Replace card-thumb CSS block
old_thumb_css = """/* ── Article Card Thumbnails ── */
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
}"""

new_thumb_css = """/* ── Article Card Thumbnails ── */
.card-thumb {
  width: calc(100% + 2.5rem);
  max-height: 160px;
  overflow: hidden;
  border-radius: 10px 10px 0 0;
  margin: -1.25rem -1.25rem 1rem -1.25rem;
}
.card-thumb img {
  width: 100%;
  height: 160px;
  object-fit: cover;
  object-position: center 70%;
  transition: transform 0.4s ease;
}
.article-card:hover .card-thumb img {
  transform: scale(1.05);
}
/* Hide thumbnail on featured card — featured has its own layout */
.article-card-featured .card-thumb {
  display: none;
}
@media (max-width: 768px) {
  .card-thumb {
    margin: -1rem -1rem 0.75rem -1rem;
    width: calc(100% + 2rem);
    max-height: 120px;
    border-radius: 8px 8px 0 0;
  }
  .card-thumb img {
    height: 120px;
  }
}"""

css = css.replace(old_thumb_css, new_thumb_css)

# 2. Fix remaining non-green tag pill colors
# tag-red, tag-blue, tag-purple, tag-amber, tag-rose, tag-cyan should all be green
tag_replacements = {
    'tag-red': 'tag-green',
    'tag-blue': 'tag-green', 
    'tag-purple': 'tag-green',
    'tag-amber': 'tag-green',
    'tag-rose': 'tag-green',
    'tag-cyan': 'tag-green',
}

with open(css_path, 'w') as f:
    f.write(css)

# Sync CSS copies
for dest in ['~/bionic-banker/dist/styles/global.css', '~/bionic-banker/styles/styles/global.css']:
    dest = os.path.expanduser(dest)
    if os.path.exists(os.path.dirname(dest)):
        with open(dest, 'w') as f:
            f.write(css)

print("CSS fixed: card-thumb height constrained, featured hidden")

# 3. Fix tag pill classes in HTML files — replace non-green tags with green
html_files = [
    os.path.expanduser('~/bionic-banker/index.html'),
    os.path.expanduser('~/bionic-banker/articles/index.html'),
]

for filepath in html_files:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    for old_class, new_class in tag_replacements.items():
        content = content.replace(f'tag-pill {old_class}', f'tag-pill {new_class}')
    
    changes = sum(1 for a, b in zip(original, content) if a != b)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"{os.path.basename(filepath)}: tag colors fixed ({'changed' if changes else 'no changes needed'})")

# 4. Remove card-thumb from the featured card on homepage
homepage = os.path.expanduser('~/bionic-banker/index.html')
with open(homepage, 'r') as f:
    content = f.read()

# The featured card uses article-card-featured class — CSS now hides .card-thumb there
# But let's also remove any card-thumb div inside article-card-featured to keep HTML clean
# Pattern: inside <a ... class="article-card-featured"...> remove <div class="card-thumb">...</div>
content = re.sub(
    r'(<a[^>]*class="article-card-featured"[^>]*>)\s*<div class="card-thumb">.*?</div>',
    r'\1',
    content,
    flags=re.DOTALL
)

with open(homepage, 'w') as f:
    f.write(content)

print("Homepage: removed card-thumb from featured card HTML")
