import sys; sys.path.insert(0,'.')
from obb import *
P=load('ws2/world-parts.tsv')
def show(ka,kb,box,minh=0.0):
    x0,x1,z0,z1=box
    A=[p for p in P if ka in p[0] and x0<p[1][0]<x1 and z0<p[1][2]<z1]
    B=[p for p in P if kb in p[0] and ka not in p[0] and x0-6<p[1][0]<x1+6 and z0-6<p[1][2]<z1+6]
    print('==',ka,'vs',kb,len(A),len(B))
    for a in A:
        for b in B:
            if np.linalg.norm(b[1]-a[1])>np.linalg.norm(a[3])+np.linalg.norm(b[3]): continue
            if sat(a,b,0.04):
                print('  ',a[0].split('.')[-1],a[1].round(2),(2*a[3]).round(2),'<>',b[0].split('.')[-1],b[1].round(2),(2*b[3]).round(2))
show('Neighbourhood.Nook','Neighbourhood.Set',(60,95,2065,2095))
show('Gates.WoodsGate','Woods.Camp.CampSet',(-1770,-1740,-25,25))
show('Cannons.WoodsCannon','Woods.Camp.CampSet',(-1740,-1710,-15,15))
show('CrateStack','Building_Warehouse',(-1455,-1435,-1495,-1475))
show('CampExtras.RelicMuseum','Gates.RuinsGate',(1405,1425,1090,1105))
