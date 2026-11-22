"""The REAL default Roblox bacon avatar rendered with glossy thumbnail lighting: the real Pal Hair mesh and texture and the
real classic shirt and pants templates (pulled from Roblox by Sync, 2026-11-16) on a blocky body with the classic rounded head.
Run: python bacon_real.py <out.png> <size> <pose> [az el]      Blender Z up, the character faces +Y.
Env: BACON_SRC (folder), BACON_SHIRT, BACON_PANTS (template png names), BACON_SKIN "r,g,b", BACON_HEAD (head and hair scale)."""
import math, os, sys
import bpy, bmesh
from mathutils import Euler, Vector
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("BACON_SRC", os.path.join(HERE, "real"))
OUT, SIZE, POSE = os.path.abspath(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
AZ = float(sys.argv[4]) if len(sys.argv) > 4 else 18.0
EL = float(sys.argv[5]) if len(sys.argv) > 5 else 4.0
HEAD_K = float(os.environ.get("BACON_HEAD", "1.2"))
SHIRT = os.environ.get("BACON_SHIRT", "shirt-template-382538294.png")
PANTS = os.environ.get("BACON_PANTS", "pants-template-398633811.png")
SKIN = tuple(float(v) for v in os.environ.get("BACON_SKIN", "0.66,0.67,0.69").split(","))
R = math.radians
TW, TH = 585, 559

# ---- the three body textures: skin with the clothes laid over it, as Roblox does
def layer(*names):
    im = Image.new("RGBA", (TW, TH), tuple(int(c * 255) for c in SKIN) + (255,))
    for n in names:
        t = Image.open(os.path.join(SRC, n)).convert("RGBA").resize((TW, TH))
        im.alpha_composite(t)
    p = os.path.join(SRC, "_tex_%d_" % os.getpid() + "_".join(n[:5] for n in names) + ".png"); im.convert("RGB").save(p)
    return p

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene


def mat(name, png=None, rgb=None, rough=0.3, coat=0.5, gain=1.0, spec=0.5):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; bs = nt.nodes["Principled BSDF"]
    bs.inputs["Roughness"].default_value = rough
    for nm in ("Specular IOR Level", "Specular"):
        if nm in bs.inputs:
            bs.inputs[nm].default_value = spec
    for nm in ("Coat Weight", "Clearcoat"):
        if nm in bs.inputs:
            bs.inputs[nm].default_value = coat
    if png:
        t = nt.nodes.new("ShaderNodeTexImage"); t.image = bpy.data.images.load(png)
        if gain != 1.0:
            mx = nt.nodes.new("ShaderNodeMixRGB"); mx.blend_type = "MULTIPLY"; mx.inputs[0].default_value = 1.0
            mx.inputs[2].default_value = (gain, gain * 0.86, gain * 0.62, 1)
            nt.links.new(t.outputs["Color"], mx.inputs[1]); nt.links.new(mx.outputs[0], bs.inputs["Base Color"])
        else:
            nt.links.new(t.outputs["Color"], bs.inputs["Base Color"])
    else:
        bs.inputs["Base Color"].default_value = tuple(c ** 2.2 for c in rgb) + (1,)
    return m


M_TORSO = mat("torso", layer(PANTS, SHIRT), rough=0.55, coat=0.0, spec=0.15); M_ARM = mat("arm", layer(SHIRT), rough=0.55, coat=0.0, spec=0.15); M_LEG = mat("leg", layer(PANTS), rough=0.55, coat=0.0, spec=0.15)
M_SKIN = mat("skin", rgb=SKIN); M_INK = mat("ink", rgb=(0.02, 0.02, 0.02), rough=0.25); M_HAIR = mat("hair", os.path.join(SRC, "palhair-texture-6858317867.png"), rough=0.36, coat=0.4, gain=float(os.environ.get("BACON_HAIR_GAIN", "2.2")))
TORSO = {"F": (231, 74, 128, 128), "B": (427, 74, 128, 128), "R": (165, 74, 64, 128), "L": (361, 74, 64, 128), "U": (231, 8, 128, 64), "D": (231, 204, 128, 64)}
LIMB_R = {"F": (217, 355, 64, 128), "R": (151, 355, 64, 128), "B": (85, 355, 64, 128), "L": (19, 355, 64, 128), "U": (217, 289, 64, 64), "D": (217, 485, 64, 64)}
LIMB_L = {"F": (308, 355, 64, 128), "L": (374, 355, 64, 128), "B": (440, 355, 64, 128), "R": (506, 355, 64, 128), "U": (308, 289, 64, 64), "D": (308, 485, 64, 64)}


def box(parent, centre, size, material, rects, t0=0.0, t1=1.0, bevel=0.1):
    """A box whose faces take their picture from a classic clothing template; t0..t1 is the slice of the limb's height."""
    me = bpy.data.meshes.new("box"); bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector((v.co.x * size[0], v.co.y * size[1], v.co.z * size[2]))
    uv = bm.loops.layers.uv.new("uv")
    for f in bm.faces:
        n = f.normal
        if abs(n.y) > 0.5:
            key, right, wd = ("F", Vector((-1, 0, 0)), size[0]) if n.y > 0 else ("B", Vector((1, 0, 0)), size[0])
        elif abs(n.x) > 0.5:
            key, right, wd = ("R", Vector((0, 1, 0)), size[1]) if n.x > 0 else ("L", Vector((0, -1, 0)), size[1])
        else:
            key, right, wd = ("U" if n.z > 0 else "D"), Vector((-1, 0, 0)), size[0]
        x0, y0, w, h = rects[key]
        for l in f.loops:
            p = l.vert.co
            s = p.dot(right) / wd + 0.5
            if key in ("U", "D"):
                t = (0.5 - p.y / size[1]) if key == "U" else (0.5 + p.y / size[1])
            else:
                t = t0 + (0.5 - p.z / size[2]) * (t1 - t0)
            l[uv].uv = ((x0 + s * w) / TW, 1 - (y0 + t * h) / TH)
        f.smooth = True
    bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new("box", me); sc.collection.objects.link(ob)
    ob.parent = parent; ob.location = centre; me.materials.append(material)
    if bevel:
        b = ob.modifiers.new("b", "BEVEL"); b.width = bevel; b.segments = 5; b.limit_method = "ANGLE"
    return ob


def empty(name, parent, loc):
    e = bpy.data.objects.new(name, None); sc.collection.objects.link(e); e.parent = parent; e.location = loc
    return e


POSES = {
    "stand": dict(armL=(0, 6), armR=(0, -6)),
    "cheer": dict(armL=(0, 150), armR=(0, -150), elbL=-10, elbR=-10, lean=-2, head=(2, 0, 0), legL=(0, 8), legR=(0, -8)),
    "hug": dict(armL=(-78, -22), armR=(-78, 22), elbL=-55, elbR=-55, lean=6, head=(4, 0, -10)),
    "net": dict(armL=(0, 152), elbL=-8, armR=(-25, -22), elbR=-35, lean=6, twist=10, head=(-6, 0, 8),
                legL=(26, 6), kneeL=18, legR=(-32, -6), kneeR=40),
    "point": dict(armR=(-20, -100), elbR=-4, armL=(0, 38), elbL=-100, lean=-3, head=(-2, 0, 14), legL=(0, 6), legR=(0, -6)),
    "run": dict(armL=(50, 12), elbL=-70, armR=(-60, -12), elbR=-70, lean=12, legL=(-50, 0), kneeL=50, legR=(40, 0), kneeR=70,
                head=(-8, 0, 0)),
    "hold": dict(armL=(-40, 0, 12), armR=(-40, 0, -12), elbL=-20, elbR=-20, lean=-4, head=(-4, 0, 6)),
    "carry": dict(armL=(float(os.environ.get("C_SH", "-30")), 0, 6), armR=(float(os.environ.get("C_SH", "-30")), 0, -6), elbL=(float(os.environ.get("C_EL", "-75")), float(os.environ.get("C_YAW", "45"))), elbR=(float(os.environ.get("C_EL", "-75")), -float(os.environ.get("C_YAW", "45"))), head=(6, 0, 5)),
    "bust": dict(armL=(0, 10), armR=(0, -10), head=(-2, 0, -8)),
}
P = POSES[POSE]
g = lambda k, d: P.get(k, d)
# poses are written for a figure facing -Y with L the picture's left; this one faces +Y, so mirror the swing signs
E = lambda rx, ry=0, rz=0: Euler((R(-rx), R(-ry), R(rz)), "XYZ")

root = empty("root", None, (0, 0, 2.0)); root.rotation_euler = E(g("lean", 0), 0, g("twist", 0))
box(root, (0, 0, 1.0), (2, 1, 2), M_TORSO, TORSO, bevel=0.1)
neck = empty("neck", root, (0, 0, 2.0)); neck.rotation_euler = E(*g("head", (0, 0, 0))); neck.scale = (HEAD_K,) * 3
hr = 0.625
bpy.ops.mesh.primitive_cylinder_add(radius=hr, depth=1.2, location=(0, 0, 0.6), vertices=64)
head = bpy.context.object; head.parent = neck
b = head.modifiers.new("b", "BEVEL"); b.width = 0.2; b.segments = 8; b.limit_method = "ANGLE"
for p in head.data.polygons:
    p.use_smooth = True
head.data.materials.append(M_SKIN)
for sx in (-1, 1):                                                        # the default face, drawn big enough to read
    x = sx * 0.19
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(x, math.sqrt(hr * hr - x * x) - 0.012, 0.68), segments=32, ring_count=16)
    e = bpy.context.object; e.parent = neck; e.scale = (0.6, 0.3, 1.2); e.data.materials.append(M_INK)
    for p in e.data.polygons:
        p.use_smooth = True
