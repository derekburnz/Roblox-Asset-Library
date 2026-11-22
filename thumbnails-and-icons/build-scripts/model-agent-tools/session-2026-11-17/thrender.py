import bpy,sys
from mathutils import Vector
out=sys.argv[-1];glbs=sys.argv[sys.argv.index('--')+1:-1]
bpy.ops.wm.read_factory_settings(use_empty=True)
for g in glbs: bpy.ops.import_scene.gltf(filepath=g)
objs=[o for o in bpy.data.objects if o.type=='MESH']
for o in objs:
    if 'Plot_Cafe_' in o.name and '_Awning' in o.name: o.hide_render=True
sc=bpy.context.scene
sc.render.engine='CYCLES';sc.cycles.samples=16;sc.cycles.device='CPU'
sc.render.resolution_x,sc.render.resolution_y=900,500
w=bpy.data.worlds.new('w');sc.world=w;w.use_nodes=True;w.node_tree.nodes['Background'].inputs[1].default_value=2.2
sun=bpy.data.objects.new('s',bpy.data.lights.new('s','SUN'));sun.data.energy=3;sun.rotation_euler=(1.0,0.0,-0.3);sc.collection.objects.link(sun)
cam=bpy.data.objects.new('c',bpy.data.cameras.new('c'));sc.collection.objects.link(cam);sc.camera=cam;cam.data.clip_end=3000
vis=[o for o in objs if not o.hide_render]
pts=[o.matrix_world@Vector(c) for o in vis for c in o.bound_box]
lo=Vector([min(p[i] for p in pts) for i in range(3)]);hi=Vector([max(p[i] for p in pts) for i in range(3)])
c=(lo+hi)/2;c.z=9
for j,d in enumerate([(0,-1,0.15),(0.6,-1,0.3)]):
    cam.location=c+Vector(d).normalized()*(hi.x-lo.x)*1.7
    cam.rotation_euler=(c-cam.location).to_track_quat('-Z','Y').to_euler()
    sc.render.filepath=f'{out}_{j}.png';bpy.ops.render.render(write_still=True)
