import math,numpy as np
from obb import *
P=load('ws/world-parts.tsv')
def roty(deg):
    a=math.radians(deg); c,s=math.cos(a),math.sin(a)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]])
def facing(x,z,tx,tz): return math.degrees(math.atan2(-(tx-x),-(tz-z)))
m=np.array([45,0.1,52.]); f=np.array([-45,0,-52.])/math.hypot(45,52); X=np.array([-f[2],0,f[0]])
C=[p for p in P if 'FishMarket' in p[0]]
names=set(p[0].rsplit('.',2)[0][-50:] for p in C); print(len(C),list(names)[:4])
xs=[(p[1]-m)@X for p in C]; zs=[(p[1]-m)@f for p in C]; print('market extent X',round(min(xs),1),round(max(xs),1),'f',round(min(zs),1),round(max(zs),1))
def near(cen,r): return [p for p in P if np.linalg.norm((p[1]-cen)[[0,2]])<r+np.linalg.norm(p[3]) and (p[1][1]+np.abs(p[2][1])@p[3])>0.45 and 'Zones' not in p[0] and 'Paving' not in p[0]]
for nm,(dx,df) in {'+X 9':(9,0.5),'-X 9':(-9,0.5),'+X 9.5 f2':(9.5,2),'-X 9.5 f2':(-9.5,2),'+X 10':(10,1),'-X 10':(-10,1)}.items():
    c=m+dx*X+df*f; rot=facing(c[0],c[2],0,-14)
    A=[('s',c+np.array([0,3,0]),roty(rot),np.array([2.5,3,1.5]))]
    N=near(c,25); print(nm,c.round(1),round(rot,1))
    for sh in (0.05,-0.5,-1.0,-2.0,-3.0):
        h=hits(A,N,shrink=sh); print('   gap',-2*sh if sh<0 else 0,[k[-45:] for k in dict(h)][:6])
