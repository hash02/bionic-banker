"""
Social Preview Image Generator - bionicbanker.tech
Generates 1200x630 social preview PNGs for articles missing custom visuals.
Uses Pillow — pip install Pillow
"""
import os, re, sys, io
from PIL import Image, ImageDraw, ImageFont

# Fix Windows console encoding (skip if already wrapped or on CI)
try:
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
except Exception:
    pass

BB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VISUALS = os.path.join(BB, "blog-visuals")
SKIP = {"index.html", "articles.html", "preview-layout.html", "agent-architecture.html", "dashboard_preview.html"}

# Design spec
WIDTH, HEIGHT = 1200, 630
BG_COLOR = (2, 2, 4)         # #020204
ACCENT_1 = (91, 115, 248)    # #5b73f8
ACCENT_2 = (139, 108, 247)   # #8b6cf7
TEXT_COLOR = (228, 228, 236)  # #e4e4ec
TAG_COLOR = (136, 136, 136)  # #888888
BRAND_COLOR = ACCENT_1


def get_system_font(size):
    """Try common system fonts, fall back to default."""
    candidates = [
        "arial.ttf", "Arial.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for font_path in candidates:
        try:
            return ImageFont.truetype(font_path, size)
        except (IOError, OSError):
            continue
    return ImageFont.load_default()


def get_bold_font(size):
    candidates = [
        "arialbd.ttf", "Arial Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for font_path in candidates:
        try:
            return ImageFont.truetype(font_path, size)
        except (IOError, OSError):
            continue
    return get_system_font(size)


def extract_article_info(html_path):
    """Extract title and tags from article HTML."""
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Title from <title> tag, strip " — Bionic Banker"
    title_m = re.search(r"<title>([^<]+)</title>", content)
    title = title_m.group(1).strip() if title_m else os.path.basename(html_path)
    title = re.sub(r"\s*[—–-]\s*Bionic Banker\s*$", "", title)

    # Tags from article-tag span
    tag_m = re.search(r'class="article-tag"[^>]*>([^<]+)<', content)
    tags = tag_m.group(1).strip() if tag_m else ""

    return title, tags


def wrap_text(text, font, max_width, draw):
    """Wrap text to fit within max_width, return list of lines."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines[:3]  # Max 3 lines


def draw_gradient_line(draw, y, width, height=3):
    """Draw a horizontal gradient line from ACCENT_1 to ACCENT_2."""
    for x in range(width):
        ratio = x / width
        r = int(ACCENT_1[0] + (ACCENT_2[0] - ACCENT_1[0]) * ratio)
        g = int(ACCENT_1[1] + (ACCENT_2[1] - ACCENT_1[1]) * ratio)
        b = int(ACCENT_1[2] + (ACCENT_2[2] - ACCENT_1[2]) * ratio)
        for dy in range(height):
            draw.point((x, y + dy), fill=(r, g, b))


def generate_preview(slug, title, tags, output_path):
    """Generate a social preview image."""
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    brand_font = get_system_font(20)
    title_font = get_bold_font(48)
    tag_font = get_system_font(22)

    # Gradient line at top
    draw_gradient_line(draw, 0, WIDTH, height=4)

    # Brand name top-left
    draw.text((60, 40), "BIONIC BANKER", fill=BRAND_COLOR, font=brand_font)

    # Title centered
    lines = wrap_text(title, title_font, WIDTH - 120, draw)
    total_height = len(lines) * 60
    start_y = (HEIGHT - total_height) // 2 - 20
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=title_font)
        line_w = bbox[2] - bbox[0]
        x = (WIDTH - line_w) // 2
        draw.text((x, start_y + i * 60), line, fill=TEXT_COLOR, font=title_font)

    # Tags at bottom center
    if tags:
        bbox = draw.textbbox((0, 0), tags, font=tag_font)
        tag_w = bbox[2] - bbox[0]
        draw.text(((WIDTH - tag_w) // 2, HEIGHT - 80), tags, fill=TAG_COLOR, font=tag_font)

    # Gradient line at bottom
    draw_gradient_line(draw, HEIGHT - 4, WIDTH, height=4)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")


def main():
    htmls = [f for f in os.listdir(BB) if f.endswith(".html") and f not in SKIP]
    generated = 0
    skipped = 0

    for f in sorted(htmls):
        slug = f.replace(".html", "")
        output_path = os.path.join(VISUALS, slug, "social-preview.png")

        # Skip if already exists
        if os.path.exists(output_path):
            print(f"  SKIP: {slug} (already has social-preview.png)")
            skipped += 1
            continue

        # Special case: aml-roaster has custom hero
        if slug == "aml-roaster":
            hero = os.path.join(VISUALS, "png", "01-hero-banner.png")
            if os.path.exists(hero):
                print(f"  SKIP: {slug} (has custom hero at blog-visuals/png/01-hero-banner.png)")
                skipped += 1
                continue

        title, tags = extract_article_info(os.path.join(BB, f))
        generate_preview(slug, title, tags, output_path)
        print(f"  GENERATED: {slug} — {output_path}")
        generated += 1

    print(f"\nDone: {generated} generated, {skipped} skipped")


if __name__ == "__main__":
    main()
