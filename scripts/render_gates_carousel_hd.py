from pathlib import Path
import subprocess

OUT = Path('/home/hash/bionic-banker/social-assets/linkedin-ready/ai-agents-need-gates-not-vibes-hd')
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1080, 1350

BASE_CSS = r'''
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700;800;900&display=swap');
*{box-sizing:border-box} body{margin:0;background:#020704;font-family:Inter,Arial,sans-serif;color:#f4fff9}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#020704;padding:64px 70px;border:0}
.slide:before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(126,224,170,.06) 1px,transparent 1px),linear-gradient(0deg,rgba(126,224,170,.06) 1px,transparent 1px);background-size:120px 120px;opacity:.8}
.slide:after{content:"";position:absolute;inset:46px;border:2px solid rgba(31,160,104,.75);border-radius:0;pointer-events:none}
.content{position:relative;z-index:2}.kicker{font-size:22px;font-weight:900;letter-spacing:.16em;color:#7ee0aa;margin-bottom:48px}.title{font-size:78px;line-height:1.02;font-weight:900;letter-spacing:-.055em;margin:0 0 26px}.subtitle{font-size:34px;line-height:1.32;color:#c8e4d4;max-width:900px;margin:0 0 42px}.grid2{display:grid;grid-template-columns:1fr 1fr;gap:22px 26px}.panel{background:#06140c;border:2px solid rgba(31,160,104,.9);border-radius:24px;padding:23px 25px;min-height:120px;box-shadow:0 0 0 1px rgba(126,224,170,.07) inset}.label{font-size:21px;font-weight:900;letter-spacing:.08em;color:#7ee0aa;margin-bottom:11px}.ptext{font-size:29px;line-height:1.2;color:#f4fff9;font-weight:700}.callout{margin-top:34px;background:#081c11;border:2px solid rgba(126,224,170,.85);border-radius:28px;padding:28px 34px}.callout h2{font-size:44px;letter-spacing:-.03em;margin:0 0 16px}.callout p{font-size:30px;line-height:1.35;color:#c8e4d4;margin:0}.footer{position:absolute;left:70px;right:70px;bottom:74px;color:#81a08d;font-size:23px;font-weight:700}.num{position:absolute;right:70px;bottom:74px;color:#81a08d;font-size:24px;font-weight:900}.table{margin-top:48px;border:2px solid rgba(31,160,104,.9);border-radius:28px;overflow:hidden;background:#06140c}.row{display:grid;grid-template-columns:240px 1fr;border-top:1px solid rgba(126,224,170,.22)}.row:first-child{border-top:0}.head{background:#092416}.cell{padding:22px 26px;font-size:29px;line-height:1.25}.head .cell{font-size:22px;text-transform:uppercase;letter-spacing:.1em;font-weight:900;color:#7ee0aa}.record{font-weight:900;color:#fff}.smallpair{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:38px}.bad{border-color:#ff7272;background:#180808}.bad .label{color:#ff7272}.checkgrid{display:grid;grid-template-columns:1fr 1fr;gap:21px 25px;margin-top:42px}.check{display:grid;grid-template-columns:54px 1fr;gap:18px;align-items:start;background:#06140c;border:2px solid rgba(31,160,104,.72);border-radius:22px;padding:22px}.badge{width:48px;height:48px;border:2px solid #1fa068;border-radius:999px;display:flex;align-items:center;justify-content:center;color:#7ee0aa;font-weight:900;font-size:22px;background:#042416}.check p{margin:0;color:#f4fff9;font-weight:800;font-size:26px;line-height:1.18}.rule{margin-top:32px;background:#081c11;border:2px solid #7ee0aa;border-radius:28px;padding:28px 34px}.rule .mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:25px;line-height:1.35;color:#f4fff9}.rule p{font-size:29px;line-height:1.3;color:#c8e4d4;margin:16px 0 0}
'''

