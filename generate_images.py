#!/usr/bin/env python3
"""Generate hero images for all Bionic Banker articles using Pillow."""

import math
import random
import hashlib
import os
from PIL import Image, ImageDraw, ImageFont

# Site color palette — green/black/white only
COLORS = {
    'bg': (2, 2, 4),           # #020204
    'green_dark': (13, 122, 74),   # #0d7a4a
    'green_mid': (31, 160, 104),   # #1fa068
    'green_bright': (52, 211, 153), # #34d399
    'green_light': (110, 231, 183), # #6ee7b7
    'green_pale': (167, 243, 208), # #a7f3d0
    'white': (228, 228, 236),      # #e4e4ec
    'dim': (80, 80, 96),           # muted text
}

WIDTH, HEIGHT = 1200, 630  # OG image standard

ARTICLES = [
    {"slug": "aml-engine", "title": "Building an AML Detection Engine", "tags": ["AML", "Python", "Compliance"], "template": "circuit"},
    {"slug": "nexus-agent", "title": "NEXUS Agent: AI Investigation System", "tags": ["AI Agent", "AML", "NLP"], "template": "network"},
    {"slug": "syos", "title": "SYOS: Symbolic Yielded Operating System", "tags": ["AI Safety", "LLM", "Research"], "template": "matrix"},
    {"slug": "syos-falsification", "title": "SYOS Falsification: Testing the Thesis", "tags": ["Testing", "AI", "Research"], "template": "grid"},
    {"slug": "anchor-problem", "title": "The Anchor Problem in AI", "tags": ["AI", "Philosophy", "LLM"], "template": "waves"},
    {"slug": "zkp-explained", "title": "Zero-Knowledge Proofs Explained", "tags": ["ZKP", "Cryptography", "Privacy"], "template": "blockchain"},
    {"slug": "tornado-cash", "title": "Tornado Cash: The Privacy Debate", "tags": ["Privacy", "DeFi", "Regulation"], "template": "circuit"},
    {"slug": "defi", "title": "DeFi: The Financial Revolution", "tags": ["DeFi", "Ethereum", "Finance"], "template": "blockchain"},
    {"slug": "aave", "title": "AAVE: Decentralized Lending Deep Dive", "tags": ["DeFi", "AAVE", "Lending"], "template": "network"},
    {"slug": "uniswap", "title": "Uniswap: The AMM That Changed DeFi", "tags": ["DeFi", "AMM", "Ethereum"], "template": "blockchain"},
    {"slug": "paypal", "title": "PayPal's Crypto Strategy", "tags": ["Crypto", "PayPal", "Payments"], "template": "waves"},
    {"slug": "extreme-fear", "title": "Extreme Fear: Crypto Market Psychology", "tags": ["Psychology", "Markets", "Crypto"], "template": "waves"},
    {"slug": "blockchain-trends", "title": "Blockchain Trends Reshaping Finance", "tags": ["Blockchain", "Finance", "Trends"], "template": "blockchain"},
    {"slug": "how-to-start-crypto", "title": "How to Start in Crypto", "tags": ["Crypto", "Beginner", "Guide"], "template": "grid"},
    {"slug": "gen-z-finance", "title": "Gen Z and the Future of Finance", "tags": ["Gen Z", "Finance", "Culture"], "template": "waves"},
    {"slug": "fintech", "title": "Fintech: Where Finance Meets Code", "tags": ["Fintech", "Innovation", "Banking"], "template": "circuit"},
    {"slug": "physics-of-ai", "title": "The Physics of AI", "tags": ["AI", "Physics", "Philosophy"], "template": "matrix"},
    {"slug": "ai-memory-system", "title": "Building AI Memory Systems", "tags": ["AI", "Memory", "Architecture"], "template": "network"},
    {"slug": "kill-agent", "title": "The Kill Agent: System Resilience", "tags": ["Security", "AI", "Systems"], "template": "circuit"},
    {"slug": "memory-case-study", "title": "Memory Architecture Case Study", "tags": ["AI", "Case Study", "Memory"], "template": "grid"},
    {"slug": "folder-agent", "title": "The Folder Agent: AI File Management", "tags": ["AI Agent", "Automation", "Files"], "template": "network"},
    {"slug": "folder-agent-part2", "title": "Folder Agent Part 2: Evolution", "tags": ["AI Agent", "Automation", "Evolution"], "template": "network"},
    {"slug": "the-anchor", "title": "The Anchor: Grounding AI Systems", "tags": ["AI", "Philosophy", "Design"], "template": "waves"},
    {"slug": "agent-evolution", "title": "Agent Evolution: From Rules to Reasoning", "tags": ["AI", "Agents", "Evolution"], "template": "matrix"},
    {"slug": "agent-replacement", "title": "When AI Agents Replace Workflows", "tags": ["AI", "Automation", "Future"], "template": "matrix"},
]

