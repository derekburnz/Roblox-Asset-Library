"""A glossy toy render of the classic Roblox "bacon hair" default avatar look, for store art (Derek 2026-11-16: like
the trending tiles' bacon: smooth, shiny, big face, swoopy orange hair, black vest over a blue shirt, bare arms).
Run: python bacon_bl.py <out.png> <size> <pose> [az el]     Blender Z up, the character faces -Y."""
import math
import os
import sys

import bpy
from mathutils import Euler, Vector

OUT, SIZE, POSE = os.path.abspath(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
AZ = float(sys.argv[4]) if len(sys.argv) > 4 else 18.0
EL = float(sys.argv[5]) if len(sys.argv) > 5 else 4.0
R = math.radians

SKIN, HAIR, HAIR2 = (1.0, 0.93, 0.86), (0.93, 0.42, 0.10), (0.78, 0.30, 0.06)
BLUE, VEST, JEANS, SHOE, INK = (0.10, 0.42, 0.95), (0.035, 0.035, 0.045), (0.10, 0.22, 0.24), (0.93, 0.93, 0.95), (0.02, 0.02, 0.02)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
MATS = {}


def mat(rgb, rough=0.28, coat=0.6):
    key = (rgb, rough)
    if key in MATS:
        return MATS[key]
    m = bpy.data.materials.new("m"); m.use_nodes = True
    bs = m.node_tree.nodes["Principled BSDF"]
    bs.inputs["Base Color"].default_value = tuple(c ** 2.2 for c in rgb) + (1,)
    bs.inputs["Roughness"].default_value = rough
    for nm in ("Coat Weight", "Clearcoat"):
        if nm in bs.inputs:
            bs.inputs[nm].default_value = coat
    MATS[key] = m
    return m


def empty(name, parent, loc, rot=(0, 0, 0)):
    e = bpy.data.objects.new(name, None); sc.collection.objects.link(e)
    e.parent = parent; e.location = loc; e.rotation_euler = Euler([R(a) for a in rot], "XYZ")
    return e


def finish(ob, parent, rgb, bevel=0.0, smooth=True, rough=0.28):
    ob.parent = parent
    ob.data.materials.append(mat(rgb, rough))
    if bevel:
        b = ob.modifiers.new("b", "BEVEL"); b.width = bevel; b.segments = 5; b.limit_method = "ANGLE"
    if smooth:
        for p in ob.data.polygons:
            p.use_smooth = True
    return ob


def box(parent, loc, size, rgb, bevel=0.14):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    ob = bpy.context.object; ob.scale = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    ob.location = loc
    return finish(ob, parent, rgb, bevel)


def ball(parent, loc, r, rgb, scale=(1, 1, 1), rough=0.28):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=loc, segments=40, ring_count=20)
    ob = bpy.context.object; ob.scale = scale
    return finish(ob, parent, rgb, 0, True, rough)


def cyl(parent, loc, r, h, rgb, bevel=0.2):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=h, location=loc, vertices=48)
    return finish(bpy.context.object, parent, rgb, bevel)


def lock(parent, pts, rgb, rough=0.35):
    """A tapering lock of hair along (x, y, z, radius) points."""
    cu = bpy.data.curves.new("lock", "CURVE"); cu.dimensions = "3D"
    cu.bevel_depth = 1.0; cu.bevel_resolution = 6; cu.use_fill_caps = True
    sp = cu.splines.new("NURBS"); sp.points.add(len(pts) - 1)
    for p, (x, y, z, r) in zip(sp.points, pts):
        p.co = (x, y, z, 1); p.radius = r
    sp.use_endpoint_u = True; sp.order_u = min(4, len(pts)); sp.resolution_u = 12
    ob = bpy.data.objects.new("lock", cu); sc.collection.objects.link(ob)
    ob.parent = parent; cu.materials.append(mat(rgb, rough))
    return ob


