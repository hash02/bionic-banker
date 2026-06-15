from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import textwrap, json, math

OUT = Path('/home/hash/bionic-banker/social-assets/agentic-payments-stablecoin-control')
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1080, 1350
BG = (1, 3, 2)
GREEN = (80, 255, 155)
GREEN2 = (31, 160, 104)
TEXT = (237, 255, 244)
MUTED = (165, 205, 181)
DIM = (72, 105, 86)
PANEL = (5, 22, 13)
PANEL2 = (8, 38, 23)
BORDER = (54, 154, 96)

FONT_REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

def font(size, bold=False, mono=False):
    return ImageFont.truetype(FONT_MONO if mono else (FONT_BOLD if bold else FONT_REG), size)

def wrap(draw, text, f, maxw):
    words = text.split()
    lines=[]; cur=''
    for w in words:
        test=(cur+' '+w).strip()
        if draw.textbbox((0,0), test, font=f)[2] <= maxw:
            cur=test
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def rounded(draw, box, fill, outline=None, width=2, radius=28):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def add_grid(draw):
    for x in range(0, W, 90):
        draw.line((x,0,x,H), fill=(6,32,18), width=1)
    for y in range(0, H, 90):
        draw.line((0,y,W,y), fill=(6,32,18), width=1)
    # curves
    for i in range(5):
        pts=[]
        for x in range(-50,W+60,30):
            y=220+i*190+math.sin((x+i*55)/110)*32
            pts.append((x,y))
        draw.line(pts, fill=(14,70,38), width=2)

def badge(draw, x, y, label, active=True):
    f=font(24, bold=True, mono=True)
    pad=18
    tw=draw.textbbox((0,0), label, font=f)[2]
    rounded(draw, (x,y,x+tw+pad*2,y+50), fill=(4,28,15) if active else (10,16,13), outline=(60,180,110) if active else (55,80,65), width=2, radius=25)
    draw.text((x+pad,y+12), label, fill=GREEN if active else MUTED, font=f)
    return x+tw+pad*2

def title(draw, s, y=155, size=68):
    f=font(size, bold=True)
    lines=wrap(draw,s,f,930)
    yy=y
    for line in lines:
        draw.text((70,yy), line, fill=TEXT, font=f)
        yy += int(size*1.08)
    return yy

def subtitle(draw, s, y, size=32):
    f=font(size)
    lines=wrap(draw,s,f,900)
    yy=y
    for line in lines:
        draw.text((72,yy), line, fill=MUTED, font=f)
        yy += int(size*1.36)
    return yy

def footer(draw, n):
    draw.text((70,1265), 'BIONIC BANKER', fill=GREEN, font=font(24,bold=True,mono=True))
    draw.text((850,1265), f'{n}/7', fill=MUTED, font=font(24,bold=True,mono=True))
    draw.line((70,1238,1010,1238), fill=(38,120,76), width=2)

def base(n):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    add_grid(d)
    d.ellipse((790,-150,1220,280), outline=(30,120,75), width=3)
    d.ellipse((-180,940,250,1380), outline=(18,95,56), width=3)
    footer(d,n)
    return im,d

