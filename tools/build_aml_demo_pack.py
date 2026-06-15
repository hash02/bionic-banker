from pathlib import Path
import csv, json, shutil, textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path('/home/hash/bionic-banker')
SRC = Path('/home/hash/aml-detection-engine')
OUT = ROOT / '_astro-source' / 'public' / 'downloads' / 'aml-demo-pack'
SOC = ROOT / '_astro-source' / 'public' / 'blog-visuals' / 'aml-engine-lab'
OUT.mkdir(parents=True, exist_ok=True)
SOC.mkdir(parents=True, exist_ok=True)

metrics = json.loads((SRC/'output_v11/metrics_v7.json').read_text())
rows=[]
with (SRC/'output_v11/scored_transactions_v7.csv').open() as f:
    reader=csv.DictReader(f)
    for i,row in enumerate(reader):
        if i>=8: break
        rows.append({k: row.get(k,'') for k in ['sender_id','receiver_id','amount','country','label','risk_score','reasons','alert']})

(OUT/'sample-output.json').write_text(json.dumps({'metrics':metrics,'sample_alerts':rows},indent=2))
with (OUT/'sample-input.csv').open('w',newline='') as f:
    w=csv.DictWriter(f, fieldnames=['sender_id','receiver_id','amount','country','timestamp','label'])
    w.writeheader()
    for r in rows[:5]:
        w.writerow({k:r.get(k,'') for k in w.fieldnames})

(OUT/'limitations.md').write_text('''# AML Review Engine Demo Pack — Limitations\n\n- Research and demonstration material only.\n- Not legal, regulatory, tax, compliance, trading, investment, KYC, or law-enforcement advice.\n- Public chain signals do not prove private identity or intent by themselves.\n- A risk score is a triage signal, not a final verdict.\n- The demo does not file reports, freeze funds, approve customers, or move assets.\n- Any production use would need governance, validation, data-quality review, access control, logging, and human approval.\n''')

(OUT/'README.md').write_text(f'''# AML Review Engine Demo Pack\n\nThis pack supports the Bionic Banker AML Review Engine Lab.\n\n## What is inside\n\n- `sample-input.csv` — small redacted-style sample input shape.\n- `sample-output.json` — metrics and sample scored rows from the local Wukong run.\n- `risk-memo-sample.md` — analyst-style memo explaining one review scenario.\n- `control-map.png` — visual workflow map.\n- `limitations.md` — boundaries and non-claims.\n\n## Verification snapshot\n\n- Local tests: 46 passing.\n- Demo run version: `{metrics.get('version')}`.\n- Demo total transactions: `{metrics.get('total_tx')}`.\n- Demo flagged transactions: `{metrics.get('flagged')}`.\n- Risk levels: `{metrics.get('risk_levels')}`.\n\n## Control doctrine\n\nThe useful output is not only the risk score. The useful output is the control layer around it:\n\n```text\nactivity → rules → anomaly signals → triage → evidence note → human review\n```\n\nNo autonomous enforcement or wallet authority is included.\n''')

memo = f'''# AML Risk Memo Sample\n\n## Scenario\n\nA sample review queue contains transactions with mixer-touch, high-risk-jurisdiction, burst, and large-amount indicators.\n\n## Local demo metrics\n\n- Total transactions reviewed: {metrics.get('total_tx')}\n- Flagged transactions: {metrics.get('flagged')}\n- Flag rate: {metrics.get('flag_rate_pct')}%\n- Risk levels: {metrics.get('risk_levels')}\n\n## Analyst interpretation\n\nThe engine should be treated as a triage assistant. It can highlight rows that deserve review, explain the rules that fired, and preserve a source/evidence note. It should not decide intent, identity, enforcement action, account closure, SAR filing, or customer outcome.\n\n## Human review questions\n\n1. Which source record supports each rule hit?\n2. Is the wallet/entity context complete enough to escalate?\n3. Is the alert caused by a known benign pattern?\n4. What evidence is missing?\n5. What is the next allowed action under policy?\n\n## Decision boundary\n\nEscalate for human review. Do not treat the score as a final verdict.\n'''
(OUT/'risk-memo-sample.md').write_text(memo)

W,H=1600,900
img=Image.new('RGB',(W,H),'#010302')
d=ImageDraw.Draw(img)
def font(size,bold=False):
    paths=['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
    return ImageFont.truetype(paths[0],size)
GREEN='#7ee0aa'; TEXT='#edf7f0'; MUTED='#a7b5ad'; PANEL='#07140d'; BORDER='#1fa068'
d.rectangle([0,0,W,H],fill='#010302')
d.text((70,60),'BIONIC LAB 01',fill=GREEN,font=font(24,True))
d.text((70,100),'AML Review Engine Control Map',fill=TEXT,font=font(58,True))
d.text((72,172),'A risk score is not the product. The product is the reviewable control trail around it.',fill=MUTED,font=font(28))
steps=[('01','Wallet activity','sample transaction rows'),('02','Rules','mixer / OFAC / burst / amount'),('03','Anomaly layer','unusual graph or flow pattern'),('04','Triage','priority label + risk score'),('05','Evidence note','source, reason, missing context'),('06','Human review','approve next step, not verdict')]
x0,y0=70,280; cardw,cardh=455,135; gapx,gapy=45,40
for i,(n,t,s) in enumerate(steps):
    col=i%3; row=i//3
    x=x0+col*(cardw+gapx); y=y0+row*(cardh+gapy)
    d.rounded_rectangle([x,y,x+cardw,y+cardh],radius=24,fill=PANEL,outline=BORDER,width=2)
    d.text((x+25,y+22),n,fill=GREEN,font=font(24,True))
    d.text((x+82,y+20),t,fill=TEXT,font=font(30,True))
    d.text((x+82,y+67),s,fill=MUTED,font=font(22))
    if i<5:
        ax=x+cardw+10 if col<2 else x0+cardw//2
        ay=y+cardh//2 if col<2 else y+cardh+20
        if col<2:
            d.line([x+cardw,y+cardh//2,x+cardw+gapx-8,y+cardh//2],fill=GREEN,width=3)
            d.polygon([(x+cardw+gapx-8,y+cardh//2),(x+cardw+gapx-25,y+cardh//2-9),(x+cardw+gapx-25,y+cardh//2+9)],fill=GREEN)

d.rounded_rectangle([70,700,1530,830],radius=26,fill='#041009',outline='#31463a',width=2)
d.text((105,730),'Boundary',fill=GREEN,font=font(24,True))
boundary='The system can surface and explain risk. It cannot identify intent, file reports, freeze funds, or make final compliance decisions.'
words=boundary.split(); lines=[]; cur=''
for w in words:
    test=(cur+' '+w).strip()
    if d.textlength(test,font=font(25))>1350:
        lines.append(cur); cur=w
    else:
        cur=test
if cur: lines.append(cur)
for j,line in enumerate(lines[:2]):
    d.text((105,770+j*32),line,fill=TEXT,font=font(25))
img.save(SOC/'aml-control-map.png')
img.save(OUT/'control-map.png')
# simple PDF from image + memo page image
img.convert('RGB').save(OUT/'aml-demo-pack-summary.pdf')
print('built', OUT)
