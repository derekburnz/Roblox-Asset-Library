import json,math,sys,numpy as np
from obb import *
P=load('ws/world-parts.tsv')
def roty(deg):
    a=math.radians(deg); c,s=math.cos(a),math.sin(a)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]])
def facing(x,z,tx,tz): return math.degrees(math.atan2(-(tx-x),-(tz-z)))
m=np.array([45,0.1,52.]); f=np.array([-45,0,-52.])/math.hypot(45,52); X=np.array([-f[2],0,f[0]])
t=json.load(open('/home/claude/Cat-Cafe/assets/cat-cafe/rbx/CatCafe_Square_DecorStand.model.json'))
for dx,df in ((-9.3,1.0),(-9.0,0.6),(-8.8,1.2)):
    at=m+dx*X+df*f; at=np.array([round(at[0],1),0.1,round(at[2],1)]); rot=round(facing(at[0],at[2],0,-14),1); Ra=roty(rot); B=[]
    def walk(x):
        for c in x.get('children',[]):
            p=c.get('properties',{})
            if 'Size' in p and 'CFrame' in p:
                cf=p['CFrame'].get('CFrame',p['CFrame']); R=np.array(cf['orientation']).reshape(3,3)
                B.append(('S.'+c['name'],at+Ra@np.array(cf['position']),Ra@R,np.array(p['Size'])/2))
            walk(c)
    walk(t)
    N=[p for p in P if np.linalg.norm((p[1]-at)[[0,2]])<30 and (p[1][1]+np.abs(p[2][1])@p[3])>0.45 and 'Zones' not in p[0] and 'Paving' not in p[0]]
    print(at,rot,len(B))
    for sh in (0.05,-0.25,-0.5,-1.0,-2.0,-3.0,-4.0):
        h=hits(B,N,shrink=sh); print('  gap',-2*sh if sh<0 else 0,[k[-40:] for k in dict(h)][:5])
    ring=[p for p in P if 'WalkUpCircle' in p[0] and np.linalg.norm((p[1]-m)[[0,2]])<16]
    if ring:
        rc=np.mean([p[1] for p in ring],axis=0); rr=max(np.linalg.norm((p[1]-rc)[[0,2]])+np.linalg.norm(p[3][[0,2]]) for p in ring)
        print('  ring centre',rc.round(1),'r<=',round(rr,1),'stand nearest', round(min(np.linalg.norm((b[1]-rc)[[0,2]])-np.linalg.norm(b[3][[0,2]]) for b in B)-rr,1))
    for nm,src in (('spawn',np.array([0,-14.])),('cannon',np.array([0,0.]))):
        dd=m[[0,2]]-src; L=np.linalg.norm(dd); dd/=L; n=np.array([-dd[1],dd[0]])
        print('  line',nm,'-> market:',round(min(abs((b[1][[0,2]]-src)@n)-np.linalg.norm(b[3][[0,2]]) for b in B),1))
    print('  extent x',round(min(b[1][0] for b in B),1),round(max(b[1][0] for b in B),1),'z',round(min(b[1][2] for b in B),1),round(max(b[1][2] for b in B),1))
