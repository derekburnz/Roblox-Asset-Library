import sys,math,collections
import numpy as np
from obb import *
P=load('ws/world-parts.tsv')
def roty(deg):
    a=math.radians(deg); c,s=math.cos(a),math.sin(a)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]])
cart=np.array([-45,0.1,-53.]); f=np.array([45,0,53.])/math.hypot(45,53); X=np.array([-f[2],0,f[0]])
def facing(x,z,tx,tz):  # rotY so -Z looks at target
    return math.degrees(math.atan2(-(tx-x),-(tz-z)))
print('cart rot',facing(-45,-53,0,0))
C=[p for p in P if 'MysteryMarket' in p[0] or 'MysteryCart' in p[0]]
print('cart parts',len(C)); 
xs=[(p[1]-cart)@X for p in C]; zs=[(p[1]-cart)@f for p in C]
print('cart extent along X',min(xs),max(xs),'along f',min(zs),max(zs))
def near(cen,r):
    return [p for p in P if np.linalg.norm((p[1]-cen)[[0,2]])<r+np.linalg.norm(p[3]) and (p[1][1]+np.abs(p[2][1])@p[3])>0.45 and 'Zones' not in p[0] and 'Paving' not in p[0]]
for nm,(dx,df,tgt) in {'A+X':(7.6,0.5,(0,-14)),'A2':(7.6,1.5,(0,-14)),'B-X':(-8.0,0.5,(0,-14)),'B2':(-8.4,1.5,(0,-14)),'A3':(8.2,0.0,(0,0)),'B3':(-8.6,0.0,(0,0))}.items():
    c=cart+dx*X+df*f; rot=facing(c[0],c[2],*tgt); R=roty(rot)
    A=[('sign',c+np.array([0,3.5,0]),R,np.array([2.9,3.5,0.9]))]
    N=near(c,25)
    out=[]
    for shrink in (0.05,-0.5,-1.0,-1.5,-2.5):
        h=hits(A,N,shrink=shrink)
        out.append((shrink, sorted(set(k.split('.')[-2] if '.' in k else k for k in dict(h)))[:6] if h else 'none'))
    print(nm,c.round(1),round(rot,1)); [print('   ',o) for o in out]
print('----')
for nm,(dx,df,tgt) in {'B':(-8.0,0.5,(0,-14)),'B4':(-8.6,2.0,(0,-14)),'B5':(-9.5,1.0,(0,-14))}.items():
    c=cart+dx*X+df*f; rot=facing(c[0],c[2],*tgt); R=roty(rot)
    A=[('sign',c+np.array([0,3.5,0]),R,np.array([2.9,3.5,0.9]))]
    N=near(c,25)
    print(nm,c.round(1),round(rot,1))
    for shrink in (-0.5,-1.0,-2.0,-3.0):
        h=hits(A,N,shrink=shrink); print('  ',shrink*-2, [k[-70:] for k in dict(h)][:8])
