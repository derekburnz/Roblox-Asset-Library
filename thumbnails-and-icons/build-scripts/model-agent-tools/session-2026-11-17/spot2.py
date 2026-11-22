import json,math,numpy as np
from obb import *
P=load('ws/world-parts.tsv')
def roty(deg):
    a=math.radians(deg); c,s=math.cos(a),math.sin(a)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]])
t=json.load(open('/home/claude/Cat-Cafe/assets/cat-cafe/rbx/CatCafe_Square_MysterySign.model.json'))
at=np.array([-37.1,0.1,-58.4]); Ra=roty(-140.1); B=[]
def walk(x):
    for c in x.get('children',[]):
        p=c.get('properties',{})
        if 'Size' in p and 'CFrame' in p:
            cf=p['CFrame'].get('CFrame',p['CFrame']); R=np.array(cf['orientation']).reshape(3,3)
            B.append(('Sign.'+c['name'],at+Ra@np.array(cf['position']),Ra@R,np.array(p['Size'])/2))
        walk(c)
walk(t); print('sign parts',len(B))
N=[p for p in P if np.linalg.norm((p[1]-at)[[0,2]])<30 and (p[1][1]+np.abs(p[2][1])@p[3])>0.45 and 'Zones' not in p[0] and 'Paving' not in p[0]]
for sh in (0.05,-0.25,-0.5,-1.0,-1.5,-2.0,-3.0):
    h=hits(B,N,shrink=sh); print('gap' ,-2*sh if sh<0 else 0, {k[-60:]:v for k,v in list(dict(h).items())[:6]} or 'none')
# walk-up ring: cart front centre + ring r
cart=np.array([-45,-53.]); f=np.array([45,53.])/math.hypot(45,53)
C=[p for p in P if 'MysteryMarket' in p[0]]
ring=[p for p in C if 'Ring' in p[0] or 'Circle' in p[0]]
print('ring parts',[(p[0][-40:],p[1].round(1),p[3].round(1)) for p in ring][:4])
d=min(np.linalg.norm(b[1][[0,2]]-(cart+ (2.85+1+4)*f))-np.linalg.norm(b[3][[0,2]]) for b in B)
print('nearest sign part to ring centre (est) minus r4:',round(d-4,1))
# sight line spawn -> cart prompt
for nm,src in (('spawn',np.array([0,-14.])),('cannon',np.array([0,0.]))):
    tgt=cart; dd=tgt-src; L=np.linalg.norm(dd); dd/=L; n=np.array([-dd[1],dd[0]])
    m=min(abs((b[1][[0,2]]-src)@n)-np.linalg.norm(b[3][[0,2]]) for b in B)
    print('line',nm,'-> cart: sign is',round(m,1),'studs off')
print('square edge: sign x,z extent', min(b[1][0] for b in B).round(1), max(b[1][0] for b in B).round(1), min(b[1][2] for b in B).round(1), max(b[1][2] for b in B).round(1))
