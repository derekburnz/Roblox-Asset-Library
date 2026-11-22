import bpy,sys,re
from mathutils import Vector
glb,out=sys.argv[-2],sys.argv[-1]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
objs=[o for o in bpy.data.objects if o.type=='MESH']
sc=bpy.context.scene
sc.render.engine='CYCLES';sc.cycles.samples=12;sc.cycles.device='CPU'
sc.render.resolution_x,sc.render.resolution_y=600,400
w=bpy.data.worlds.new('w');sc.world=w;w.use_nodes=True;w.node_tree.nodes['Background'].inputs[1].default_value=2.2
sun=bpy.data.objects.new('s',bpy.data.lights.new('s','SUN'));sun.data.energy=3;sun.rotation_euler=(0.8,0.2,0.5);sc.collection.objects.link(sun)
cam=bpy.data.objects.new('c',bpy.data.cameras.new('c'));sc.collection.objects.link(cam);sc.camera=cam
cam.data.clip_end=3000
D4=[(1,0,0.4),(-1,0,0.4),(0,1,0.4),(0,-1,0.4)]
for tag,sub,idx,k in (('wall','WallBroken',2,1.0),('rubble','Rubble',3,1.6),('colonnade','WallColonnade',1,1.0)):
    m=sorted([o for o in objs if re.search(r'_\d+_'+sub+r'(\.\d+)?$',o.name)],key=lambda o:o.name)
    if not m: print('none',sub,[o.name for o in objs[:5]]);continue
    t=m[min(idx,len(m)-1)]
    num=re.search(r'_(\d+)_'+sub,t.name).group(1)
    grp=[o for o in objs if re.search(r'_'+num+'_'+sub,o.name)]
    for o in objs: o.hide_render=o not in grp
    pts=[o.matrix_world@Vector(c) for o in grp for c in o.bound_box]
    lo=Vector([min(p[i] for p in pts) for i in range(3)]);hi=Vector([max(p[i] for p in pts) for i in range(3)])
    c=(lo+hi)/2;sz=hi-lo
    for j,d in enumerate(D4):
        cam.location=c+Vector(d).normalized()*max(sz)*k
        cam.rotation_euler=(c-cam.location).to_track_quat('-Z','Y').to_euler()
        sc.render.filepath=f'{out}_{tag}{j}.png';bpy.ops.render.render(write_still=True)
