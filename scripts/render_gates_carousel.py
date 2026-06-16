from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path('/home/hash/bionic-banker/social-assets/linkedin-ready/ai-agents-need-gates-not-vibes')
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1080, 1350
BG = (2, 7, 4)
GREEN = (126, 224, 170)
WHITE = (243, 255, 248)
MUTED = (190, 220, 205)
PANEL = (6, 20, 12)
LINE = (31, 160, 104)

font_paths = [
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
]
font_bold_paths = [
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf',
]

def fp(paths):
    for p in paths:
        if Path(p).exists(): return p
    return None
REG = fp(font_paths)
BOLD = fp(font_bold_paths) or REG

def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size)

def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines=[]; line=''
    for w in words:
        test=(line+' '+w).strip()
        if draw.textbbox((0,0), test, font=fnt)[2] <= max_width:
            line=test
        else:
            if line: lines.append(line)
            line=w
    if line: lines.append(line)
    return lines

def slide(num, kicker, title, body, footer='BIONIC BANKER'):
    img=Image.new('RGB',(W,H),BG)
    d=ImageDraw.Draw(img)
    # glow/grid
    for r, alpha in [(520,35),(360,25),(220,18)]:
        d.ellipse((-220,-180,r,r), fill=(3, 40, 22))
    for x in range(80,W,160):
        d.line((x, 0, x, H), fill=(8,25,15), width=1)
    for y in range(120,H,160):
        d.line((0, y, W, y), fill=(8,25,15), width=1)
    d.rounded_rectangle((58,58,W-58,H-58), radius=38, outline=(28,120,76), width=3)
    d.text((84,90), kicker.upper(), fill=GREEN, font=font(26, True))
    y=175
    for line in wrap(d,title,font(74,True),900):
        d.text((84,y), line, fill=WHITE, font=font(74,True))
        y+=88
    y+=30
    for line in wrap(d,body,font(40),890):
        d.text((84,y), line, fill=MUTED, font=font(40))
        y+=58
    d.text((84,H-135), footer, fill=GREEN, font=font(28,True))
    d.text((W-160,H-135), f'{num}/7', fill=(130,165,145), font=font(28,True))
    img.save(OUT / f'slide-{num:02d}.png', quality=95)

slides = [
('AI AGENTS', 'AI agents need gates, not vibes.', 'The useful demo is not that the agent answered. It is what the agent was allowed to do.'),
('THE QUESTION', 'Stop asking only: can it answer?', 'Ask: what can it touch, who approved it, what was blocked, and what record proves it?'),
('FINANCE REALITY', 'In finance, an output can become an action.', 'A payment, message, risk note, customer file, or portfolio change needs a gate before it becomes real.'),
('FOUR RECORDS', 'Every agent needs four records.', 'Request. Rule. Output. Review. Without those, nobody can replay the decision.'),
('THE PROOF', 'The blocked action matters.', 'A good system can say: the agent tried X, policy allowed Y, the gate blocked Z, and the reason was recorded.'),
('LOCAL PROOF', 'Governed agent workflow, tested locally.', 'Retrieval, safety eval, RBAC, audit rows, trace events, queue states, and external-action gates. 70 tests passed.'),
('TAKEAWAY', 'Autonomy without a gate is operational risk.', 'The next serious finance layer is not a smarter prompt. It is request → rule → tool → check → audit → human review.'),
]
for i, s in enumerate(slides,1): slide(i,*s)
# contact sheet
thumbs=[Image.open(OUT/f'slide-{i:02d}.png').resize((216,270)) for i in range(1,8)]
sheet=Image.new('RGB',(216*4,270*2),BG)
for idx,t in enumerate(thumbs): sheet.paste(t,((idx%4)*216,(idx//4)*270))
sheet.save(OUT/'contact-sheet.png')
print(OUT)
