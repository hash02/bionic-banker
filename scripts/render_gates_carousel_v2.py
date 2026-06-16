from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

OUT = Path('/home/hash/bionic-banker/social-assets/linkedin-ready/ai-agents-need-gates-not-vibes-v2')
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1080, 1350
BG = (2, 7, 4)
PANEL = (5, 18, 11)
PANEL2 = (8, 28, 17)
GREEN = (126, 224, 170)
GREEN2 = (31, 160, 104)
WHITE = (244, 255, 249)
MUTED = (196, 224, 210)
DIM = (110, 145, 125)
RED = (255, 114, 114)

REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

def f(size, bold=False, mono=False):
    return ImageFont.truetype(MONO if mono else (BOLD if bold else REG), size)

def draw_bg(d):
    d.rectangle((0,0,W,H), fill=BG)
    for x in range(60, W, 120): d.line((x, 0, x, H), fill=(5,22,13), width=1)
    for y in range(80, H, 120): d.line((0, y, W, y), fill=(5,22,13), width=1)
    d.rectangle((48,48,W-48,H-48), outline=(24,102,65), width=2)
    d.text((70,76), 'BIONIC BANKER / AI FINANCE CONTROL MAP', fill=GREEN, font=f(22, True))

def wrap(draw, text, font, width):
    words=text.split(); lines=[]; cur=''
    for w in words:
        test=(cur+' '+w).strip()
        if draw.textbbox((0,0), test, font=font)[2] <= width:
            cur=test
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def text_box(d, xy, wh, title, body, accent=GREEN2):
    x,y=xy; w,h=wh
    d.rounded_rectangle((x,y,x+w,y+h), radius=22, fill=PANEL, outline=accent, width=2)
    d.text((x+24,y+20), title.upper(), fill=GREEN, font=f(24, True))
    yy=y+62
    for line in wrap(d, body, f(28), w-48):
        d.text((x+24, yy), line, fill=MUTED, font=f(28))
        yy += 38

def pill(d, x, y, label, color=GREEN2):
    tw=d.textbbox((0,0), label, font=f(20, True))[2]
    d.rounded_rectangle((x,y,x+tw+28,y+34), radius=17, fill=(4,36,22), outline=color, width=1)
    d.text((x+14,y+7), label, fill=GREEN, font=f(20, True))

