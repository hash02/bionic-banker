from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
W,H=2160,2700
img=Image.new('RGB',(W,H),'#020604')
d=ImageDraw.Draw(img)
def font(size,bold=False,mono=False):
    p='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf' if mono else ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
    return ImageFont.truetype(p,size)
F_mono=font(36,mono=True); F_brand=font(30,mono=True); F_title=font(126,True); F_sub=font(54); F_h=font(54,True); F_body=font(38); F_gate=font(40,True); F_take=font(50,True)
for x in range(0,W,180): d.line((x,0,x,H), fill='#0b3d28', width=2)
for y in range(0,H,180): d.line((0,y,W,y), fill='#0b3d28', width=2)
for r,alpha in [(900,18),(650,22),(420,30)]:
    overlay=Image.new('RGBA',(W,H),(0,0,0,0)); od=ImageDraw.Draw(overlay); od.ellipse((120-r,70-r,120+r,70+r), fill=(31,160,104,alpha)); img=Image.alpha_composite(img.convert('RGBA'),overlay).convert('RGB')
d=ImageDraw.Draw(img)
def wrap(text,f,maxw):
    words=text.split(); lines=[]; cur=''
    for w in words:
        test=(cur+' '+w).strip()
        if d.textbbox((0,0),test,font=f)[2] <= maxw: cur=test
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines
def tb(x,y,text,f,fill,maxw,leading=1.18):
    for line in wrap(text,f,maxw):
        d.text((x,y),line,font=f,fill=fill); y+=int(f.size*leading)
    return y
def rounded(xy,fill,outline,width=4,radius=44): d.rounded_rectangle(xy,radius=radius,fill=fill,outline=outline,width=width)
# header
d.text((144,144),'PROMPT INJECTION',font=F_mono,fill='#2ef29a')
d.text((1510,150),'BIONIC BANKER / AI SECURITY',font=F_brand,fill='#9ebdab')
y=222
for line in ['AI can be hacked','through instructions.']:
    d.text((144,y),line,font=F_title,fill='#f4fff9'); y+=126
tb(144,505,'The risk is untrusted text crossing into trusted instruction, tool, or approval space.',F_sub,'#c5dfd2',1700,1.18)
# boxes
trusted=(144,770,790,1115); untrusted=(144,1395,790,1775); context=(910,1050,1515,1515); gates=(1635,770,2020,1775)
rounded(trusted,'#062014','#2ef29a'); rounded(untrusted,'#21070d','#ff5c7a'); rounded(context,'#06160f','#77ffc0',6); rounded(gates,'#06160f','#2ef29a')
d.text((200,830),'TRUSTED',font=F_mono,fill='#2ef29a'); d.text((200,900),'System rules',font=F_h,fill='#f4fff9'); tb(200,985,'Policy, role, tool limits, approvals.',F_body,'#cfe9dc',500)
d.text((200,1455),'UNTRUSTED',font=F_mono,fill='#ff7890'); d.text((200,1530),'Hidden instruction',font=F_h,fill='#fff4f6'); tb(200,1620,'Email, PDF, web page, retrieved note, tool result.',F_body,'#ffd2d9',510)
d.text((970,1115),'MODEL CONTEXT',font=F_mono,fill='#77ffc0'); d.text((970,1205),'What the AI sees',font=F_h,fill='#f4fff9'); tb(970,1295,'The model needs the system to separate evidence from commands.',F_body,'#cfe9dc',440)
d.text((1690,835),'CONTROL GATES',font=F_mono,fill='#2ef29a')
gates_text=[('1','Label source'),('2','Restrict tools'),('3','Log review')]
y=970
for n,t in gates_text:
    d.ellipse((1690,y,1770,y+80),fill='#2ef29a'); d.text((1715,y+13),n,font=font(44,True),fill='#031008')
    d.text((1800,y+8),t,font=F_gate,fill='#eafff4')
    if n=='1': tb(1800,y+65,'Data is not instruction.',font(31),'#b9d7c8',190,1.1)
    if n=='2': tb(1800,y+65,'No secret or action by default.',font(31),'#b9d7c8',190,1.1)
    if n=='3': tb(1800,y+65,'Request, source, tool, outcome.',font(31),'#b9d7c8',190,1.1)
    y+=250
# arrows
import math
def arrow(x1,y1,x2,y2,color):
    d.line((x1,y1,x2,y2),fill=color,width=9)
    ang=math.atan2(y2-y1,x2-x1); L=34
    d.polygon([(x2,y2),(x2-L*math.cos(ang-math.pi/7),y2-L*math.sin(ang-math.pi/7)),(x2-L*math.cos(ang+math.pi/7),y2-L*math.sin(ang+math.pi/7))],fill=color)
arrow(790,940,910,1190,'#2ef29a'); arrow(790,1580,910,1400,'#ff5c7a'); arrow(1515,1280,1635,1280,'#2ef29a')
# footer
d.line((144,2255,2016,2255),fill='#1c6b47',width=2)
d.text((144,2330),'bionicbanker.tech',font=font(42,mono=True),fill='#2ef29a')
tb(760,2310,'If you cannot trace what the AI saw, trusted, called, and approved, do not trust it with sensitive work.',F_take,'#f4fff9',1180,1.13)
out=Path('/home/hash/bionic-banker/social-assets/linkedin-ready/ai-prompt-injection-control-failure/prompt-injection-single-slide.png')
img.save(out, quality=95)
print(out, img.size)
