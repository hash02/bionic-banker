from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import math

W, H = 2160, 2700
BG = '#020604'
GREEN = '#2ef29a'
GREEN_SOFT = '#77ffc0'
RED = '#ff5c7a'
WHITE = '#f4fff9'
MUTED = '#b9d7c8'
GRID = '#0d4a31'

img = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(img)


def font(size, bold=False, mono=False):
    if mono:
        p = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
    else:
        p = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    return ImageFont.truetype(p, size)


F_kicker = font(34, mono=True)
F_brand = font(28, mono=True)
F_title = font(120, True)
F_sub = font(50)
F_label = font(30, mono=True)
F_card_title = font(54, True)
F_card_body = font(38)
F_context_title = font(54, True)
F_context_body = font(40)
F_gate_title = font(32, True)
F_gate_body = font(31)
F_take = font(52, True)
F_url = font(42, mono=True)

# Background grid: finer + low-contrast, with stronger safe margins.
for x in range(0, W, 180):
    d.line((x, 0, x, H), fill=GRID, width=2)
for y in range(0, H, 180):
    d.line((0, y, W, y), fill=GRID, width=2)
for x in range(0, W, 90):
    d.line((x, 0, x, H), fill='#062417', width=1)
for y in range(0, H, 90):
    d.line((0, y, W, y), fill='#062417', width=1)

# Atmospheric glow + subtle arc shape.
for r, alpha in [(950, 18), (680, 24), (440, 30)]:
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse((120-r, 40-r, 120+r, 40+r), fill=(31, 160, 104, alpha))
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

d = ImageDraw.Draw(img)


def tw(text, f):
    box = d.textbbox((0, 0), text, font=f)
    return box[2] - box[0]


def wrap(text, f, maxw):
    words = text.split()
    lines, cur = [], ''
    for w in words:
        test = (cur + ' ' + w).strip()
        if tw(test, f) <= maxw:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def tb(x, y, text, f, fill, maxw, leading=1.18):
    for line in wrap(text, f, maxw):
        d.text((x, y), line, font=f, fill=fill)
        y += int(f.size * leading)
    return y


def glow_round(xy, fill, outline, width=4, radius=44, glow=None):
    if glow:
        layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        ld.rounded_rectangle(xy, radius=radius, outline=glow, width=10)
        blurred = layer.filter(ImageFilter.GaussianBlur(10))
        global img, d
        img = Image.alpha_composite(img.convert('RGBA'), blurred).convert('RGB')
        d = ImageDraw.Draw(img)
    d.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def arrow(x1, y1, x2, y2, color, width=10):
    d.line((x1, y1, x2, y2), fill=color, width=width)
    ang = math.atan2(y2 - y1, x2 - x1)
    L = 40
    d.polygon([
        (x2, y2),
        (x2 - L * math.cos(ang - math.pi / 7), y2 - L * math.sin(ang - math.pi / 7)),
        (x2 - L * math.cos(ang + math.pi / 7), y2 - L * math.sin(ang + math.pi / 7)),
    ], fill=color)


# Header
left, right = 150, 2010
d.text((left, 145), 'PROMPT INJECTION', font=F_kicker, fill=GREEN)
d.text((1470, 150), 'BIONIC BANKER / AI SECURITY', font=F_brand, fill='#9ebdab')

# Title block: slightly tighter, more intentional, more breathing above diagram.
y = 230
for line in ['AI can be hacked', 'through instructions.']:
    d.text((left, y), line, font=F_title, fill=WHITE)
    y += 126

tb(left, 515, 'The risk is untrusted text crossing into trusted instruction, tool, or approval space.', F_sub, '#cfe7d9', 1660, 1.15)

# Diagram layout: bigger cards, cleaner alignment, no cramped gate text.
trusted = (150, 760, 805, 1125)
untrusted = (150, 1360, 805, 1760)
context = (930, 1015, 1545, 1515)
gates = (1640, 760, 2025, 1760)

glow_round(trusted, '#062014', GREEN, 5, 36, (46, 242, 154, 72))
glow_round(untrusted, '#21070d', RED, 5, 36, (255, 92, 122, 58))
glow_round(context, '#06160f', GREEN_SOFT, 6, 38, (119, 255, 192, 64))
glow_round(gates, '#06160f', GREEN, 5, 36, (46, 242, 154, 54))

# Card text positions improved: labels up, body has bigger line length.
d.text((205, 825), 'TRUSTED', font=F_label, fill=GREEN)
d.text((205, 898), 'System rules', font=F_card_title, fill=WHITE)
tb(205, 985, 'Policy, role, tool limits, approvals.', F_card_body, '#d5efe2', 520, 1.16)

d.text((205, 1428), 'UNTRUSTED', font=F_label, fill='#ff7890')
d.text((205, 1502), 'Hidden instruction', font=F_card_title, fill='#fff4f6')
tb(205, 1594, 'Email, PDF, web page, retrieved note, tool result.', F_card_body, '#ffd6dd', 520, 1.16)

d.text((995, 1085), 'MODEL CONTEXT', font=F_label, fill=GREEN_SOFT)
d.text((995, 1180), 'What the AI sees', font=F_context_title, fill=WHITE)
tb(995, 1282, 'The model needs a boundary between evidence and commands.', F_context_body, '#d5efe2', 455, 1.13)

# Control gates: more vertical rhythm; no tiny words jammed against border.
d.text((1695, 835), 'CONTROL GATES', font=F_label, fill=GREEN)
gates_text = [
    ('1', 'Label source', 'Data is not instruction.'),
    ('2', 'Restrict tools', 'No secret or action by default.'),
    ('3', 'Log review', 'Request, source, tool, outcome.'),
]
y = 970
for n, title, body in gates_text:
    d.ellipse((1695, y, 1778, y + 83), fill=GREEN)
    d.text((1722, y + 14), n, font=font(42, True), fill='#031008')
    d.text((1795, y + 6), title, font=F_gate_title, fill='#eafff4')
    tb(1795, y + 62, body, F_gate_body, MUTED, 185, 1.08)
    y += 252

# Arrows drawn after cards for crisp heads, aligned to centers.
arrow(805, 935, 930, 1180, GREEN)
arrow(805, 1560, 930, 1390, RED)
arrow(1545, 1265, 1640, 1265, GREEN)

# Add subtle labels near arrows so the concept is readable at phone size.
d.text((835, 880), 'rules', font=font(26, mono=True), fill='#7cfac4')
d.text((830, 1602), 'payload', font=font(26, mono=True), fill='#ff8aa0')
d.text((1568, 1214), 'gate', font=font(26, mono=True), fill='#7cfac4')

# Footer: move up and widen text; remove huge dead lower third.
d.line((left, 2200, right, 2200), fill='#1c6b47', width=2)
d.text((left, 2278), 'bionicbanker.tech', font=F_url, fill=GREEN)
tb(720, 2258, 'If you cannot trace what the AI saw, trusted, called, and approved, do not trust it with sensitive work.', F_take, WHITE, 1220, 1.12)

# Thin bottom rule to make crop feel intentional.
d.line((left, 2525, right, 2525), fill='#0f5135', width=2)
d.text((left, 2575), 'CONTROL MAP / DEFENSIVE AI SECURITY LITERACY', font=font(28, mono=True), fill='#628f79')

out = Path('/home/hash/bionic-banker/social-assets/linkedin-ready/ai-prompt-injection-control-failure/prompt-injection-single-slide.png')
img.save(out, quality=98, subsampling=0)
print(out, img.size)
