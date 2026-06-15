from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import json

OUT = Path('/home/hash/bionic-banker/social-assets/agentic-payments-stablecoin-control')
OUT.mkdir(parents=True, exist_ok=True)
W,H = 1240,1754  # A4-ish @ 150dpi
BG=(1,3,2); TEXT=(238,255,244); MUTED=(172,209,187); GREEN=(82,255,158); BORDER=(49,158,95); PANEL=(6,25,15); PANEL2=(9,39,24)
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
def f(s,b=False,m=False): return ImageFont.truetype(MONO if m else (BOLD if b else FONT), s)
def wrap(draw, text, font, width):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if draw.textbbox((0,0),t,font=font)[2] <= width: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def r(draw, box, fill=PANEL, outline=BORDER, width=2, radius=28): draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
img=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(img)
for x in range(0,W,80): d.line((x,0,x,H), fill=(5,28,16), width=1)
for y in range(0,H,80): d.line((0,y,W,y), fill=(5,28,16), width=1)
d.ellipse((860,-120,1320,340), outline=(25,118,70), width=3)
d.text((80,70),'BIONIC BANKER',fill=GREEN,font=f(28,True,True))
d.text((80,125),'AI Agent Payment Control',fill=TEXT,font=f(54,True))
d.text((80,185),'Checklist',fill=TEXT,font=f(54,True))
sub='Use this before an AI agent can spend stablecoins, pay for APIs, buy data, or trigger any machine-to-machine transaction.'
y=260
for line in wrap(d,sub,f(27),1020): d.text((82,y),line,fill=MUTED,font=f(27)); y+=40
r(d,(80,370,1160,540),PANEL2,BORDER,2,28)
d.text((115,405),'Core rule',fill=GREEN,font=f(28,True,True))
core='The chain can prove value moved. It cannot prove authority, delivery, or ledger fit.'
yy=450
for line in wrap(d, core, f(28, True), 980):
    d.text((115,yy),line,fill=TEXT,font=f(28,True)); yy+=36
sections=[
('01 Request record',['Original user/system request is stored','Resource, vendor, amount, token, chain, and purpose are captured','Prompt/instruction that triggered payment is replayable']),
('02 Authority rule',['Agent has written spend boundary','Per-payment and daily limits exist','Blocked vendors/resources/jurisdictions are explicit']),
('03 Payment proof',['Wallet address and signer are recorded','Transaction hash or payment receipt is stored','Stablecoin/chain/network fees are captured']),
('04 Delivery check',['What the agent received is stored','Service/data/API response matches what was requested','Failed or partial delivery triggers exception review']),
('05 Reconciliation',['Payment maps to internal ledger/category','Duplicate/retry payments are detected','Wallet and accounting records can be matched']),
('06 Human review',['Human approval is required for high-risk/unclear payments','Exception queue has an owner and SLA','Reviewer can replay request → rule → payment → delivery → audit'])
]
y=600
for idx,(title,items) in enumerate(sections):
    x=80 if idx%2==0 else 640
    if idx%2==0 and idx>0: y+=285
    r(d,(x,y,x+520,y+245),PANEL,BORDER,2,24)
    d.text((x+28,y+26),title,fill=GREEN,font=f(25,True,True))
    yy=y+73
    for item in items:
        d.rectangle((x+30,yy+5,x+52,yy+27), outline=GREEN, width=2)
        for line in wrap(d,item,f(20),420):
            d.text((x+68,yy),line,fill=TEXT,font=f(20)); yy+=29
        yy+=8
# footer
r(d,(80,1510,1160,1660),PANEL2,BORDER,2,28)
d.text((115,1540),'Decision',fill=GREEN,font=f(26,True,True))
decision='If any box is unclear, do not increase autonomy. Improve the receipt, review, and reconciliation layer first.'
yy=1585
for line in wrap(d, decision, f(26, True), 980):
    d.text((115,yy),line,fill=TEXT,font=f(26,True)); yy+=34
d.text((80,1695),'Educational checklist only. Not legal, tax, compliance, trading, or investment advice.',fill=MUTED,font=f(17))
d.text((820,1695),'bionicbanker.tech',fill=GREEN,font=f(20,True,True))
png=OUT/'ai-agent-payment-control-checklist.png'
pdf=OUT/'ai-agent-payment-control-checklist.pdf'
img.save(png, quality=95)
img.save(pdf, 'PDF', resolution=150.0)
(OUT/'checklist-manifest.json').write_text(json.dumps({'title':'AI Agent Payment Control Checklist','png':str(png),'pdf':str(pdf),'size':[W,H]}, indent=2))
print(png); print(pdf)