def html_slide(num, body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body><div class="slide"><div class="content">{body}</div><div class="num">{num}/3</div></div></body></html>'

slides = [
html_slide(1, '''
<div class="kicker">BIONIC BANKER / AI FINANCE CONTROL MAP</div>
<h1 class="title">AI agents need<br>gates, not vibes.</h1>
<p class="subtitle">The finance question is not “can it answer?” It is: what was it allowed to do when nobody was watching?</p>
<div class="grid2">
  <div class="panel"><div class="label">REQUEST</div><div class="ptext">what was asked</div></div>
  <div class="panel"><div class="label">RULE</div><div class="ptext">what allowed it</div></div>
  <div class="panel"><div class="label">TOOL</div><div class="ptext">what it touched</div></div>
  <div class="panel"><div class="label">OUTPUT</div><div class="ptext">what changed</div></div>
  <div class="panel"><div class="label">CHECK</div><div class="ptext">what failed</div></div>
  <div class="panel"><div class="label">AUDIT</div><div class="ptext">what can be replayed</div></div>
</div>
<div class="callout"><h2>The blocked action is the proof.</h2><p>A useful system can say: the agent tried X, policy allowed Y, the gate blocked Z, and the reason was recorded.</p></div>

'''),
html_slide(2, '''
<div class="kicker">BIONIC BANKER / EVIDENCE CARD</div>
<h1 class="title">What a finance agent<br>must leave behind</h1>
<p class="subtitle">If nobody can replay the decision, nobody can supervise it.</p>
<div class="table">
  <div class="row head"><div class="cell">Record</div><div class="cell">Question it answers</div></div>
  <div class="row"><div class="cell record">Request</div><div class="cell">What did the agent receive?</div></div>
  <div class="row"><div class="cell record">Rule</div><div class="cell">Which policy allowed or blocked action?</div></div>
  <div class="row"><div class="cell record">Output</div><div class="cell">What did the agent produce or change?</div></div>
  <div class="row"><div class="cell record">Review</div><div class="cell">Who checked before external action?</div></div>
  <div class="row"><div class="cell record">Exception</div><div class="cell">What was stopped, escalated, or logged?</div></div>
</div>
<div class="smallpair">
 <div class="panel bad"><div class="label">WEAK DEMO</div><div class="ptext">“the agent answered”</div></div>
 <div class="panel"><div class="label">CONTROL SYSTEM</div><div class="ptext">“the gate worked”</div></div>
</div>
'''),
html_slide(3, '''
<div class="kicker">BIONIC BANKER / OPERATING RULE</div>
<h1 class="title">More autonomy is not<br>the goal.</h1>
<p class="subtitle">More accountable action is. The useful agent loop is boring in the right way.</p>
<div class="checkgrid">
  <div class="check"><div class="badge">1</div><p>Draft locally before action</p></div>
  <div class="check"><div class="badge">2</div><p>Cite the source or say missing</p></div>
  <div class="check"><div class="badge">3</div><p>Check role + policy</p></div>
  <div class="check"><div class="badge">4</div><p>Block external actions by default</p></div>
  <div class="check"><div class="badge">5</div><p>Record the exception</p></div>
  <div class="check"><div class="badge">6</div><p>Send high-risk work to human review</p></div>
  <div class="check"><div class="badge">7</div><p>Update the ledger after publishing</p></div>
  <div class="check"><div class="badge">8</div><p>Stop if duplicate or unverified</p></div>
</div>
<div class="rule"><div class="mono">request → rule → tool → output → check → audit record → human review</div><p>That is where trust starts.</p></div>
<div class="footer">Full note: bionicbanker.tech/blog/ai-agents-need-gates-not-vibes/</div>
''')]

for i, s in enumerate(slides, 1):
    html = OUT / f'slide-{i:02d}.html'
    png = OUT / f'slide-{i:02d}.png'
    html.write_text(s)
    cmd = [
        'brave-browser', '--headless', '--disable-gpu', '--no-sandbox',
        '--hide-scrollbars', '--force-device-scale-factor=2',
        f'--window-size={W},{H}', f'--screenshot={png}', html.resolve().as_uri()
    ]
    subprocess.run(cmd, check=True)

# contact sheet using ImageMagick
subprocess.run(['convert', str(OUT/'slide-01.png'), str(OUT/'slide-02.png'), str(OUT/'slide-03.png'), '+append', str(OUT/'contact-sheet.png')], check=True)
print(OUT)
