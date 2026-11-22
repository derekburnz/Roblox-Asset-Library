import sys; sys.path.insert(0,'/tmp/claude-0/-home-user/a4f71671-9dc8-5695-92a1-30a7f3b86c31/scratchpad')
from obb import *
P=load('/tmp/claude-0/-home-user/a4f71671-9dc8-5695-92a1-30a7f3b86c31/scratchpad/ws2/world-parts.tsv')
A=[p for p in P if 'Alley.Props.CatCafe_Alley_Crate' in p[0] and 'Stack' not in p[0] and -1359.2<p[1][0]<-1356.5 and -1285.2<p[1][2]<-1282.8]
lo=np.min([p[1]-np.abs(p[2])@p[3] for p in A],axis=0); hi=np.max([p[1]+np.abs(p[2])@p[3] for p in A],axis=0)
print(len(A),'crate parts',lo.round(2),hi.round(2))
ids=set(id(p) for p in A)
near=[p for p in P if id(p) not in ids and np.linalg.norm(p[1]-(lo+hi)/2)<12+np.linalg.norm(p[3]) and p[1][1]+abs(p[2][1])@p[3]>0.25]
for dx in (0,-0.4,-0.6,-0.8):
    print(dx, {k.replace('Workspace.World.',''):v for k,v in hits(A,near,shift=np.array([dx,0,0]),shrink=0.02).items()}, 'within 0.2:', {k.replace('Workspace.World.',''):v for k,v in hits(A,near,shift=np.array([dx,0,0]),shrink=-0.1).items()})
