import bpy,sys,math
from mathutils import Vector
glb,out=sys.argv[-2],sys.argv[-1]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb)
objs=[o for o in bpy.data.objects if o.type=='MESH']
def center(sub):
    for o in objs:
        if sub in o.name:
            return sum((o.matrix_world@Vector(c) for c in o.bound_box),Vector())/8
sc=bpy.context.scene
sc.render.engine='CYCLES';sc.cycles.samples=12;sc.cycles.device='CPU'
sc.render.resolution_x,sc.render.resolution_y=800,500
w=bpy.data.worlds.new('w');sc.world=w;w.use_nodes=True;w.node_tree.nodes['Background'].inputs[1].default_value=1.2
sun=bpy.data.objects.new('s',bpy.data.lights.new('s','SUN'));sun.data.energy=3;sun.rotation_euler=(0.8,0.2,0.5);sc.collection.objects.link(sun)
cam=bpy.data.objects.new('c',bpy.data.cameras.new('c'));sc.collection.objects.link(cam);sc.camera=cam
for tag,sub,d in (('pillar','_001_Pillar',(3,-9,3)),('lamp','_Lamp',(4,-8,2)),('patch','FlowerPatch_Flowers',(5,-6,4)),('stone','WallStone',(0,-16,2))):
    c=center(sub)
    if c is None: print('none',sub);continue
    cam.location=c+Vector(d)
    cam.rotation_euler=(c-cam.location).to_track_quat('-Z','Y').to_euler()
    sc.render.filepath=f'{out}_{tag}.png';bpy.ops.render.render(write_still=True)