slides=[]
# 1 cover
im,d=base(1)
badge(d,70,70,'AI AGENTS',True); badge(d,250,70,'STABLECOINS',True); badge(d,485,70,'PAYMENTS',True)
y=title(d,'Stablecoins are becoming machine payment rails.',150,66)
subtitle(d,'The serious question is not whether agents can pay. It is whether finance can explain the payment after it happens.', y+28, 34)
rounded(d,(70,820,1010,1080),PANEL2,BORDER,2,34)
d.text((110,865),'Bionic read',fill=GREEN,font=font(30,bold=True,mono=True))
d.text((110,920),'Speed is not the control layer.',fill=TEXT,font=font(48,bold=True))
d.text((110,992),'Receipts, delivery checks, reconciliation, and review are.',fill=MUTED,font=font(30))
slides.append(im)
# 2 why now
im,d=base(2); badge(d,70,70,'WHY NOW',True)
y=title(d,'The signal: small payments at machine scale.',155,58)
items=[('$73M+','settled by AI agents onchain'),('176M','transactions analyzed'),('$0.31–$0.48','average transaction size'),('98.6%','reported using USDC')]
for i,(num,cap) in enumerate(items):
    x=90+(i%2)*485; yy=470+(i//2)*245
    rounded(d,(x,yy,x+420,yy+170),PANEL2,BORDER,2,28)
    d.text((x+35,yy+32),num,fill=GREEN,font=font(56,bold=True))
    for j,line in enumerate(wrap(d,cap,font(27),340)):
        d.text((x+35,yy+105+j*35),line,fill=MUTED,font=font(27))
subtitle(d,'Source trail: Keyrock report summarized by FinanceFeeds. Treat the figures as a market signal, not proof of production maturity.',1005,26)
slides.append(im)
# 3 problem
im,d=base(3); badge(d,70,70,'THE GAP',True)
y=title(d,'The chain can prove value moved.',165,62)
subtitle(d,'It cannot prove the agent had authority, the vendor delivered, or the payment belongs in the ledger.', y+30, 36)
for i,text in enumerate(['authority','delivery','ledger fit']):
    x=120+i*300; yy=800
    d.ellipse((x,yy,x+180,yy+180), fill=(5,27,16), outline=BORDER, width=3)
    d.text((x+42,yy+62),'?',fill=GREEN,font=font(72,bold=True,mono=True))
    d.text((x-10,yy+215),text.upper(),fill=MUTED,font=font(25,bold=True,mono=True))
slides.append(im)
# 4 stack
im,d=base(4); badge(d,70,70,'CONTROL STACK',True)
title(d,'Before an agent pays, map the control stack.',150,54)
steps=['Request','Rule','Payment','Receipt','Delivery','Audit']
desc=['What did it ask for?','Was spend authorized?','Wallet, token, chain','Proof returned','Service received?','Human can replay']
for i,s in enumerate(steps):
    x=80+(i%2)*500; y=390+(i//2)*210
    rounded(d,(x,y,x+440,y+145),PANEL2,BORDER,2,24)
    d.text((x+25,y+22),f'{i+1:02d} {s}',fill=GREEN,font=font(30,bold=True,mono=True))
    d.text((x+25,y+80),desc[i],fill=TEXT,font=font(31,bold=True))
slides.append(im)
# 5 checklist
im,d=base(5); badge(d,70,70,'CHECKLIST',True)
title(d,'Seven questions before machine payments scale.',150,52)
qs=['What did the agent request?','Which rule approved the spend?','Which wallet/token/chain was used?','What proof shows payment happened?','What proof shows delivery happened?','What catches mismatches?','Can a reviewer replay the record?']
y=385
for i,q in enumerate(qs):
    rounded(d,(85,y,995,y+86),(4,25,15),BORDER,1,18)
    d.text((115,y+24),f'{i+1}',fill=GREEN,font=font(28,bold=True,mono=True))
    d.text((170,y+24),q,fill=TEXT,font=font(30,bold=True))
    y+=100
slides.append(im)
# 6 source card
im,d=base(6); badge(d,70,70,'SOURCE TRAIL',True)
title(d,'Do not treat this as a price story.',150,58)
subtitle(d,'This is a control-system story for AI, finance, and stablecoin infrastructure.', y:=330, 34)
rounded(d,(90,560,990,990),PANEL2,BORDER,2,30)
lines=['FinanceFeeds → Keyrock / Who Pays the Agent?','Coinbase x402 → HTTP-native payment flow','Chainalysis → x402 adoption context','Bionic Banker → receipt + review control map']
for i,line in enumerate(lines):
    d.text((135,610+i*86),'◆',fill=GREEN,font=font(32,bold=True))
    d.text((185,612+i*86),line,fill=TEXT,font=font(30,bold=True))
d.text((135,930),'Boundary: educational commentary. No trading advice. No compliance approval.',fill=MUTED,font=font(24))
slides.append(im)
# 7 CTA
im,d=base(7); badge(d,70,70,'TAKEAWAY',True)
y=title(d,'The next payment layer needs receipts, not just rails.',160,62)
subtitle(d,'Stablecoins can make machine payments cheaper. Finance still needs authority, delivery proof, reconciliation, exception review, and audit.', y+30, 34)
rounded(d,(90,840,990,1055),PANEL2,BORDER,2,30)
d.text((135,900),'Read the full Bionic Banker note:',fill=GREEN,font=font(28,bold=True,mono=True))
d.text((135,960),'bionicbanker.tech/blog/agentic-payments-receipt-layer/',fill=TEXT,font=font(28,bold=True))
slides.append(im)

paths=[]
for i,im in enumerate(slides,1):
    p=OUT/f'slide-{i:02d}.png'
    im.save(p, quality=95)
    paths.append(p)
# contact sheet
thumbs=[]
for p in paths:
    im=Image.open(p).resize((216,270))
    thumbs.append(im)
sheet=Image.new('RGB',(216*4,270*2+40),(2,8,5));
for idx,im in enumerate(thumbs):
    x=(idx%4)*216; y=(idx//4)*270
    sheet.paste(im,(x,y))
sheet.save(OUT/'contact-sheet.png')
# PDF from images
imgs=[Image.open(p).convert('RGB') for p in paths]
imgs[0].save(OUT/'agentic-payments-stablecoin-control-carousel.pdf', save_all=True, append_images=imgs[1:])
(OUT/'qa.json').write_text(json.dumps({'slides':len(paths),'size':[W,H],'files':[str(p) for p in paths]},indent=2))
print('\n'.join(str(p) for p in paths))
print(OUT/'contact-sheet.png')
print(OUT/'agentic-payments-stablecoin-control-carousel.pdf')