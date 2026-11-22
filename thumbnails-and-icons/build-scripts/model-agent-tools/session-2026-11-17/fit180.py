import json,math,re,sys,numpy as np,itertools
from obb import *
RBX='/home/claude/Cat-Cafe/assets/cat-cafe/rbx/'
def face(x,z,tx=0,tz=0): return math.degrees(math.atan2(-(tx-x),-(tz-z)))
def roty(d):
    a=math.radians(d); c,s=math.cos(a),math.sin(a); return np.array([[c,0,s],[0,1,0],[-s,0,c]])
ST={"arcade":("ArcadeCabinet",(-44,22),(-45,30),0),"spin":("SpinWheel",(-26,54),(-26,56),0),"pool":("MysticPool",(44,22),(45,30),0),
"fish":("FishMarket",(45,52),(47,79),0),"cart":("CornerShop",(24,56),(25,57),0),"codes":("CodesCat",(-44,-23),(-45,-30),0),
"mystery":("MysteryMarket",(-45,-53),(-46,-78),0),"pity":("TownSquare.CatCafe_Square_PitySign",(-22,-56),(-20,-62),1),
"feedback":("FeedbackStand",(28,-54),(26,-56),0),"thanks":("ThanksBoard",(46,-56),(47,-79),0),
"poster":("TownSquare.CatCafe_Square_UpdatePoster",(20,-40),(13.5,-66),1),"bellhop":("BellhopStand",(-48,0),(-48,0),0),"leaders":("Leaderboards",(50,0),(50,0),0)}
EXTRA={"night":("CatCafe_Street_DealerCart",(45,-30),0),"rally":("CatCafe_Square_RallyBoard",(-46,78),1),
"msign":("CatCafe_Square_MysterySign",(-38.1,-83.4),1),"decor":("CatCafe_Square_DecorStand",(38.5,85.5),1)}
P=load('ws/world-parts.tsv')
def model(name,d=RBX):
    t=json.load(open(d+name+'.model.json')); B=[]
    def walk(x):
        for ch in x.get('children',[]):
            p=ch.get('properties',{})
            if 'Size' in p and 'CFrame' in p:
                cf=p['CFrame'].get('CFrame',p['CFrame']); B.append((ch['name'],np.array(cf['position']),np.array(cf['orientation']).reshape(3,3),np.array(p['Size'])/2))
            walk(ch)
    walk(t); return B
G={}
for k,(folder,a,b,fix) in ST.items():
    pre='Workspace.World.'+folder
    r0=face(*a,0,-14) if fix else face(*a); r1=face(*b,0,-14) if fix else face(*b); D=roty(r1-r0); A=np.array([a[0],0,a[1]]); Bv=np.array([b[0],0,b[1]])
    G[k]=[(k,Bv+D@(c-A),D@R,h) for (n,c,R,h) in P if (n.startswith(pre+'.') or n==pre) and c[1]+np.abs(R[1])@h>0.45]
import os
for k,(name,b,fix) in EXTRA.items():
    d=RBX if os.path.exists(RBX+name+'.model.json') else 'rbxx/'
    Ra=roty(face(*b,0,-14) if fix else face(*b))
    G[k]=[(k,np.array([b[0],0.1,b[1]])+Ra@p,Ra@R,h) for (n,p,R,h) in model(name,d) if (0.1+p[1]+np.abs(R[1])@h)>0.45]
E=[]
for l in open('rows.txt'):
    m=re.search(r'asset = "(\w+)", x = ([-\d.]+), y = 0.1, z = ([-\d.]+)(?:, rotY = ([-\d.]+))?',l)
    if not m or 'Paving' in l or 'Bunting' in l or 'Garden' in l: continue
    name,x,z,r=m.group(1),float(m.group(2)),float(m.group(3)),float(m.group(4) or 0); Ra=roty(r)
    E+=[(name.replace('CatCafe_Square_','')+'@%g,%g'%(x,z),np.array([x,0.1,z])+Ra@p,Ra@R,h) for (n,p,R,h) in model(name) if (0.1+p[1]+np.abs(R[1])@h)>0.45]
RING={"arcade","spin","pool","fish","cart","codes","mystery","night","feedback"}
rc={}
for k in RING:
    b=ST[k][2] if k in ST else EXTRA[k][1]; f=-np.array(b)/np.linalg.norm(b)
    # ring centre: just in front of the model's front extent
    ext=max((np.array([p[1][0],p[1][2]])-np.array(b))@f+np.linalg.norm(p[3][[0,2]])*0.6 for p in G[k])
    rc[k]=np.array(b)+f*(ext+8+1.5)
def gap(A,B):
    for sh in (0.05,-0.5,-1,-1.5,-2,-3,-4,-5):
        hit=False
        for a in A:
            for b in B:
                if np.linalg.norm(b[1]-a[1])>rad(a)+rad(b)+12: continue
                if sat(a,b,sh): hit=True;break
            if hit: break
        if hit: return -2*sh if sh<0 else 0
    return 99
print('--- body to body gaps under 6')
for a,b in itertools.combinations(G,2):
    g=gap(G[a],G[b])
    if g<=6: print(a,b,'gap <',g)
print('--- body to edge props under 4')
for a in G:
    near=[e for e in E if min(np.linalg.norm(e[1][[0,2]]-p[1][[0,2]]) for p in G[a][::5])<14]
    if near:
        g=gap(G[a],near)
        if g<=4: print(a,'gap <',g)
print('--- rings: centre, distance to other bodies, rings, lanes')
for k,c in rc.items():
    out=[]
    for o in G:
        if o==k: continue
        d=min(np.linalg.norm(p[1][[0,2]]-c)-np.linalg.norm(p[3][[0,2]]) for p in G[o])-8
        if d<3: out.append('%s %.1f'%(o,d))
    for o,c2 in rc.items():
        if o!=k and np.linalg.norm(c-c2)-16<3: out.append('ring %s %.1f'%(o,np.linalg.norm(c-c2)-16))
    lane=abs(c[0])-8-8; cross=abs(c[1])-6-8
    print(k,c.round(1),'street lane %.1f cross lane %.1f'%(lane,cross),out)
print('--- sight from spawn and cannon: bodies within 3 of the line to each station middle')
for src,nm in (((0,-14),'spawn'),((0,0),'cannon')):
    for k in G:
        b=ST[k][2] if k in ST else EXTRA[k][1]; s=np.array(src,float); d=np.array(b)-s; L=np.linalg.norm(d); d/=L; n=np.array([-d[1],d[0]])
        for o in G:
            if o==k: continue
            for p in G[o]:
                q=p[1][[0,2]]-s; t=q@d
                if 2<t<L-3 and abs(q@n)<np.linalg.norm(p[3][[0,2]])*0.7 and p[1][1]+p[3][1]>2.5:
                    print(nm,'->',k,'crossed by',o); break
