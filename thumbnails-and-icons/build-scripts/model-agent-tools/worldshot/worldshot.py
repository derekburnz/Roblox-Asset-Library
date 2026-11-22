"""Render a region of the built world from worldscan's world-parts.tsv (with the extra colour column).
usage: python worldshot.py -- parts.tsv OUTDIR "x0,x1,z0,z1" cams.json
cams.json: [{"name":..,"eye":[x,y,z],"look":[x,y,z],"lens":35,"res":[1280,800]}] in Roblox world studs."""
import sys, json, math, os
import bpy, bmesh
from mathutils import Matrix, Vector
argv = sys.argv[sys.argv.index("--") + 1:]
tsv, out, region, cams = argv[0], argv[1], [float(v) for v in argv[2].split(",")], json.load(open(argv[3]))
x0, x1, z0, z1 = region
bpy.ops.wm.read_factory_settings(use_empty=True)
C = Matrix(((-1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)))
groups = {}
def bm_for(key):
    if key not in groups:
        groups[key] = bmesh.new()
    return groups[key]
n = 0
for line in open(tsv):
    f = line.rstrip("\n").split("\t")
    try:
        m = [float(v) for v in f[3:15]]; size = [float(v) for v in f[15:18]]; tr = float(f[18])
    except (ValueError, IndexError):
        continue
    if tr >= 0.95 or not (x0 <= m[0] <= x1 and z0 <= m[2] <= z1):
        continue
    if max(size) > 400:
        continue
    col = (0.7, 0.7, 0.7)
    if len(f) > 24 and f[24]:
        col = tuple(float(v) for v in f[24].split(","))
    mat = f[22]
    key = (col, mat == "Neon", tr > 0.2)
    bm = bm_for(key)
    R = Matrix(((m[3], m[4], m[5], 0), (m[6], m[7], m[8], 0), (m[9], m[10], m[11], 0), (0, 0, 0, 1)))
    M = C @ Matrix.Translation(m[0:3]) @ R
    cls, shape = f[1], f[2]
    ms = f[20]
    if cls == "WedgePart":
        sx, sy, sz = size
        vs = [(-.5*sx,-.5*sy,-.5*sz),(.5*sx,-.5*sy,-.5*sz),(.5*sx,-.5*sy,.5*sz),(-.5*sx,-.5*sy,.5*sz),(-.5*sx,.5*sy,.5*sz),(.5*sx,.5*sy,.5*sz)]
        bv = [bm.verts.new(M @ Vector(v)) for v in vs]
        for idx in ((0,1,2,3),(3,2,5,4),(0,4,5,1),(0,3,4),(1,5,2)):
            try: bm.faces.new([bv[i] for i in idx])
            except ValueError: pass
    elif shape == "Cylinder":
        d = min(size[1], size[2])
        bmesh.ops.create_cone(bm, cap_ends=True, segments=14, radius1=d/2, radius2=d/2, depth=size[0],
                              matrix=M @ Matrix.Rotation(math.radians(90), 4, "Y"))
    elif shape == "Ball" or (ms and cls == "Part" and "Sphere" in ms):
        if shape == "Ball":
            d = min(size); sc = (d, d, d)
        else:
            sc = size
        bmesh.ops.create_icosphere(bm, subdivisions=2, radius=0.5, matrix=M @ Matrix.Diagonal((*sc, 1)))
    else:
        bmesh.ops.create_cube(bm, size=1.0, matrix=M @ Matrix.Diagonal((*size, 1)))
    n += 1
print("parts", n, "groups", len(groups))
sc = bpy.context.scene
for i, (key, bm) in enumerate(groups.items()):
    col, neon, glass = key
    me = bpy.data.meshes.new(f"g{i}"); bm.normal_update(); bm.to_mesh(me); bm.free()
    ob = bpy.data.objects.new(f"g{i}", me); sc.collection.objects.link(ob)
    mt = bpy.data.materials.new(f"m{i}"); mt.use_nodes = True
    bsdf = mt.node_tree.nodes["Principled BSDF"]
    lin = tuple(c ** 2.2 for c in col)
    bsdf.inputs["Base Color"].default_value = (*lin, 1); bsdf.inputs["Roughness"].default_value = 0.8
    if neon:
        bsdf.inputs["Emission Color"].default_value = (*lin, 1); bsdf.inputs["Emission Strength"].default_value = 1.5
    if glass:
        bsdf.inputs["Alpha"].default_value = 0.5
    me.materials.append(mt)
# ground
gm = bpy.data.meshes.new("ground"); gb = bmesh.new()
bmesh.ops.create_grid(gb, x_segments=1, y_segments=1, size=1500); gb.to_mesh(gm)
go = bpy.data.objects.new("ground", gm); sc.collection.objects.link(go); go.location = (-(x0 + x1) / 2, (z0 + z1) / 2, -0.02)
gmt = bpy.data.materials.new("gm"); gmt.use_nodes = True
gmt.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.35, 0.33, 0.3, 1); gm.materials.append(gmt)
sun = bpy.data.lights.new("sun", "SUN"); sun.energy = 3.0; so = bpy.data.objects.new("sun", sun); sc.collection.objects.link(so)
so.rotation_euler = (math.radians(float(os.environ.get("WS_SUN", 50))), 0, math.radians(30)); sun.angle = math.radians(8)
w = bpy.data.worlds.new("W"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (0.55, 0.7, 0.9, 1); w.node_tree.nodes["Background"].inputs[1].default_value = 1.0
sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"; sc.cycles.samples = int(os.environ.get("WS_SAMPLES", 12)); sc.cycles.use_denoising = True
sc.view_settings.view_transform = "Standard"; sc.render.image_settings.file_format = "PNG"
cd = bpy.data.cameras.new("cam"); cam = bpy.data.objects.new("cam", cd); sc.collection.objects.link(cam); sc.camera = cam
cd.clip_start = 0.3; cd.clip_end = 3000
os.makedirs(out, exist_ok=True)
for c in cams:
    eye = (C @ Vector((*c["eye"], 1))).to_3d(); look = (C @ Vector((*c["look"], 1))).to_3d()
    cam.location = eye
    cam.rotation_euler = (look - eye).to_track_quat("-Z", "Y").to_euler()
    cd.lens = c.get("lens", 35)
    if c.get("ortho"):
        cd.type = "ORTHO"; cd.ortho_scale = c["ortho"]
    else:
        cd.type = "PERSP"
    sc.render.resolution_x, sc.render.resolution_y = c.get("res", [1280, 800])
    sc.render.filepath = os.path.join(out, c["name"] + ".png")
    bpy.ops.render.render(write_still=True)
    print("saved", sc.render.filepath)
