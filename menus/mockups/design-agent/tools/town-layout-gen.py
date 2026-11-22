import sys, math
S=1.8
X0,X1=-222,222
Z0,Z1=-192,272
TOP=70
W=int((X1-X0)*S); H=int((Z1-Z0)*S)+TOP+40
def px(x): return (x-X0)*S
def py(z): return (Z1-z)*S+TOP
out=[]
F='font-family="Helvetica, Arial, sans-serif"'
def rect(x1,z1,x2,z2,fill,stroke='none',sw=0,op=1,dash=None):
    X1_,X2_=min(x1,x2),max(x1,x2); Za,Zb=min(z1,z2),max(z1,z2)
    d=f' stroke-dasharray="{dash}"' if dash else ''
    out.append(f'<rect x="{px(X1_):.1f}" y="{py(Zb):.1f}" width="{(X2_-X1_)*S:.1f}" height="{(Zb-Za)*S:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"{d}/>')
def circ(x,z,r,fill,stroke='none',sw=0,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    out.append(f'<circle cx="{px(x):.1f}" cy="{py(z):.1f}" r="{r*S:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
def text(x,z,t,size=11,fill='#3b2f2f',weight='normal',anchor='middle',rot=None):
    tr=f' transform="rotate({rot} {px(x):.1f} {py(z):.1f})"' if rot is not None else ''
    out.append(f'<text x="{px(x):.1f}" y="{py(z):.1f}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" {F}{tr}>{t}</text>')
def line(x1,z1,x2,z2,color,w=4,dash=None,op=1):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    out.append(f'<line x1="{px(x1):.1f}" y1="{py(z1):.1f}" x2="{px(x2):.1f}" y2="{py(z2):.1f}" stroke="{color}" stroke-width="{w}" stroke-linecap="round" opacity="{op}"{d}/>')
out.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ece7da"/>')
out.append(f'<text x="{W/2}" y="26" font-size="18" font-weight="bold" fill="#3b2f2f" text-anchor="middle" {F}>Town layout v3.1: the compass</text>')
out.append(f'<text x="{W/2}" y="46" font-size="12" fill="#5d4e4e" text-anchor="middle" {F}>North is up. 1 grid square = 20 studs. Each area is straight down one arm of the Town Square.</text>')
for gx in range(-220,221,20):
    out.append(f'<line x1="{px(gx):.1f}" y1="{TOP}" x2="{px(gx):.1f}" y2="{py(Z0):.1f}" stroke="#ddd6c6" stroke-width="0.6"/>')
for gz in range(-180,271,20):
    out.append(f'<line x1="0" y1="{py(gz):.1f}" x2="{W}" y2="{py(gz):.1f}" stroke="#ddd6c6" stroke-width="0.6"/>')
# areas
rect(-70,126,70,266,'#f2c48d'); text(0,236,'Neighbourhood (Tier 3)',14,weight='bold'); text(0,222,'140 x 140, its gate at the street\'s north end',10)
rect(-40,-182,40,-126,'#9ccc65'); text(0,-160,'Park (Tier 2)',13,weight='bold')
rect(-215,-60,-95,60,'#6d9d5e'); text(-155,12,'Woods (Tier 4)',13,fill='#fff',weight='bold'); text(-155,-2,'120 x 120',10,fill='#fff')
rect(95,-45,185,45,'#8aa3b0'); text(140,12,'Sewer (Tier 5)',13,fill='#fff',weight='bold'); text(140,-2,'90 x 90',10,fill='#fff')
# back alleys with closed ends
for s in (-1,1):
    rect(s*63,-125.5,s*93,125.5,'#d9b38c')
    line(s*63,125.5,s*94,125.5,'#6d4c41',3); line(s*63,-125.5,s*94,-125.5,'#6d4c41',3)
    text(s*78,60,'Back alley (Alleyway)',11,rot=-90)
# street
rect(-16,-124,16,124,'#b9b4ab')
# plots
order={(-1,-58):1,(1,-58):2,(-1,58):3,(1,58):4,(-1,-102):5,(1,-102):6,(-1,102):7,(1,102):8}
for (side,cz),n in order.items():
    rect(side*24,cz-18,side*52,cz+18,'#f8bbd0','#c2185b',1)
    rect(side*53,cz-18,side*63,cz+18,'#ffe0b2')
    text(side*38,cz-2,f'Cafe {n}',12,weight='bold')
# town square
rect(-48,-32,48,32,'#f3e3c3','#b08d57',1.5)
rect(-63,-32,-48,32,'#a5d6a7'); rect(48,-32,63,32,'#a5d6a7')
for gx in (-56,56):
    for gz in (-24,-14,14,24):
        circ(gx,gz,3,'#66bb6a')
rect(-8,-32,8,32,'#fbf3e3'); rect(-63,-6,63,6,'#fbf3e3')
text(0,33.8,'TOWN SQUARE (safe zone)',12,weight='bold')
# paw paths to each gate, in the area colour
line(0,8,0,124,'#e08a2c',5,'2 7',0.9)
line(0,-8,0,-124,'#4f8f22',5,'2 7',0.9)
line(-8,0,-93,0,'#2e5e30',5,'2 7',0.9)
line(8,0,93,0,'#3f6378',5,'2 7',0.9)
for a in (45,135,315):
    r=11; circ(r*math.cos(math.radians(a)),r*math.sin(math.radians(a)),1.2,'#8d6e63')
circ(0,0,6,'#81d4fa','#0277bd',1.5); text(0,8.6,'fountain',9)
# signpost replaces the south-west bench
circ(-7.8,-7.8,1.6,'#5d4037'); text(-11,-4.2,'signpost',9,fill='#5d4037',weight='bold',anchor='end')
def station(x,z,label,color):
    circ(x,z,4,color,'#3b2f2f',1); text(x,z+6.5 if z>0 else z-9.5,label,10,weight='bold')
station(-28,16,'Spin Wheel','#ffcc80')
station(28,16,'Golden Fish Market','#ffe082')
station(-28,-16,'Codes Cat','#ce93d8')
circ(-22.8,-13.0,4,'none','#8e24aa',1.2,'3 2')
station(28,-16,'Dealer cart','#90a4ae')
circ(0,-14,1.8,'#2e7d32'); text(3,-20,'spawn',9,fill='#2e7d32',weight='bold',anchor='start')
# side arches (12 wide) and Alleyway boards
for s in (-1,1):
    line(s*63,6,s*63,-6,'#c0392b',4)
    rect(s*71-1.5,s*9-1,s*71+1.5,s*9+1,'#5d4037')
text(-63,9,'arch',9); text(63,9,'arch',9)
text(-71,-15.5,'board',8); text(71,15.5,'board',8)
# gates
line(-12,-125,12,-125,'#c0392b',5); text(0,-132,'Park gate',10,weight='bold')
line(-12,125,12,125,'#c0392b',5); text(0,130,'Neighbourhood gate',10,weight='bold')
line(-94,-12,-94,12,'#c0392b',5); text(-80,18,'Woods gate',10,weight='bold')
line(94,-12,94,12,'#c0392b',5); text(80,-20,'Sewer gate',10,weight='bold')
# rare cat nooks at the alley ends
for s in (-1,1):
    for (x,z) in ((70,119),(84,121),(82,-119),(68,-121)):
        circ(s*x,z,2,'#ffd54f','#b8860b',1)
text(-78,112,'rare cat nook',8,weight='bold'); text(78,-112,'rare cat nook',8,weight='bold')
# legend
ly=py(Z0)+22
out.append(f'<circle cx="24" cy="{ly-4}" r="4" fill="#ffd54f" stroke="#b8860b" stroke-width="1"/><text x="34" y="{ly}" font-size="11" fill="#3b2f2f" {F}>Epic and rarer alley cats (the old Alley Square points)</text>')
out.append(f'<line x1="470" y1="{ly-4}" x2="502" y2="{ly-4}" stroke="#4f8f22" stroke-width="5" stroke-dasharray="2 7" stroke-linecap="round"/><text x="510" y="{ly}" font-size="11" fill="#3b2f2f" {F}>paw path in the area\'s colour</text>')
H2=int(ly+16)
svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H2}" viewBox="0 0 {W} {H2}">'+''.join(out)+'</svg>'
open(sys.argv[1],'w').write(svg); print(W,H2)
