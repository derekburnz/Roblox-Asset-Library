import bpy,sys,math
from mathutils import Vector
glb,out=sys.argv[-2],sys.argv[-1]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
objs=[o for o in bpy.data.objects if o.type=='MESH']
def box(sub,idx=0):
    m=[o for o in objs if sub in o.name]
    m.sort(key=lambda o:o.name)
    if not m: return None
    o=m[min(idx,len(m)-1)]
    pts=[o.matrix_world@Vector(c) for c in o.bound_box]
    lo=Vector((min(p.x for p in pts),min(p.y for p in pts),min(p.z for p in pts)))
    hi=Vector((max(p.x for p in pts),max(p.y for p in pts),max(p.z for p in pts)))
    return (lo+hi)/2,(hi-lo)
sc=bpy.context.scene
sc.render.engine='CYCLES';sc.cycles.samples=12;sc.cycles.device='CPU'
sc.render.resolution_x,sc.render.resolution_y=700,500
w=bpy.data.worlds.new('w');sc.world=w;w.use_nodes=True;w.node_tree.nodes['Background'].inputs[1].default_value=1.2
sun=bpy.data.objects.new('s',bpy.data.lights.new('s','SUN'));sun.data.energy=3;sun.rotation_euler=(0.8,0.2,0.5);sc.collection.objects.link(sun)
cam=bpy.data.objects.new('c',bpy.data.cameras.new('c'));sc.collection.objects.link(cam);sc.camera=cam
cam.data.clip_end=2000
for tag,sub,idx,dirs,k in (('pine','PineTall',40,[(1,-1,0.25)],1.5),('oldtree','OldTree',5,[(1,0,0.2),(-1,0,0.2),(0,1,0.2),(0,-1,0.2)],1.6),('palisade','WallPalisade',0,[(1,0,0.3),(-1,0,0.3),(0,1,0.3),(0,-1,0.3)],1.0),('drystone','WallDrystone',0,[(1,0,0.3),(-1,0,0.3),(0,1,0.3),(0,-1,0.3)],1.0),('fern','Fern',3,[(1,-1,0.8)],2.2)):
    r=box(sub,idx)
    if r is None: print('none',sub);continue
    c,sz=r
    for j,d in enumerate(dirs):
        cam.location=c+Vector(d).normalized()*max(sz)*k
        cam.rotation_euler=(c-cam.location).to_track_quat('-Z','Y').to_euler()
        sc.render.filepath=f'{out}_{tag}{j}.png';bpy.ops.render.render(write_still=True)
