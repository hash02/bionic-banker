#!/usr/bin/env python3
"""Generate v2 hero images — subtle, atmospheric, no text. Matches Vanta 3D aesthetic."""

import math
import random
import hashlib
import os
from PIL import Image, ImageDraw, ImageFilter

# Site palette
C = {
    'bg': (2, 2, 4),
    'g1': (13, 122, 74),    # dark green
    'g2': (31, 160, 104),   # accent
    'g3': (52, 211, 153),   # bright
    'g4': (110, 231, 183),  # light
    'white': (228, 228, 236),
}

WIDTH, HEIGHT = 1200, 630

ARTICLES = [
    {"slug": "aml-engine", "template": "nodes"},
    {"slug": "nexus-agent", "template": "nodes"},
    {"slug": "syos", "template": "drift"},
    {"slug": "syos-falsification", "template": "grid_glow"},
    {"slug": "anchor-problem", "template": "drift"},
    {"slug": "zkp-explained", "template": "grid_glow"},
    {"slug": "tornado-cash", "template": "nodes"},
    {"slug": "defi", "template": "drift"},
    {"slug": "aave", "template": "nodes"},
    {"slug": "uniswap", "template": "grid_glow"},
    {"slug": "paypal", "template": "drift"},
    {"slug": "extreme-fear", "template": "orbs"},
    {"slug": "blockchain-trends", "template": "grid_glow"},
    {"slug": "how-to-start-crypto", "template": "drift"},
    {"slug": "gen-z-finance", "template": "orbs"},
    {"slug": "fintech", "template": "nodes"},
    {"slug": "physics-of-ai", "template": "orbs"},
    {"slug": "ai-memory-system", "template": "nodes"},
    {"slug": "kill-agent", "template": "grid_glow"},
    {"slug": "memory-case-study", "template": "drift"},
    {"slug": "folder-agent", "template": "nodes"},
    {"slug": "folder-agent-part2", "template": "nodes"},
    {"slug": "the-anchor", "template": "orbs"},
    {"slug": "agent-evolution", "template": "drift"},
    {"slug": "agent-replacement", "template": "orbs"},
    {"slug": "claude-proxy-api", "template": "nodes"},
    {"slug": "roast-gallery", "template": "grid_glow"},
    {"slug": "agent-architecture", "template": "nodes"},
    {"slug": "aml-roaster", "template": "grid_glow"},
]

def seed(slug):
    return int(hashlib.md5(slug.encode()).hexdigest()[:8], 16)

def draw_soft_circle(img, cx, cy, radius, color, alpha_max=60):
    """Draw a soft radial gradient circle (glow orb)."""
    overlay = Image.new('RGBA', img.size, (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    for r in range(radius, 0, -2):
        a = int(alpha_max * (1 - (r / radius) ** 1.5))
        if a > 0:
            draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color + (a,))
    img.paste(Image.alpha_composite(img, overlay))

def template_nodes(img, rng):
    """Subtle connected nodes — like Vanta NET but static and blurred."""
    draw = ImageDraw.Draw(img, 'RGBA')
    nodes = [(rng.randint(30, WIDTH-30), rng.randint(30, HEIGHT-30)) for _ in range(18)]
    
    # Draw subtle connections
    for i, (x1, y1) in enumerate(nodes):
        for j, (x2, y2) in enumerate(nodes):
            if i < j:
                dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                if dist < 350:
                    a = int(max(5, 25 - dist * 0.07))
                    draw.line([(x1, y1), (x2, y2)], fill=(*C['g1'], a), width=1)
    
    # Draw node glows
    for x, y in nodes:
        r = rng.randint(8, 25)
        draw_soft_circle(img, x, y, r, C['g2'], alpha_max=rng.randint(20, 45))
    
    # Add 2-3 large ambient glows
    for _ in range(rng.randint(2, 3)):
        gx = rng.randint(100, WIDTH-100)
        gy = rng.randint(50, HEIGHT-50)
        draw_soft_circle(img, gx, gy, rng.randint(120, 250), C['g1'], alpha_max=rng.randint(12, 25))

def template_drift(img, rng):
    """Flowing gradient waves — atmospheric, dreamy."""
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Large background orbs
    for _ in range(4):
        gx = rng.randint(-100, WIDTH+100)
        gy = rng.randint(-50, HEIGHT+50)
        draw_soft_circle(img, gx, gy, rng.randint(150, 350), C['g1'], alpha_max=rng.randint(15, 30))
    
    # Flowing sine curves
    for wave in range(rng.randint(3, 5)):
        freq = rng.uniform(0.003, 0.012)
        amp = rng.randint(40, 120)
        offset_y = rng.randint(50, HEIGHT-50)
        phase = rng.uniform(0, math.pi * 2)
        pts = []
        for x in range(0, WIDTH, 2):
            y = offset_y + math.sin(x * freq + phase) * amp
            pts.append((x, int(y)))
        if len(pts) > 1:
            a = rng.randint(12, 30)
            draw.line(pts, fill=(*C['g2'], a), width=rng.randint(1, 2))
    
    # Tiny scattered dots
    for _ in range(rng.randint(15, 30)):
        x, y = rng.randint(0, WIDTH), rng.randint(0, HEIGHT)
        r = rng.randint(1, 3)
        a = rng.randint(20, 60)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(*C['g3'], a))

