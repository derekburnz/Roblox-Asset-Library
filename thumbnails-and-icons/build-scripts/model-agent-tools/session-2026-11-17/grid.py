import math,numpy as np,collections
from obb import *
P=load('ws/world-parts.tsv')
def roty(deg):
    a=math.radians(deg); c,s=math.cos(a),math.sin(a)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]])
def facing(x,z,tx,tz): return math.degrees(math.atan2(-(tx-x),-(tz-z)))
sq=[p for p in P if abs(p[1][0])<75 and abs(p[1][2])<85 and 'Paving' not in p[0] and 'Zones' not in p[0] and 'DayCart' not in p[0] and 'CornerShop' not in p[0]]
tall=[p for p in sq if (p[1][1]+np.abs(p[2][1])@p[3])>0.45 or 'WalkUpCircle' in p[0] or 'Circle' in p[0]]
# drop the day cart's own ring: rings near (24,56)+front
dc=np.array([24,56.]); f0=-dc/np.linalg.norm(dc)
tall=[p for p in tall if not ('WalkUpCircle' in p[0] and np.linalg.norm(p[1][[0,2]]-(dc+7*f0))<9)]
print(len(sq),len(tall))
top=collections.Counter(p[0].split('.')[2] if p[0].count('.')>=2 else p[0] for p in tall); print(top.most_common(40))
best=[]
fm=np.array([45,52.])
for x in range(-54,55,2):
  for z in range(-64,65,2):
    if abs(x)<8+6 or abs(z)<6+6: continue
    c=np.array([x,0.1,z]); R=roty(facing(x,z,0,0))
    # cart body 8.4x3.6 plus ring r8 one stud in front: box x±5, z from -12 (front) to +2
    A=[('b',c+R@np.array([0,3.5,-5.0]),R,np.array([5.0,3.5,7.0]))]
    N=[p for p in tall if np.linalg.norm((p[1]-c)[[0,2]])<16+np.linalg.norm(p[3][[0,2]])]
    if hits(A,N,shrink=-1.5): continue
    best.append((round(float(np.linalg.norm(np.array([x,z])-fm)),1),x,z))
best.sort(reverse=True); print(len(best)); print(best[:40])
