"""Render Part models (rbx/*.model.json) as Roblox would show them, from cameras given in Roblox space.
usage: python rbx_shot.py -- <blender dir> <out dir> <prefix> <model.json[@x,z,roty[,y]]>... -- <name:ax,ay,az:lx,ly,lz[:lens]>...
Optional env: FLOOR=<palette swatch> for the ground, NIGHT=1 for the night lights, SAMPLES, RES=w,h, ORTHO=<scale>
(orthographic camera of that width)."""
import math
import os
import sys

argv = sys.argv[sys.argv.index("--") + 1:]
split = argv.index("--", 3)
blender_dir, out, prefix = argv[:3]
models, shots = argv[3:split], argv[split + 1:]
sys.path.insert(0, blender_dir)
import bpy  # noqa: E402
from mathutils import Matrix, Vector  # noqa: E402

import common  # noqa: E402
import rbx_preview  # noqa: E402

CT = common.TO_ROBLOX.transposed().to_4x4()
CTi = CT.inverted()


def B(p):
    return (CT @ Vector((*p, 1.0))).to_3d()


common.reset_scene()
import json  # noqa: E402
import tempfile  # noqa: E402


def _visible(path):
    """A copy of the model without parts that are invisible in game (Transparency 1: barriers, trusses, volumes)."""
    tree = json.load(open(path))

    count = [0]

    def prune(n):
        n["children"] = [c for c in n.get("children", []) if c.get("properties", {}).get("Transparency", 0) < 1]
        for c in n["children"]:
            size = c.get("properties", {}).get("Size")
            if size:            # Cycles shades overlapping coplanar faces black (Roblox does not): split them a hair
                for i in range(3):
                    size[i] += 0.004 * ((count[0] + i) % 3)
                count[0] += 1
            prune(c)
    prune(tree)
    fd, tmp = tempfile.mkstemp(suffix=".model.json")
    with os.fdopen(fd, "w") as f:
        json.dump(tree, f)
    return tmp


for k, spec in enumerate(models):
    path, _, at = spec.partition("@")
    objs = rbx_preview.build(_visible(path), f"m{k}")
    if at:
        v = [float(t) for t in at.split(",")]
        x, z, ry, y = v[0], v[1], v[2], (v[3] if len(v) > 3 else 0.0)
        M = Matrix.Translation((x, y, z)) @ Matrix.Rotation(math.radians(ry), 4, "Y")
        W = CT @ M @ CTi
        for ob in objs:
            ob.matrix_world = W @ ob.matrix_world
sc = bpy.context.scene
sc.render.engine = "CYCLES"
sc.cycles.device = "CPU"
sc.cycles.samples = int(os.environ.get("SAMPLES", 24))
sc.cycles.use_denoising = True
rx, ry_ = (int(v) for v in os.environ.get("RES", "1280,800").split(","))
sc.render.resolution_x, sc.render.resolution_y = rx, ry_
sc.view_settings.view_transform = "Standard"
common._ensure_floor(os.environ.get("FLOOR", "floor_tile"), size=600)       # a palette swatch name
common._ensure_lights(not os.environ.get("NIGHT"))
if os.environ.get("AMBIENT"):           # Roblox's Ambient lights roofed rooms with no shadow: shadowless suns round about
    for i, (ex, ez) in enumerate(((10, 0), (70, 0), (70, 120), (70, 240))):
        amb = bpy.data.lights.new(f"_Amb{i}", "SUN")
        amb.energy = float(os.environ["AMBIENT"]) / 4
        amb.use_shadow = False
        ao = bpy.data.objects.new(f"_Amb{i}", amb)
        ao.rotation_euler = (math.radians(ex), 0, math.radians(ez))
        sc.collection.objects.link(ao)
cd = bpy.data.cameras.new("_Cam")
cam = bpy.data.objects.new("_Cam", cd)
sc.collection.objects.link(cam)
sc.camera = cam
cd.clip_start, cd.clip_end = 0.1, 1500
if os.environ.get("ORTHO"):
    cd.type, cd.ortho_scale = "ORTHO", float(os.environ["ORTHO"])
os.makedirs(out, exist_ok=True)
for shot in shots:
    parts = shot.split(":")
    name, at, look = parts[0], [float(v) for v in parts[1].split(",")], [float(v) for v in parts[2].split(",")]
    cd.lens = float(parts[3]) if len(parts) > 3 else 28
    cam.location = B(at)
    cam.rotation_euler = (B(look) - B(at)).to_track_quat("-Z", "Y").to_euler()
    sc.render.filepath = os.path.join(out, f"{prefix}_{name}.png")
    bpy.ops.render.render(write_still=True)
    print("wrote", sc.render.filepath, flush=True)
