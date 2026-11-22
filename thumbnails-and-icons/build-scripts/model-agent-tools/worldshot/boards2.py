import sys; sys.path.insert(0,'/tmp/claude-0/-home-user/a4f71671-9dc8-5695-92a1-30a7f3b86c31/scratchpad')
from obb import *
P=load('/tmp/claude-0/-home-user/a4f71671-9dc8-5695-92a1-30a7f3b86c31/scratchpad/ws2/world-parts.tsv')
for area in ['Ruins','Desert','Park','Neighbourhood','Woods','Sewer']:
    A=[p for p in P if ('IndexBoards.'+area+'IndexBoard') in p[0]]
    bars=[p for p in P if ('Gates.'+area+'Gate') in p[0]]
    cen=np.mean([p[1] for p in A],axis=0)
    near=[p for p in P if ('IndexBoards.'+area+'IndexBoard') not in p[0] and np.linalg.norm((p[1]-cen)[[0,2]])<40+np.linalg.norm(p[3]) and p[1][1]+abs(p[2][1])@p[3]>0.6 and 'Zones' not in p[0] and 'WalkUp' not in p[0]]
    g=np.mean([p[1] for p in bars],axis=0)
    lo=np.min([p[1]-np.abs(p[2])@p[3] for p in bars],axis=0); hi=np.max([p[1]+np.abs(p[2])@p[3] for p in bars],axis=0)
    along = np.array([1,0,0]) if (hi-lo)[0]>(hi-lo)[2] else np.array([0,0,1])
    nrm=np.array([0,0,1]) if along[0] else np.array([1,0,0])
    if np.dot(cen-g,nrm)<0: nrm=-nrm
    print('==',area)
    for d in (0,3,4):
        h=hits(A,near,shift=nrm*d,shrink=-0.25)
        print('  back %d, within 0.5 studs:'%d,{k.replace('Workspace.World.',''):v for k,v in h.items()})