# ---- poses: shoulder (rx forward-, ry out), elbow rx, hip (rx, ry), knee rx; L is the picture's left
POSES = {
    "stand": dict(),
    "cheer": dict(armL=(0, 150), armR=(0, -150), elbL=-10, elbR=-10, lean=-2, head=(2, 0, 0), legL=(0, 8), legR=(0, -8)),
    "hug": dict(armL=(-78, -22), armR=(-78, 22), elbL=-55, elbR=-55, lean=6, head=(4, 0, -10)),
    "net": dict(armL=(0, 152), elbL=-8, armR=(-25, -22), elbR=-35, lean=6, twist=10, head=(-6, 0, 8),
                legL=(26, 6), kneeL=18, legR=(-32, -6), kneeR=40),
    "point": dict(armR=(-20, -100), elbR=-4, armL=(0, 38), elbL=-100, lean=-3, head=(-2, 0, 14), legL=(0, 6), legR=(0, -6)),
    "ride": dict(armL=(0, 152), armR=(0, -152), lean=-12, legL=(-80, 12), kneeL=70, legR=(-80, -12), kneeR=70, head=(-12, 0, 0)),
    "run": dict(armL=(50, 12), elbL=-70, armR=(-60, -12), elbR=-70, lean=12, legL=(-50, 0), kneeL=50, legR=(40, 0), kneeR=70,
                head=(-8, 0, 0)),
    "bust": dict(armL=(0, 14), armR=(0, -14), head=(-2, 0, -8)),
}
P = POSES[POSE]
g = lambda k, d: P.get(k, d)

root = empty("root", None, (0, 0, 0), (g("lean", 0), 0, g("twist", 0)))
torso = empty("torso", root, (0, 0, 3.0))
box(torso, (0, 0, 0), (2.0, 1.0, 2.0), VEST, 0.16)
box(torso, (0, -0.47, -0.02), (1.1, 0.14, 1.9), BLUE, 0.05)            # the blue shirt between the vest's fronts
box(torso, (0, -0.44, -0.9), (2.02, 0.16, 0.22), BLUE, 0.05)             # its hem
for sx in (-1, 1):
    box(torso, (sx * 0.6, -0.5, 0.0), (0.12, 0.1, 1.9), (0.13, 0.13, 0.15), 0.03)   # the vest's lapel edge

neck = empty("neck", torso, (0, 0, 1.0), g("head", (0, 0, 0)))
neck.scale = (1.42, 1.42, 1.42)
head = cyl(neck, (0, 0, 0.66), 0.66, 1.22, SKIN, 0.24)
rh = 0.66
for sx in (-1, 1):                                                       # the classic face: two tall eyes and a smile
    x = sx * 0.21
    ball(neck, (x, -math.sqrt(rh * rh - x * x) + 0.01, 0.68), 0.125, INK, (0.72, 0.3, 1.3), 0.2)
    ball(neck, (x + 0.02, -math.sqrt(rh * rh - x * x) - 0.02, 0.76), 0.036, (1, 1, 1), (1, 0.4, 1), 0.2)
smile = []
for i in range(9):
    a = -1 + 2 * i / 8
    x = a * 0.3
    smile.append((x, -math.sqrt(rh * rh - x * x) - 0.005, 0.4 - 0.13 * (1 - a * a), 0.036))
lock(neck, smile, INK, 0.2)

# the hair: a cap, then locks sweeping from the crown over the brow and down the sides and back
ball(neck, (0, 0.08, 1.02), 0.74, HAIR, (1.06, 1.08, 0.86), 0.35)
crown = (0.05, 0.05, 1.62)
tips = [(-0.86, -0.46, 0.72, 0.5), (-0.62, -0.74, 0.78, 0.35), (-0.36, -0.86, 0.9, 0.2), (-0.1, -0.9, 0.84, 0.0),
        (0.18, -0.9, 0.92, -0.2), (0.44, -0.84, 0.8, -0.3), (0.7, -0.7, 0.74, -0.4), (0.9, -0.38, 0.66, -0.5),
        (-0.95, -0.05, 0.5, 0.5), (0.97, 0.0, 0.46, -0.5), (-0.86, 0.5, 0.42, 0.4), (0.86, 0.52, 0.42, -0.4),
        (-0.45, 0.9, 0.36, 0.2), (0.0, 0.98, 0.34, 0.0), (0.45, 0.9, 0.36, -0.2)]
for i, (tx, ty, tz, curl) in enumerate(tips):
    if ty < -0.3:
        tz += 0.36
    mx, my = tx * 0.78, ty * 0.78
    pts = [(crown[0], crown[1], crown[2] - 0.08, 0.3), (mx * 0.6, my * 0.6, 1.7, 0.38), (mx * 1.2, my * 1.2, 1.36, 0.34),
           (tx * 1.12, ty * 1.12, tz + 0.2, 0.22), (tx * 1.06 - curl * 0.16, ty * 1.04, tz - 0.08, 0.06)]
    lock(neck, pts, HAIR if i % 2 == 0 else HAIR2)