def seed_from_slug(slug):
    """Deterministic seed so same slug always produces same image."""
    return int(hashlib.md5(slug.encode()).hexdigest()[:8], 16)

def draw_circuit(draw, img, rng):
    """Circuit board pattern — traces, nodes, connection points."""
    for _ in range(40):
        x = rng.randint(0, WIDTH)
        y = rng.randint(0, HEIGHT)
        length = rng.randint(40, 200)
        horizontal = rng.random() > 0.5
        alpha = rng.randint(30, 90)
        color = (*COLORS['green_mid'], alpha)
        if horizontal:
            draw.line([(x, y), (x + length, y)], fill=color, width=1)
            draw.ellipse([x + length - 3, y - 3, x + length + 3, y + 3], fill=(*COLORS['green_bright'], alpha + 40))
        else:
            draw.line([(x, y), (x, y + length)], fill=color, width=1)
            draw.ellipse([x - 3, y + length - 3, x + 3, y + length + 3], fill=(*COLORS['green_bright'], alpha + 40))
    # Add larger junction nodes
    for _ in range(15):
        cx, cy = rng.randint(50, WIDTH-50), rng.randint(50, HEIGHT-50)
        r = rng.randint(4, 8)
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(*COLORS['green_dark'], 120), outline=(*COLORS['green_mid'], 160))

def draw_matrix(draw, img, rng):
    """Matrix rain / data stream pattern."""
    chars = "01アイウエオカキクケコサシスセソ∑∆∏∫√∞≈≠"
    try:
        font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 14)
    except:
        font_sm = ImageFont.load_default()
    for col in range(0, WIDTH, 22):
        length = rng.randint(5, 20)
        start_y = rng.randint(-100, HEIGHT - 50)
        for i in range(length):
            char = rng.choice(chars)
            y = start_y + i * 20
            if 0 <= y <= HEIGHT:
                brightness = max(0, 255 - i * 18)
                alpha = max(20, brightness)
                g = int(COLORS['green_bright'][1] * (brightness / 255))
                draw.text((col, y), char, fill=(0, g, int(g * 0.6), alpha), font=font_sm)

def draw_network(draw, img, rng):
    """Neural network / node-connection pattern."""
    nodes = [(rng.randint(50, WIDTH-50), rng.randint(50, HEIGHT-50)) for _ in range(25)]
    # Draw connections first
    for i, (x1, y1) in enumerate(nodes):
        for j, (x2, y2) in enumerate(nodes):
            if i < j:
                dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                if dist < 300:
                    alpha = int(max(10, 60 - dist * 0.2))
                    draw.line([(x1, y1), (x2, y2)], fill=(*COLORS['green_dark'], alpha), width=1)
    # Draw nodes
    for x, y in nodes:
        r = rng.randint(3, 10)
        glow_r = r + 8
        # Glow
        for gr in range(glow_r, r, -1):
            a = int(15 * (glow_r - gr) / (glow_r - r))
            draw.ellipse([x-gr, y-gr, x+gr, y+gr], fill=(*COLORS['green_mid'], a))
        draw.ellipse([x-r, y-r, x+r, y+r], fill=COLORS['green_bright'])