def template_grid_glow(img, rng):
    """Subtle grid with glowing intersection points."""
    draw = ImageDraw.Draw(img, 'RGBA')
    cell = rng.choice([50, 60, 70])
    
    # Very faint grid lines
    for x in range(0, WIDTH, cell):
        draw.line([(x, 0), (x, HEIGHT)], fill=(*C['g1'], 10), width=1)
    for y in range(0, HEIGHT, cell):
        draw.line([(0, y), (WIDTH, y)], fill=(*C['g1'], 10), width=1)
    
    # Glowing points at some intersections
    for _ in range(rng.randint(8, 18)):
        gx = rng.randint(0, WIDTH // cell) * cell
        gy = rng.randint(0, HEIGHT // cell) * cell
        r = rng.randint(10, 30)
        draw_soft_circle(img, gx, gy, r, C['g2'], alpha_max=rng.randint(25, 50))
    
    # 1-2 large ambient orbs
    for _ in range(rng.randint(1, 2)):
        ox = rng.randint(100, WIDTH-100)
        oy = rng.randint(50, HEIGHT-50)
        draw_soft_circle(img, ox, oy, rng.randint(180, 300), C['g1'], alpha_max=rng.randint(12, 22))

def template_orbs(img, rng):
    """Pure atmospheric orbs — like the glow-orb background on the site."""
    for _ in range(rng.randint(4, 7)):
        ox = rng.randint(-100, WIDTH+100)
        oy = rng.randint(-50, HEIGHT+50)
        color = rng.choice([C['g1'], C['g2'], C['g3']])
        r = rng.randint(80, 300)
        a = rng.randint(10, 35)
        draw_soft_circle(img, ox, oy, r, color, alpha_max=a)
    
    # Tiny sparkle dots
    for _ in range(rng.randint(20, 40)):
        x, y = rng.randint(0, WIDTH), rng.randint(0, HEIGHT)
        r = rng.randint(1, 2)
        a = rng.randint(30, 80)
        draw = ImageDraw.Draw(img, 'RGBA')
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(*C['g3'], a))

TEMPLATES = {
    'nodes': template_nodes,
    'drift': template_drift,
    'grid_glow': template_grid_glow,
    'orbs': template_orbs,
}

def generate(article, out_dir):
    rng = random.Random(seed(article['slug']))
    img = Image.new('RGBA', (WIDTH, HEIGHT), C['bg'] + (255,))
    
    # Apply template
    TEMPLATES[article['template']](img, rng)
    
    # Apply gaussian blur for that smooth atmospheric feel
    img = img.filter(ImageFilter.GaussianBlur(radius=3))
    
    # Convert to RGB
    final = Image.new('RGB', (WIDTH, HEIGHT), C['bg'])
    final.paste(img, mask=img.split()[3])
    
    path = os.path.join(out_dir, f"{article['slug']}-hero.png")
    final.save(path, 'PNG', optimize=True)
    return path

def main():
    out = os.path.expanduser("~/bionic-banker/blog-visuals/png")
    os.makedirs(out, exist_ok=True)
    for a in ARTICLES:
        p = generate(a, out)
        print(f"  {a['slug']}")
    print(f"\nGenerated {len(ARTICLES)} atmospheric hero images")

if __name__ == '__main__':
    main()
