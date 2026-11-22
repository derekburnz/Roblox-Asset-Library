import sys,json,math,collections
sys.path.insert(0,'.')
import numpy as np
from obb import *
P=load('ws/world-parts.tsv')
def roty(deg):
    a=math.radians(deg); c,s=math.cos(a),math.sin(a)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]])
def near(cen,r,skip):
    return [p for p in P if skip not in p[0] and np.linalg.norm((p[1]-cen)[[0,2]])<r+np.linalg.norm(p[3]) and (p[1][1]+np.abs(p[2][1])@p[3])>0.45 and 'Zones' not in p[0] and 'Paving' not in p[0]]
def report(name,A,cen,skip):
    N=near(cen,30,skip)
    for shrink in (0.05,-0.5,-1.0,-2.0):
        h=hits(A,N,shrink=shrink)
        print(name,'clearance' if shrink<0 else 'overlap',abs(shrink)*2 if shrink<0 else 0, dict(h) or 'none')
# poster: old pose -> new pose
A0=[p for p in P if 'CatCafe_Square_UpdatePoster' in p[0]]
old=np.array([20,0.1,-40]); Ro=roty(142.43); new=np.array([13.5,0.1,-50]); Rn=roty(159.44)
T=Rn@Ro.T
A=[(p[0],new+T@(p[1]-old),T@p[2],p[3]) for p in A0]
print('poster parts',len(A),'x range',min(a[1][0] for a in A).round(1),max(a[1][0] for a in A).round(1),'z',min(a[1][2] for a in A).round(1),max(a[1][2] for a in A).round(1))
report('poster@new',A,new,'UpdatePoster')
# sight lines: does any poster part box cross the segment spawn->stand or cannon->stand (xz)?
stand=np.array([28,-54.0])
for nm,src in (('spawn',np.array([0,-14.0])),('cannon',np.array([0,0.0]))):
    d=stand-src; L=np.linalg.norm(d); d/=L; n=np.array([-d[1],d[0]])
    m=min(abs((a[1][[0,2]]-src)@n)-np.linalg.norm(a[3][[0,2]]) for a in A if 0<(a[1][[0,2]]-src)@d<L)
    print('line',nm,'->stand: nearest poster part edge is',round(m,1),'studs off the line')
# arch from model json
t=json.load(open('/home/claude/Cat-Cafe/assets/cat-cafe/rbx/CatCafe_Harvest_Arch.model.json'))
at=np.array([-42,0.1,38]); Ra=roty(math.degrees(math.atan2(at[0],at[2])))
B=[]
def walk(x):
    for c in x.get('children',[]):
        p=c.get('properties',{})
        if 'Size' in p and 'CFrame' in p and p.get('Transparency',0)<0.95:
            cf=p['CFrame']['CFrame']; R=np.array(cf['orientation']); 
            B.append(('Arch.'+c['name'],at+Ra@np.array(cf['position']),Ra@R,np.array(p['Size'])/2))
        walk(c)
walk(t)
print('arch parts',len(B))
report('arch@(-42,38)',B,at,'Harvest_Arch')
