"""F78 checkpoint: each new themed cat walking (A), sitting (B) and at work in all four jobs (B in the role outfit,
F71 rules: role pieces in a prop slot stay off; an Entertainer with Head and Back props wears the party hat in place
of its head prop), a plain Tabby for scale; front and back views. Also a clip test: every prop object against every
outfit piece it is worn with.
usage: python f78_roles.py -- <blender_dir> <out_dir> [Cat,Cat]"""
import os
import sys

argv = sys.argv[sys.argv.index("--") + 1:]
BL, OUT = argv[0], argv[1]
sys.path.insert(0, BL)
import bpy  # noqa: E402
from mathutils import Matrix  # noqa: E402
from mathutils.bvhtree import BVHTree  # noqa: E402

import accessories  # noqa: E402
import cats  # noqa: E402
import common  # noqa: E402
import gold  # noqa: E402
import palette  # noqa: E402
import poses  # noqa: E402
import props  # noqa: E402

NEW = ["Binbag", "Taxi", "Neon", "Birdwatch", "Duckling", "Balloon", "Builder", "Gardener", "Gnome", "Plumber"]
ONLY = argv[2].split(",") if len(argv) > 2 else NEW
SLOT = {"BaristaCap": "Head", "Boater": "Head", "PartyHat": "Head", "Cape": "Back"}      # Catalog.outfitPieceSlots
ROLES = ("barista", "waiter", "greeter", "entertainer")
os.makedirs(OUT, exist_ok=True)

common.reset_scene()
png = os.path.join(OUT, "pal.png")
palette.write_palette_png(png)
palette.write_metal_png(png.replace(".png", "_Metal.png"))
mat = common.palette_material(png)
built = {n: fn(mat) for n, (fn, _) in accessories.ASSETS.items()}
for objs in built.values():
    for ob in objs:
        ob.hide_render = True


def dress(name, role):
    """(outfit pieces worn, prop object suffixes hidden) for a cat working in a role."""
    slots = {props.slot(name), props.slot2(name)} - {None}
    hidden = set()
    if role == "entertainer" and {"Head", "Back"} <= slots:
        slots.discard("Head")                       # F71: the party hat in place of its head prop
        hidden = {"_Prop", "_Prop_Glass"} if props.slot(name) == "Head" else {"_Prop2"}
    return [p for p in accessories.ROLE_OUTFITS[role] if SLOT.get(p) not in slots], hidden


def copies(objs, W, skip=()):
    out = []
    for ob in objs:
        if ob.name.endswith(tuple(skip)) if skip else False:
            continue
        c = ob.copy()
        c.name = "_v_" + ob.name
        c.matrix_world = W @ ob.matrix_world
        c.hide_render = False
        bpy.context.scene.collection.objects.link(c)
        out.append(c)
    return out


def ortho(objs, path, az, el=10, res=(1800, 400), samples=20):
    """An orthographic three-quarter view of objs framed to fit (no perspective shrink along the row)."""
    import math
    from mathutils import Vector
    common.render_preview(objs[:1], path, res=(8, 8), samples=1)          # floor, lights and camera exist
    sc = bpy.context.scene
    sc.cycles.samples = samples
    sc.render.resolution_x, sc.render.resolution_y = res
    lo, hi = common.bounds(objs)
    c = (lo + hi) / 2
    a, e = math.radians(az), math.radians(el)
    d = Vector((math.sin(a) * math.cos(e), -math.cos(a) * math.cos(e), math.sin(e)))
    cam = sc.camera
    cam.data.type = "ORTHO"
    cam.location = c + d * 40
    cam.rotation_euler = (-d).to_track_quat("-Z", "Y").to_euler()
    right = Vector((math.cos(a), math.sin(a), 0))
    xs = [right.dot(Vector(v)) for v in ((lo.x, lo.y, 0), (hi.x, lo.y, 0), (lo.x, hi.y, 0), (hi.x, hi.y, 0))]
    w = (max(xs) - min(xs)) * 1.04
    h = (hi.z - lo.z) * 1.25 * res[0] / res[1]
    cam.data.ortho_scale = max(w, h)
    cam.data.clip_end = 200
    for ob in sc.objects:
        if ob.type == "MESH" and not ob.name.startswith("_"):
            ob.hide_render = True
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)


def tree(ob):
    M = ob.matrix_world
    return BVHTree.FromPolygons([M @ v.co for v in ob.data.vertices], [p.vertices[:] for p in ob.data.polygons])


report = []
for name in ONLY:
    spec = cats.ROSTER[name]
    walk = cats.build_cat(name, mat, body="walk")
    sit = cats.build_cat(name, mat, body="sit")
    tabby = cats.build_cat("Tabby", mat, body="sit")
    gwalk = gold.build_gold(name, mat, "walk")
    bpy.context.view_layer.update()
    for ob in walk + sit + tabby + gwalk:
        ob.hide_render = True
    shown = []
    step = 1.55
    x = 0.0
    shown += copies(walk, Matrix.Translation((x, 0, 0)))
    x += step * 1.1
    shown += copies(gwalk, Matrix.Translation((x, 0, 0)))
    x += step * 1.05
    shown += copies(sit, Matrix.Translation((x, 0, 0)))
    for role in ROLES:
        x += step
        W = Matrix.Translation((x, 0, 0))
        pieces, hidden = dress(name, role)
        cat_c = copies(sit, W, skip=hidden)
        acc = poses.accessory_copies(built, sit, spec, "sit", pieces, world=W)
        shown += cat_c + acc
        for p in (c for c in cat_c if "_Prop" in c.name):
            for a in acc:
                n = len(tree(p).overlap(tree(a)))
                report.append(f"{name} {role}: {p.name[3:]} x {a.name[3:]}: {n} face pairs" if n else None)
        report.append(f"{name} {role}: wears {', '.join(pieces)}" + (f"; hides {', '.join(sorted(hidden))}" if hidden
                                                                    else ""))
    x += step
    shown += copies(tabby, Matrix.Translation((x, 0, 0)))
    for view, az in (("front", 18), ("back", 198)):
        ortho(shown, os.path.join(OUT, f"{name}_{view}.png"), az)
    poses.cleanup(shown)
    for ob in walk + sit + tabby + gwalk:
        bpy.data.objects.remove(ob, do_unlink=True)
    print(name, "done", flush=True)
open(os.path.join(OUT, "clip_report.txt"), "w").write("\n".join(r for r in report if r) + "\n")
print("\n".join(r for r in report if r))