for side, sx in (("L", -1), ("R", 1)):
    arx, ary = g("arm" + side, (0, 8 * -sx))
    sh = empty("sh" + side, torso, (sx * 1.42, 0, 0.8), (arx, ary, 0))
    box(sh, (0, 0, -0.3), (0.9, 0.94, 0.9), VEST, 0.16)                 # the short sleeve
    box(sh, (0, 0, -0.72), (0.76, 0.8, 0.6), SKIN, 0.14)
    el = empty("el" + side, sh, (0, 0, -1.0), (g("elb" + side, 0), 0, 0))
    box(el, (0, 0, -0.46), (0.78, 0.82, 1.0), SKIN, 0.18)
    if POSE == "net" and side == "L":                                    # the catching net, held up
        bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=2.6, location=(0, 0, -2.1), vertices=24)
        finish(bpy.context.object, el, (0.55, 0.33, 0.16), 0.03)
        bpy.ops.mesh.primitive_torus_add(major_radius=0.95, minor_radius=0.1, location=(0, 0, -4.3), rotation=(R(90), 0, 0))
        finish(bpy.context.object, el, (0.98, 0.78, 0.2), 0)
        ball(el, (0, 0.6, -4.3), 0.9, (0.78, 0.92, 1.0), (1, 1.0, 1), 0.7)
    hrx, hry = g("leg" + side, (0, 0))
    hip = empty("hip" + side, torso, (sx * 0.5, 0, -1.0), (hrx, hry, 0))
    box(hip, (0, 0, -0.5), (0.98, 0.98, 1.1), JEANS, 0.14)
    kn = empty("kn" + side, hip, (0, 0, -1.0), (g("knee" + side, 0), 0, 0))
    box(kn, (0, 0, -0.36), (0.98, 0.98, 0.8), JEANS, 0.14)
    box(kn, (0, -0.06, -0.84), (1.04, 1.16, 0.4), SHOE, 0.14)

bpy.context.view_layer.update()
lo = Vector((1e9, 1e9, 1e9)); hi = -lo
for ob in sc.objects:
    if ob.type in ("MESH", "CURVE"):
        for c in ob.bound_box:
            w = ob.matrix_world @ Vector(c)
            lo = Vector(map(min, lo, w)); hi = Vector(map(max, hi, w))
if POSE == "bust":
    lo.z = 3.1
c = (lo + hi) / 2; r = (hi - lo).length / 2
az, el_ = R(AZ), R(EL)
d = Vector((math.sin(az) * math.cos(el_), -math.cos(az) * math.cos(el_), math.sin(el_)))
cam = bpy.data.objects.new("cam", bpy.data.cameras.new("cam")); sc.collection.objects.link(cam); sc.camera = cam
cam.data.lens = 60
cam.location = c + d * (r / math.sin(math.atan(18 / 60)) * 1.02)
cam.rotation_euler = (c - cam.location).to_track_quat("-Z", "Y").to_euler()


def light(loc, energy, rgb, size):
    L = bpy.data.lights.new("L", "AREA"); L.energy = energy; L.color = rgb; L.size = size
    ob = bpy.data.objects.new("L", L); ob.location = loc
    ob.rotation_euler = (c - Vector(loc)).to_track_quat("-Z", "Y").to_euler(); sc.collection.objects.link(ob)


side = Vector((d.y, -d.x, 0)).normalized()
light(c + d * r * 3 + side * r * 2.2 + Vector((0, 0, r * 1.6)), 95 * r * r, (1.0, 0.97, 0.94), r * 3)
light(c + d * r * 2.2 - side * r * 3, 30 * r * r, (0.85, 0.92, 1.0), r * 3)
light(c - d * r * 2.6 + side * r * 1.5 + Vector((0, 0, r * 2.0)), 80 * r * r, (1.0, 0.92, 0.85), r * 2)
light(c - d * r * 2.4 - side * r * 2.4 + Vector((0, 0, r * 0.4)), 55 * r * r, (0.75, 0.88, 1.0), r * 2)
w = bpy.data.worlds.new("W"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (1, 0.97, 0.98, 1)
w.node_tree.nodes["Background"].inputs[1].default_value = 0.6
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = 56; sc.cycles.use_denoising = True
sc.render.film_transparent = True
sc.render.resolution_x = sc.render.resolution_y = SIZE; sc.render.resolution_percentage = 100
sc.view_settings.view_transform = "Standard"
sc.render.filepath = OUT
bpy.ops.render.render(write_still=True)
print("wrote", OUT)
