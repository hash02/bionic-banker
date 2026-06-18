from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import math, hashlib

W,H=2160,2700
BG='#020604'; GREEN='#2ef29a'; SOFT='#77ffc0'; RED='#ff5c7a'; WHITE='#f4fff9'; MUTED='#cfe7d9'
img=Image.new('RGB',(W,H),BG)
d=ImageDraw.Draw(img)

def font(size,bold=False,mono=False):
    if mono: p='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
    else: p='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    return ImageFont.truetype(p,size)

F_k=font(34,True,True); F_brand=font(28,False,True); F_title=font(142,True); F_sub=font(52)
F_label=font(26,True,True); F_ct=font(54,True); F_cb=font(34); F_num=font(34,True); F_strip=font(48,True); F_item=font(36,True); F_url=font(42,False,True); F_take=font(56,True); F_foot=font(26,False,True)

# background grid
for x in range(0,W,180): d.line((x,0,x,H),fill='#0b3d28',width=2)
for y in range(0,H,180): d.line((0,y,W,y),fill='#0b3d28',width=2)
for x in range(0,W,60): d.line((x,0,x,H),fill='#052417',width=1)
for y in range(0,H,60): d.line((0,y,W,y),fill='#052417',width=1)
# glows
for cx,cy,col in [(230,120,(46,242,154)),(1960,620,(255,92,122)),(1060,1500,(46,242,154))]:
    for r,a in [(850,18),(560,24),(320,28)]:
        ov=Image.new('RGBA',(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
        od.ellipse((cx-r,cy-r,cx+r,cy+r),fill=(*col,a))
        img=Image.alpha_composite(img.convert('RGBA'),ov).convert('RGB'); d=ImageDraw.Draw(img)

def tw(text,f):
    b=d.textbbox((0,0),text,font=f); return b[2]-b[0]
def wrap(text,f,maxw):
    out=[]; cur=''
    for w in text.split():
        t=(cur+' '+w).strip()
        if tw(t,f)<=maxw: cur=t
        else:
            if cur: out.append(cur)
            cur=w
    if cur: out.append(cur)
    return out
def tb(x,y,text,f,fill,maxw,leading=1.18):
    for line in wrap(text,f,maxw):
        d.text((x,y),line,font=f,fill=fill)
        y+=int(f.size*leading)
    return y
def glow_rect(xy,fill,outline,width=5,r=42,glow=(46,242,154,60)):
    ov=Image.new('RGBA',(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
    od.rounded_rectangle(xy,radius=r,outline=glow,width=16)
    ov=ov.filter(ImageFilter.GaussianBlur(12))
    global img,d
    img=Image.alpha_composite(img.convert('RGBA'),ov).convert('RGB'); d=ImageDraw.Draw(img)
    d.rounded_rectangle(xy,radius=r,fill=fill,outline=outline,width=width)
def arrow(x1,y1,x2,y2,color):
    d.line((x1,y1,x2,y2),fill=color,width=10)
    ang=math.atan2(y2-y1,x2-x1); L=40
    d.polygon([(x2,y2),(x2-L*math.cos(ang-math.pi/7),y2-L*math.sin(ang-math.pi/7)),(x2-L*math.cos(ang+math.pi/7),y2-L*math.sin(ang+math.pi/7))],fill=color)

L=150; R=2010
# header
d.text((L,135),'PROMPT INJECTION',font=F_k,fill=GREEN)
d.text((1445,142),'BIONIC BANKER / AI SECURITY',font=F_brand,fill='#9ebdab')
# title
for i,line in enumerate(['AI can be hacked','through instructions.']):
    d.text((L,235+i*146),line,font=F_title,fill=WHITE if i==0 else GREEN)
tb(L,550,'The real risk is not a clever phrase. It is untrusted text crossing into trusted instruction, tool, or approval space.',F_sub,MUTED,1740,1.14)

# central compact rail — no cramped right panel
cards=[
    ('01 / UNTRUSTED','Outside content','Email, PDF, web page, retrieved note, browser text, or tool result.','#21070d',RED,'#ffd6dd'),
    ('02 / MODEL','Context window','The AI reads evidence and instructions in the same place unless the system separates them.','#062014',GREEN,'#d5efe2'),
    ('03 / GATES','Control layer','Label source, restrict tools, require approval, and keep an audit log.','#06160f',SOFT,'#d5efe2'),
    ('04 / ACTION','Safe output','Answer, summarize, draft, or escalate without leaking secrets or taking hidden actions.','#062014',GREEN,'#d5efe2'),
]
y0=790; cardw=428; gap=44; cardh=510
xs=[L+i*(cardw+gap) for i in range(4)]
for idx,(lab,title,body,fill,outline,bodyfill) in enumerate(cards):
    x=xs[idx]
    glow=(255,92,122,58) if idx==0 else (46,242,154,58)
    glow_rect((x,y0,x+cardw,y0+cardh),fill,outline,5,44,glow)
    # number badge
    d.rounded_rectangle((x+28,y0+28,x+98,y0+98),radius=20,fill=outline)
    d.text((x+47,y0+45),str(idx+1),font=F_num,fill='#031008')
    d.text((x+116,y0+45),lab,font=F_label,fill=outline if idx!=0 else '#ff7890')
    tb(x+32,y0+145,title,F_ct,WHITE,cardw-64,1.05)
    tb(x+32,y0+265,body,F_cb,bodyfill,cardw-70,1.18)
# arrows between cards, centered
for i,c in enumerate([GREEN,GREEN,GREEN]):
    arrow(xs[i]+cardw+8,y0+255,xs[i+1]-10,y0+255,c)

# knowledge strip
strip=(L,1390,R,1810)
glow_rect(strip,'#031008','#1d8f5b',4,42,(46,242,154,42))
d.text((L+42,1435),'WHAT NORMAL USERS SHOULD KNOW',font=F_label,fill=GREEN)
tb(L+42,1500,'Do not paste secrets into a system that cannot show what it trusted.',F_strip,WHITE,800,1.1)
items=[('1','Treat outside text as data, not authority.'),('2','Keep passwords, keys, IDs, and private files out.'),('3','Never let an AI spend, send, approve, or delete by default.')]
ix=1125; iy=1458
for n,t in items:
    d.ellipse((ix,iy,ix+58,iy+58),fill=GREEN)
    d.text((ix+19,iy+11),n,font=font(28,True),fill='#031008')
    tb(ix+82,iy+1,t,F_item,'#eafff4',720,1.08)
    iy+=108

# takeaway panel: fills the bottom intentionally instead of leaving dead grid space
take=(L,1950,R,2365)
glow_rect(take,'#031008','#166b47',4,42,(46,242,154,34))
d.text((L+42,2028),'bionicbanker.tech',font=F_url,fill=GREEN)
tb(720,2000,'If you cannot trace what the AI saw, trusted, called, and approved, do not trust it with sensitive work.',F_take,WHITE,1210,1.12)
d.line((L,2468,R,2468),fill='#0f5135',width=2)
d.text((L,2525),'CONTROL MAP / DEFENSIVE AI SECURITY LITERACY',font=F_foot,fill='#628f79')

# save
out=Path('/home/hash/bionic-banker/social-assets/linkedin-ready/ai-prompt-injection-control-failure/prompt-injection-single-slide.png')
img.save(out,quality=98,subsampling=0)
print(out,img.size,out.stat().st_size,hashlib.sha256(out.read_bytes()).hexdigest())
