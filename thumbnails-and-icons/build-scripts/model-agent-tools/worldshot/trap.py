import sys; sys.path.insert(0,'/tmp/claude-0/-home-user/a4f71671-9dc8-5695-92a1-30a7f3b86c31/scratchpad')
from obb import *
P=load('/tmp/claude-0/-home-user/a4f71671-9dc8-5695-92a1-30a7f3b86c31/scratchpad/ws2/world-parts.tsv')
A=[p for p in P if 'rescue_park_2' in p[0]]
ids=set(id(p) for p in A)
cen=np.mean([p[1] for p in A],axis=0); print('trap centre',cen.round(1), len(A))
near=[p for p in P if id(p) not in ids and np.linalg.norm((p[1]-cen)[[0,2]])<45+np.linalg.norm(p[3]) and p[1][1]+abs(p[2][1])@p[3]>0.35 and 'Zones' not in p[0]]
print(len(near))
ok=[]
for dx in range(-14,3,1):
    for dz in range(-24,25,2):
        h=hits(A,near,shift=np.array([dx,0,dz]),shrink=-0.4)
        if not h: ok.append((dx,dz))
print('clear shifts (world dx,dz):',ok)
print('local spots:',[(-(52+dx), -( -2030+dz) - 2000) for dx,dz in ok])