# Slide 1
img=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(img); draw_bg(d)
d.text((70,145), 'AI agents need', fill=WHITE, font=f(76, True))
d.text((70,230), 'gates, not vibes.', fill=WHITE, font=f(76, True))
d.text((74,325), 'The finance question is not “can it answer?”', fill=MUTED, font=f(34))
d.text((74,370), 'It is: what was it allowed to do when nobody was watching?', fill=MUTED, font=f(34))
labels=[('REQUEST','what was asked'),('RULE','what allowed it'),('TOOL','what it touched'),('OUTPUT','what changed'),('CHECK','what failed'),('AUDIT','what can be replayed')]
x0,y0=78,470
for i,(a,b) in enumerate(labels):
    x=x0+(i%2)*465; y=y0+(i//2)*145
    text_box(d,(x,y),(420,112),a,b)
d.rounded_rectangle((78,930,1002,1148), radius=26, fill=PANEL2, outline=GREEN2, width=2)
d.text((112,962),'The blocked action is the proof.', fill=WHITE, font=f(44, True))
for j,line in enumerate(['A useful system can say: the agent tried X, policy allowed Y,', 'the gate blocked Z, and the reason was recorded.']):
    d.text((112,1030+j*42), line, fill=MUTED, font=f(31))
d.text((78,1230),'local proof: retrieval • safety eval • RBAC • audit rows • traces • queue gates', fill=DIM, font=f(24))
d.text((925,1230),'1/3', fill=DIM, font=f(24, True))
img.save(OUT/'slide-01.png')

# Slide 2
img=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(img); draw_bg(d)
d.text((70,145),'What a finance agent', fill=WHITE, font=f(62, True))
d.text((70,218),'must leave behind', fill=WHITE, font=f(62, True))
d.text((74,305),'If nobody can replay the decision, nobody can supervise it.', fill=MUTED, font=f(32))
# table
x,y=78,390; rowh=125; col1=250; col2=640
d.rounded_rectangle((x,y,x+924,y+rowh*5+20), radius=24, fill=PANEL, outline=GREEN2, width=2)
d.text((x+28,y+24),'RECORD', fill=GREEN, font=f(24, True)); d.text((x+col1,y+24),'QUESTION IT ANSWERS', fill=GREEN, font=f(24, True))
rows=[('Request','What did the agent receive?'),('Rule','Which policy allowed or blocked action?'),('Output','What did the agent produce or change?'),('Review','Who checked before external action?'),('Exception','What was stopped, escalated, or logged?')]
for i,(a,b) in enumerate(rows):
    yy=y+76+i*rowh
    d.line((x+20,yy-16,x+904,yy-16), fill=(18,80,50), width=1)
    d.text((x+28,yy),a, fill=WHITE, font=f(34, True))
    for k,line in enumerate(wrap(d,b,f(30),600)):
        d.text((x+col1,yy+k*38), line, fill=MUTED, font=f(30))
# before after
d.rounded_rectangle((78,1060,495,1190), radius=22, fill=(24,8,8), outline=RED, width=2)
d.text((106,1088),'WEAK DEMO', fill=RED, font=f(24, True)); d.text((106,1130),'“the agent answered”', fill=WHITE, font=f(34, True))
d.rounded_rectangle((545,1060,1002,1190), radius=22, fill=PANEL2, outline=GREEN2, width=2)
d.text((573,1088),'CONTROL SYSTEM', fill=GREEN, font=f(24, True)); d.text((573,1130),'“the gate worked”', fill=WHITE, font=f(34, True))
d.text((925,1230),'2/3', fill=DIM, font=f(24, True))
img.save(OUT/'slide-02.png')

# Slide 3
img=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(img); draw_bg(d)
d.text((70,145),'The operating rule', fill=WHITE, font=f(68, True))
d.text((74,235),'More autonomy is not the goal. More accountable action is.', fill=MUTED, font=f(32))
items=[
('1','Draft locally before action'),('2','Cite the source or say missing'),('3','Check role + policy'),('4','Block external actions by default'),('5','Record the exception'),('6','Send high-risk work to human review'),('7','Update the ledger after publishing'),('8','Stop if duplicate, unclear, or unverified')]
for idx,(n,txt) in enumerate(items):
    x=78+(idx%2)*465; y=335+(idx//2)*135
    d.rounded_rectangle((x,y,x+420,y+96), radius=20, fill=PANEL, outline=(24,102,65), width=2)
    d.ellipse((x+24,y+25,x+70,y+71), fill=(4,36,22), outline=GREEN2, width=2)
    d.text((x+39,y+34), n, fill=GREEN, font=f(22, True))
    for k,line in enumerate(wrap(d,txt,f(27,True),310)):
        d.text((x+88,y+24+k*34), line, fill=WHITE if k==0 else MUTED, font=f(27, True))
d.rounded_rectangle((78,910,1002,1135), radius=26, fill=PANEL2, outline=GREEN2, width=2)
d.text((112,942),'Bionic version:', fill=GREEN, font=f(28, True))
for j,line in enumerate(['request → rule → tool → output → check → audit record → human review', 'That loop is boring in the right way. That is where trust starts.']):
    d.text((112,995+j*48), line, fill=WHITE if j==0 else MUTED, font=f(30 if j else 27, True if j==0 else False))
d.text((78,1215),'Full note: bionicbanker.tech/blog/ai-agents-need-gates-not-vibes/', fill=DIM, font=f(24))
d.text((925,1215),'3/3', fill=DIM, font=f(24, True))
img.save(OUT/'slide-03.png')

# contact sheet
thumbs=[Image.open(OUT/f'slide-{i:02d}.png').resize((270,337)) for i in range(1,4)]
sheet=Image.new('RGB',(810,337),BG)
for i,t in enumerate(thumbs): sheet.paste(t,(i*270,0))
sheet.save(OUT/'contact-sheet.png')
print(OUT)
