import bpy,sys
from mathutils import Vector
glb,out=sys.argv[-2],sys.argv[-1]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
sc=bpy.context.scene
sc.render.engine='CYCLES';sc.cycles.samples=12;sc.cycles.device='CPU'
sc.render.resolution_x,sc.render.resolution_y=900,500
w=bpy.data.worlds.new('w');sc.world=w;w.use_nodes=True;w.node_tree.nodes['Background'].inputs[1].default_value=1.2
sun=bpy.data.objects.new('s',bpy.data.lights.new('s','SUN'));sun.data.energy=3;sun.rotation_euler=(0.8,0.2,0.5);sc.collection.objects.link(sun)
cam=bpy.data.objects.new('c',bpy.data.cameras.new('c'));sc.collection.objects.link(cam);sc.camera=cam;cam.data.clip_end=5000
for tag,loc,look in (('north',(0,60,14),(40,300,10)),('east',(-40,0,14),(-300,60,10)),('west',(40,0,14),(300,-40,10))):
    cam.location=Vector(loc)
    cam.rotation_euler=(Vector(look)-cam.location).to_track_quat('-Z','Y').to_euler()
    sc.render.filepath=f'{out}_{tag}.png';bpy.ops.render.render(write_still=True)
