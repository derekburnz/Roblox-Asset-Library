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
w=bpy.data.worlds.new('w');sc.world=w;w.use_nodes=True;w.node_tree.nodes['Background'].inputs[1].default_value=2.5
sun=bpy.data.objects.new('s',bpy.data.lights.new('s','SUN'));sun.data.energy=3;sun.rotation_euler=(0.8,0.2,0.5);sc.collection.objects.link(sun)
cam=bpy.data.objects.new('c',bpy.data.cameras.new('c'));sc.collection.objects.link(cam);sc.camera=cam
cam.data.clip_end=2000
D4=[(1,0,0.35),(-1,0,0.35),(0,1,0.35),(0,-1,0.35)]
sc.render.resolution_x,sc.render.resolution_y=500,400
for tag,sub,idx in (('oldtree','OldTree',5),('palisade','WallPalisade',0),('drystone','WallDrystone',0)):
    m=sorted([o for o in objs if sub in o.name],key=lambda o:o.name)
    tgt=m[min(idx,len(m)-1)]
    for o in objs: o.hide_render=(o is not tgt)
    c,sz=box(sub,idx)
    for j,d in enumerate(D4):
        cam.location=c+Vector(d).normalized()*max(sz)*1.25
        cam.rotation_euler=(c-cam.location).to_track_quat('-Z','Y').to_euler()
        sc.render.filepath=f'{out}_{tag}{j}.png';bpy.ops.render.render(write_still=True)
