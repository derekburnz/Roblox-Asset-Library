"""Toolkit locator on one builder function at every yaw 0..89: qa_rot.py -- module.func"""
import importlib, math, os, sys
argv = sys.argv[sys.argv.index("--") + 1:]
sys.argv = [sys.argv[0]]
sys.path.insert(0, os.environ["BLDIR"])
import toolkit_qa as tq
import bpy
tq.common.reset_scene()
mat = tq.common.palette_material(os.path.join(tq.ROOT, "assets", "cat-cafe", "exports", tq.palette.TEXTURE_NAME + ".png"))
mod, fn = argv[0].split(".")
objs = [o for o in getattr(importlib.import_module(mod), fn)(mat) if o.type == "MESH"]
bad = []
for deg in range(0, 90):
    for o in objs:
        o.rotation_euler[2] = math.radians(deg)
        o.location = (37.0, -11.0, 0.0)
    bpy.context.view_layer.update()
    loc = tq.locate(objs)
    v = sum(n for _, n in loc["visible"])
    if v:
        bad.append(deg)
print(argv[0], "bad yaws", bad, flush=True)
