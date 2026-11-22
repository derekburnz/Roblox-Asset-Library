"""Render an area from chosen cameras. usage: python arearender.py OUT models(comma) cams.json
cams: [{"name":..,"pos":[rx,ry,rz],"look":[rx,ry,rz],"lens":24,"res":[1200,800]}] in ROBLOX coords."""
import sys, os, json, math
sys.path.insert(0, "/home/user/Cat-Cafe/assets/cat-cafe/blender")
import bpy
from mathutils import Vector
import common, rbx_preview as rp
out, models, cams = sys.argv[1], sys.argv[2].split(","), json.load(open(sys.argv[3]))
common.reset_scene()
objs = []
for m in models:
    objs += rp.build(os.path.join(rp.ROOT, "assets/cat-cafe/rbx", m + ".model.json"), m)
keep = []
for ob in objs:
    m = ob.data.materials[0] if ob.data.materials else None
    if m and m.node_tree.nodes["Principled BSDF"].inputs["Alpha"].default_value < 0.01:
        bpy.data.objects.remove(ob, do_unlink=True)
    else:
        keep.append(ob)
objs = keep
lo, hi = common.bounds(objs)
print("bounds blender", tuple(lo), tuple(hi))
def B(v):  # roblox -> blender via CT
    return rp.CT @ Vector(v)
sc = bpy.context.scene
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = 16; sc.cycles.use_denoising = True
sc.view_settings.view_transform = "Standard"; sc.render.image_settings.file_format = "PNG"
common._ensure_floor(); fl = bpy.data.objects.get("_PreviewFloor"); fl.location.z = -0.05; fl.scale = (60, 60, 1)
common._ensure_lights(True)
w = bpy.data.worlds.get("World") or bpy.data.worlds.new("World"); sc.world = w
cd = bpy.data.cameras.new("_AreaCam"); cam = bpy.data.objects.new("_AreaCam", cd); sc.collection.objects.link(cam); sc.camera = cam
cd.clip_start = 0.5; cd.clip_end = 3000
os.makedirs(out, exist_ok=True)
for c in cams:
    cd.lens = c.get("lens", 24)
    sc.render.resolution_x, sc.render.resolution_y = c.get("res", [1200, 800])
    p, t = B(c["pos"]), B(c["look"])
    cam.location = p
    cam.rotation_euler = (t - p).to_track_quat("-Z", "Y").to_euler()
    sc.render.filepath = os.path.join(out, c["name"] + ".png")
    bpy.ops.render.render(write_still=True)
    print("rendered", sc.render.filepath)
