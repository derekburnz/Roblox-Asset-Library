"""usage: blender python scene.py -- OUT rbxdir models cams.json ; models: Name or Name@x,z,rot (Roblox set space)"""
import sys, os, json, math
sys.path.insert(0, "/home/user/Cat-Cafe/assets/cat-cafe/blender")
import bpy
from mathutils import Vector, Matrix
import common, rbx_preview as rp
argv = sys.argv[sys.argv.index("--") + 1:]
out, rbxdir, models, cams = argv[0], argv[1], argv[2].split(","), json.load(open(argv[3]))
common.reset_scene()
objs = []
for m in models:
    name, _, at = m.partition("@")
    path = os.path.join(rbxdir, name + ".model.json")
    if not os.path.exists(path):
        path = os.path.join(rp.ROOT, "assets/cat-cafe/rbx", name + ".model.json")
    new = rp.build(path, name)
    if at:
        v = [float(t) for t in at.split(";")] + [0.0, 1.0][len(at.split(";")) - 3:]
        x, z, r, y, sc = v[:5]
        M = (rp.CT.to_4x4() @ Matrix.Translation((x, y, z)) @ Matrix.Rotation(math.radians(r), 4, "Y")
             @ Matrix.Scale(sc, 4) @ rp.CT.transposed().to_4x4())
        for ob in new:
            ob.data.transform(M)
    objs += new
for ob in list(objs):
    mm = ob.data.materials[0] if ob.data.materials else None
    if mm and mm.node_tree.nodes["Principled BSDF"].inputs["Alpha"].default_value < 0.01:
        bpy.data.objects.remove(ob, do_unlink=True)
def B(v):
    return rp.CT @ Vector(v)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = 16; sc.cycles.use_denoising = True
sc.view_settings.view_transform = "Standard"; sc.render.image_settings.file_format = "PNG"
common._ensure_floor(); fl = bpy.data.objects.get("_PreviewFloor"); fl.location.z = -0.05; fl.scale = (80, 80, 1)
common._ensure_lights(True)
w = bpy.data.worlds.get("World") or bpy.data.worlds.new("World"); sc.world = w
cd = bpy.data.cameras.new("_AreaCam"); cam = bpy.data.objects.new("_AreaCam", cd); sc.collection.objects.link(cam); sc.camera = cam
cd.clip_start = 0.5; cd.clip_end = 3000
os.makedirs(out, exist_ok=True)
for c in cams:
    cd.lens = c.get("lens", 24)
    sc.render.resolution_x, sc.render.resolution_y = c.get("res", [800, 520])
    p, t = B(c["pos"]), B(c["look"])
    cam.location = p
    cam.rotation_euler = (t - p).to_track_quat("-Z", "Y").to_euler()
    sc.render.filepath = os.path.join(out, c["name"] + ".png")
    bpy.ops.render.render(write_still=True)
    print("rendered", sc.render.filepath)
