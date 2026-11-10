#!/usr/bin/env python3
"""Infographic for the guide 'Banks vs personal AI agents: the full guide'.
1200x630 social/hero image, site palette (black, green, white), exact text.
Output: _astro-source/public/blog-visuals/banks-vs-personal-ai-agents/three-questions-test.png
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
BG = (8, 12, 9)
GREEN = (46, 230, 107)
WHITE = (240, 244, 240)
DIM = (170, 182, 172)
CARD = (16, 24, 18)
LINE = (38, 60, 42)

FD = "/usr/share/fonts/truetype/dejavu/"
def f(name, size):
    return ImageFont.truetype(FD + name, size)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# top rule and kicker
d.rectangle([0, 0, W, 6], fill=GREEN)
d.text((64, 44), "BANKS VS PERSONAL AI AGENTS: THE FULL GUIDE", font=f("DejaVuSans-Bold.ttf", 25), fill=GREEN)
d.text((64, 84), "The three questions test", font=f("DejaVuSans-Bold.ttf", 54), fill=WHITE)
d.text((64, 152), "Ask these before any AI tool touches your money.", font=f("DejaVuSans.ttf", 27), fill=DIM)

questions = [
    ("1", "Can the bank tell the agent from you?",
     "If it signs in with your password, every action looks like yours."),
    ("2", "Is the agent's permission limited, and can you take it back?",
     "Scoped access you can revoke beats a login that opens everything."),
    ("3", "When money moves, does a person approve it first?",
     "The safe tools prepare the move. A person says yes before it goes."),
]

y = 216
for num, q, sub in questions:
    d.rounded_rectangle([64, y, W - 64, y + 104], radius=14, fill=CARD, outline=LINE, width=2)
    d.ellipse([88, y + 24, 144, y + 80], fill=GREEN)
    tw = d.textlength(num, font=f("DejaVuSans-Bold.ttf", 30))
    d.text((116 - tw / 2, y + 36), num, font=f("DejaVuSans-Bold.ttf", 30), fill=(8, 12, 9))
    d.text((168, y + 18), q, font=f("DejaVuSans-Bold.ttf", 27), fill=WHITE)
    d.text((168, y + 58), sub, font=f("DejaVuSans.ttf", 22), fill=DIM)
    y += 122

d.text((64, y + 6), "bionicbanker.tech", font=f("DejaVuSans-Bold.ttf", 22), fill=GREEN)
right = "By Hash"
tw = d.textlength(right, font=f("DejaVuSans.ttf", 22))
d.text((W - 64 - tw, y + 6), right, font=f("DejaVuSans.ttf", 22), fill=DIM)

out = os.path.expanduser("~/workspace/bionic-banker-publish/_astro-source/public/blog-visuals/banks-vs-personal-ai-agents/three-questions-test.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
img.save(out, "PNG")
print("wrote", out, os.path.getsize(out), "bytes")