cu = bpy.data.curves.new("smile", "CURVE"); cu.dimensions = "3D"; cu.bevel_depth = 0.026; cu.bevel_resolution = 4; cu.use_fill_caps = True
sp = cu.splines.new("NURBS"); sp.points.add(8)
for i, p in enumerate(sp.points):
    a = -1 + 2 * i / 8; x = a * 0.25
    p.co = (x, math.sqrt(hr * hr - x * x) + 0.004, 0.42 - 0.1 * (1 - a * a), 1)
sp.use_endpoint_u = True
sm = bpy.data.objects.new("smile", cu); sc.collection.objects.link(sm); sm.parent = neck; cu.materials.append(M_INK)
# the real Pal Hair: Roblox Y up, front -Z, torso top at y = 1
bpy.ops.wm.obj_import(filepath=os.path.join(SRC, "bacon-hair.obj"))
hair = bpy.context.selected_objects[0]
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
for l in hair.data.uv_layers[0].data:
    l.uv.y = 1 - l.uv.y
hair.data.materials.clear(); hair.data.materials.append(M_HAIR)
for p in hair.data.polygons:
    p.use_smooth = True
hair.parent = neck; hair.location = (0, 0, -1.0)

ARMS = []
for pk, sx in (("L", 1), ("R", -1)):                                     # L is the picture's left = the figure's right (+x)
    rects = LIMB_R if sx > 0 else LIMB_L
    av = tuple(g("arm" + pk, (0, 0))) + (0,)
    sh = empty("sh" + pk, root, (sx * 1.5, 0, 1.75)); sh.rotation_euler = Euler((R(-av[0]), R(-av[1]), R(av[2])), "ZYX")
    ARMS.append(box(sh, (0, 0, -0.25), (1, 1, 1), M_ARM, rects, 0.0, 0.5, 0.09))
    ev = g("elb" + pk, 0); ev = ev if isinstance(ev, tuple) else (ev, 0)
    el = empty("el" + pk, sh, (0, 0, -0.75)); el.rotation_euler = Euler((R(-ev[0]), 0, R(ev[1])), os.environ.get("BACON_EORD", "XYZ"))
    ARMS.append(box(el, (0, 0, -0.5), (0.98, 0.98, 1), M_ARM, rects, 0.5, 1.0, 0.09))
    if POSE == "net" and pk == "L":                                      # the catching net, held up
        bpy.ops.mesh.primitive_cylinder_add(radius=0.09, depth=2.6, location=(0, 0, -2.2), vertices=24)
        o = bpy.context.object; o.parent = el; o.data.materials.append(mat("wood", rgb=(0.55, 0.33, 0.16)))
        bpy.ops.mesh.primitive_torus_add(major_radius=0.95, minor_radius=0.09, location=(0, 0, -4.4), rotation=(R(90), 0, 0))
        o = bpy.context.object; o.parent = el; o.data.materials.append(mat("hoop", rgb=(0.98, 0.78, 0.2)))
    lx, ly = g("leg" + pk, (0, 0))
    hip = empty("hip" + pk, root, (sx * 0.5, 0, 0.0)); hip.rotation_euler = E(lx, ly)
    box(hip, (0, 0, -0.5), (1, 1, 1), M_LEG, rects, 0.0, 0.5, 0.08)
    kn = empty("kn" + pk, hip, (0, 0, -1.0)); kn.rotation_euler = E(g("knee" + pk, 0))
    box(kn, (0, 0, -0.5), (0.98, 0.98, 1), M_LEG, rects, 0.5, 1.0, 0.08)