def draw_blockchain(draw, img, rng):
    """Blockchain / linked blocks pattern."""
    block_w, block_h = 80, 50
    rows = 3
    cols = 6
    margin_x = (WIDTH - cols * 140) // 2
    margin_y = (HEIGHT - rows * 100) // 2
    for row in range(rows):
        for col in range(cols):
            x = margin_x + col * 140 + rng.randint(-10, 10)
            y = margin_y + row * 100 + rng.randint(-10, 10)
            alpha = rng.randint(40, 100)
            # Block
            draw.rounded_rectangle([x, y, x+block_w, y+block_h], radius=6,
                                   outline=(*COLORS['green_mid'], alpha), width=1)
            # Inner hash lines
            for line_y in range(y + 12, y + block_h - 8, 10):
                lw = rng.randint(20, block_w - 20)
                draw.line([(x + 10, line_y), (x + 10 + lw, line_y)],
                         fill=(*COLORS['green_dark'], alpha - 10), width=1)
            # Chain link to next
            if col < cols - 1:
                nx = margin_x + (col + 1) * 140 + rng.randint(-10, 10)
                draw.line([(x + block_w, y + block_h // 2), (nx, y + block_h // 2 + rng.randint(-10, 10))],
                         fill=(*COLORS['green_mid'], 60), width=2)

def draw_waves(draw, img, rng):
    """Data wave / oscillation pattern."""
    for wave_i in range(6):
        points = []
        amplitude = rng.randint(30, 80)
        freq = rng.uniform(0.005, 0.015)
        offset_y = 80 + wave_i * 90
        phase = rng.uniform(0, math.pi * 2)
        for x in range(0, WIDTH, 3):
            y = offset_y + math.sin(x * freq + phase) * amplitude
            points.append((x, y))
        if len(points) > 1:
            alpha = 30 + wave_i * 12
            draw.line(points, fill=(*COLORS['green_mid'], alpha), width=2)

def draw_grid(draw, img, rng):
    """Tech grid / data visualization pattern."""
    cell = 40
    for x in range(0, WIDTH, cell):
        draw.line([(x, 0), (x, HEIGHT)], fill=(*COLORS['green_dark'], 25), width=1)
    for y in range(0, HEIGHT, cell):
        draw.line([(0, y), (WIDTH, y)], fill=(*COLORS['green_dark'], 25), width=1)
    # Data points at intersections
    for _ in range(50):
        gx = rng.randint(0, WIDTH // cell) * cell
        gy = rng.randint(0, HEIGHT // cell) * cell
        r = rng.randint(2, 6)
        alpha = rng.randint(40, 120)
        draw.ellipse([gx-r, gy-r, gx+r, gy+r], fill=(*COLORS['green_bright'], alpha))

TEMPLATE_MAP = {
    'circuit': draw_circuit,
    'matrix': draw_matrix,
    'network': draw_network,
    'blockchain': draw_blockchain,
    'waves': draw_waves,
    'grid': draw_grid,
}

def generate_article_image(article, output_dir):
    slug = article['slug']
    rng = random.Random(seed_from_slug(slug))
    
    # RGBA for alpha compositing
    img = Image.new('RGBA', (WIDTH, HEIGHT), COLORS['bg'] + (255,))
    overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Draw template pattern
    template_fn = TEMPLATE_MAP.get(article['template'], draw_grid)
    template_fn(draw, overlay, rng)
    
    img = Image.alpha_composite(img, overlay)
    
    # Add gradient overlay for text readability (bottom darker)
    gradient = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(gradient)
    for y in range(HEIGHT):
        # Bottom 60% gets progressively darker
        if y > HEIGHT * 0.4:
            progress = (y - HEIGHT * 0.4) / (HEIGHT * 0.6)
            alpha = int(progress * 200)
            gdraw.line([(0, y), (WIDTH, y)], fill=(2, 2, 4, alpha))
    img = Image.alpha_composite(img, gradient)
    
    # Text overlay
    text_layer = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(text_layer)
    
    # Load fonts
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
        font_tag = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        font_brand = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    except:
        font_title = ImageFont.load_default()
        font_tag = ImageFont.load_default()
        font_brand = ImageFont.load_default()
    
    # Title — word wrap
    title = article['title']
    words = title.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = tdraw.textbbox((0, 0), test, font=font_title)
        if bbox[2] > WIDTH - 120:
            lines.append(current)
            current = word
        else:
            current = test
    if current:
        lines.append(current)
    
    # Position title at bottom third
    title_y = HEIGHT - 80 - len(lines) * 52 - 40
    for i, line in enumerate(lines):
        tdraw.text((60, title_y + i * 52), line, fill=COLORS['white'] + (240,), font=font_title)
    
    # Tags
    tag_y = HEIGHT - 80
    tag_x = 60
    for tag in article['tags'][:3]:
        text = f"#{tag}"
        bbox = tdraw.textbbox((0, 0), text, font=font_tag)
        tw = bbox[2] - bbox[0]
        # Tag pill background
        tdraw.rounded_rectangle([tag_x - 4, tag_y - 2, tag_x + tw + 8, tag_y + 22], 
                                radius=4, fill=(*COLORS['green_dark'], 140))
        tdraw.text((tag_x, tag_y), text, fill=COLORS['green_light'] + (220,), font=font_tag)
        tag_x += tw + 20
    
    # Brand mark top-right
    tdraw.text((WIDTH - 220, 24), "bionicbanker.tech", fill=COLORS['green_mid'] + (140,), font=font_brand)
    
    # Green accent line
    tdraw.line([(60, title_y - 16), (200, title_y - 16)], fill=COLORS['green_bright'] + (180,), width=3)
    
    img = Image.alpha_composite(img, text_layer)
    
    # Convert to RGB for PNG save
    final = Image.new('RGB', (WIDTH, HEIGHT), COLORS['bg'])
    final.paste(img, mask=img.split()[3])
    
    out_path = os.path.join(output_dir, f"{slug}-hero.png")
    final.save(out_path, 'PNG', optimize=True)
    return out_path

def main():
    output_dir = os.path.expanduser("~/bionic-banker/blog-visuals/png")
    os.makedirs(output_dir, exist_ok=True)
    
    for article in ARTICLES:
        path = generate_article_image(article, output_dir)
        print(f"✅ {article['slug']}: {path}")
    
    print(f"\n🎯 Generated {len(ARTICLES)} hero images in {output_dir}")

if __name__ == '__main__':
    main()