CAT = os.environ.get("BACON_CAT")
if CAT:                                                                   # a real cat model held against the chest
    sys.path.insert(0, "/home/claude/Cat-Cafe/assets/cat-cafe/blender")
    import rbx_preview
    from mathutils import Matrix
    got = rbx_preview.build("/home/claude/Cat-Cafe/assets/cat-cafe/rbx/%s.model.json" % CAT, "cat")
    pts = [ob.matrix_world @ Vector(c) for ob in got for c in ob.bound_box]
    clo = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    chi = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    k = float(os.environ.get("BACON_CAT_W", "1.25")) / (chi.x - clo.x)
    cz, cy = float(os.environ.get("BACON_CAT_Z", "2.2")), float(os.environ.get("BACON_CAT_Y", "0.55"))
    mid = (clo + chi) / 2
    # the cat's front is Blender -Y; turn it to face +Y, its back against the chest, base at cz
    M = (Matrix.Translation(Vector((0, cy + (chi.y - clo.y) * k / 2, cz))) @ Matrix.Rotation(math.pi, 4, "Z") @ Matrix.Scale(k, 4)
         @ Matrix.Translation(Vector((-mid.x, -mid.y, -clo.z))))
    for ob in got:
        ob.matrix_world = M @ ob.matrix_world
        for m in ob.data.materials:
            bs = m.node_tree.nodes.get("Principled BSDF") if m and m.use_nodes else None
            if bs:
                bs.inputs["Roughness"].default_value = min(bs.inputs["Roughness"].default_value, 0.3)
                for nm in ("Coat Weight", "Clearcoat"):
                    if nm in bs.inputs:
                        bs.inputs[nm].default_value = 0.5
    print("cat size", [(round(a, 2), round(b, 2)) for a, b in zip(clo, chi)], "k", round(k, 3))
bpy.context.view_layer.update()
lo = Vector((1e9,) * 3); hi = -lo
for ob in sc.objects:
    if ob.type in ("MESH", "CURVE"):
        for c in ob.bound_box:
            w = ob.matrix_world @ Vector(c)
            lo = Vector(map(min, lo, w)); hi = Vector(map(max, hi, w))
if POSE in ("bust", "hold"):
    lo.z = 2.4
if POSE == "carry":
    lo.z = 1.9
c = (lo + hi) / 2; r = (hi - lo).length / 2
az, el_ = R(AZ), R(EL)
d = Vector((-math.sin(az) * math.cos(el_), math.cos(az) * math.cos(el_), math.sin(el_)))
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
if os.environ.get("BACON_ONLY") == "arms":
    for ob in sc.objects:
        if ob.type in ("MESH", "CURVE") and ob not in ARMS:
            ob.hide_render = True
bpy.ops.render.render(write_still=True)
print("wrote", OUT)
