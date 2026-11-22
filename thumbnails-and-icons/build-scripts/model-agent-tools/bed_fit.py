"""Fit check for the F79 cat beds (run from assets/cat-cafe): python3 bed_fit.py [x,z,rot ...]
Each bed is placed at its spot and every part tested against the shell, interior and tier dressing (SAT depth),
plus stand-in boxes for the nap spot cats and the decor spots."""
import json, math, sys
import numpy as np

def parts_of(name):
    out = []

    def walk(node, model):
        for c in node.get("children", []):
            p = c.get("properties", {})
            m = c["name"] if c.get("className") == "Model" else model
            if "CFrame" in p and "Size" in p:
                cf = p["CFrame"]["CFrame"]
                R = np.array(cf["orientation"], float)
                cyl = p.get("Shape") == "Cylinder"
                out.append((m, c["name"] + ("#cyl" if cyl else ""), np.array(cf["position"], float), R,
                            np.array(p["Size"], float) / 2))
            walk(c, m)
    walk(json.load(open(f"rbx/{name}.model.json")), name)
    return out


def depth(a, b):
    """SAT depth; a Cylinder part counts as the octagon its square and the square turned 45 degrees share."""
    if a[1].endswith("#cyl") or b[1].endswith("#cyl"):
        best = 1e9
        for ta in (_twins(a) if a[1].endswith("#cyl") else [a]):
            for tb in (_twins(b) if b[1].endswith("#cyl") else [b]):
                best = min(best, _depth(ta, tb))
        return best
    return _depth(a, b)


def _twins(p):
    c45 = math.cos(math.pi / 4)
    Rx = np.array([[1, 0, 0], [0, c45, -c45], [0, c45, c45]])
    return [(p[0], p[1][:-4], p[2], p[3], p[4]), (p[0], p[1][:-4], p[2], p[3] @ Rx, p[4])]


def _depth(a, b):
    (_, _, ca, Ra, ha), (_, _, cb, Rb, hb) = a, b
    axes = [Ra[:, i] for i in range(3)] + [Rb[:, i] for i in range(3)]
    for i in range(3):
        for j in range(3):
            v = np.cross(Ra[:, i], Rb[:, j])
            if np.linalg.norm(v) > 1e-6:
                axes.append(v / np.linalg.norm(v))
    d = cb - ca
    best = 1e9
    for ax in axes:
        ra = np.sum(np.abs(Ra.T @ ax) * ha)
        rb = np.sum(np.abs(Rb.T @ ax) * hb)
        o = ra + rb - abs(d @ ax)
        if o <= 0:
            return 0.0
        best = min(best, o)
    return best



def ry(deg):
    a = math.radians(deg)
    return np.array([[math.cos(a), 0, math.sin(a)], [0, 1, 0], [-math.sin(a), 0, math.cos(a)]])

def box(name, x, y, z, rot, size):
    return ("standin", name, np.array([x, y, z], float), ry(rot), np.array(size, float) / 2)

SPOTS = {"bed_1": (-16.3, -12.5, -135), "bed_2": (16.3, -12.5, 135), "bed_3": (-13.6, -12.6, 180),
         "bed_4": (13.6, -12.6, 180), "bed_5": (-16.4, 8.5, -90), "bed_6": (16.4, 8.5, 90)}
for a in [t for t in sys.argv[1:] if "=" in t]:
    k, v = a.split("=")
    SPOTS[k] = tuple(float(t) for t in v.split(","))
others = []
for m in ("CatCafe_Plot_Cafe_Blush", "CatCafe_Plot_Interior", "CatCafe_Plot_Tier1", "CatCafe_Plot_Tier2",
          "CatCafe_Plot_Tier3", "CatCafe_Plot_Tier4", "CatCafe_Plot_Tier5", "CatCafe_Plot_BackDoor"):
    others += [(m,) + p[1:] for p in parts_of(m)]
naps = [(-15.5, -10, 45), (15.5, -10, -45), (15.5, 3.5, -90), (11, 11, 180)]
for i, (x, z, r) in enumerate(naps):
    others.append(box(f"nap_{i + 1}", x, 0.95, z, r, (1.1, 1.9, 2.1)))
decor = [(-9.5, -12.6, 180), (9.5, -12.6, 180), (16.6, -6.5, 90), (-16.6, -7.5, -90), (8, 12.6, 0), (-12.6, 12.6, 0),
         (-16.6, 4, -90), (11.5, 12.6, 0)]
for i, (x, z, r) in enumerate(decor):
    others.append(box(f"decor_{i + 1}", x, 1.5, z, r, (2.6, 3.0, 2.2)))
trees = [(-14, 8), (14, 8)]
for i, (x, z) in enumerate(trees):
    others += [("CatTree", n, np.array([x, 0, z]) + c, R, h) for (_, n, c, R, h) in parts_of("CatCafe_Furniture_CatTree")]
bed = parts_of("CatCafe_Furniture_CatBed")
for spot, (x, z, rot) in SPOTS.items():
    R = ry(rot)
    placed = [(m, n, np.array([x, 0, z]) + R @ c, R @ Rp, h) for (m, n, c, Rp, h) in bed]
    lo = np.array([x - 3, -1, z - 3]); hi = np.array([x + 3, 4, z + 3])
    near = [o for o in others if np.all(o[2] + 4 > lo) and np.all(o[2] - 4 < hi)]
    hits = {}
    for a in placed:
        for o in near:
            d = depth(a, o)
            if d > 0.01:
                key = (o[0], o[1], tuple(o[2].round(2)))
                hits[key] = max(hits.get(key, 0), d)
    print(f"{spot} at ({x}, {z}) turn {rot}: {len(hits)} clashes")
    for (m, n, c), d in sorted(hits.items(), key=lambda kv: -kv[1])[:8]:
        print(f"   {d:.2f} {m}/{n} at {c}")


def clashes(x, z, rot):
    R = ry(rot)
    placed = [(m, n, np.array([x, 0, z]) + R @ c, R @ Rp, h) for (m, n, c, Rp, h) in bed]
    lo = np.array([x - 3, -1, z - 3]); hi = np.array([x + 3, 4, z + 3])
    near = [o for o in others if np.all(o[2] + 4 > lo) and np.all(o[2] - 4 < hi)]
    # a quick bound: bed parts reach 1.5 from the centre in plan
    for a in placed:
        for o in near:
            if depth(a, o) > 0.01:
                return True
    return False


if "--search" in sys.argv[0:] or True:
    print("nudges (smallest move with no clash, up to 2 studs):")
    for spot, (x, z, rot) in SPOTS.items():
        cands = sorted(((dx / 10, dz / 10) for dx in range(-20, 21) for dz in range(-20, 21)
                        if dx * dx + dz * dz <= 400), key=lambda d: (d[0] ** 2 + d[1] ** 2, d))
        for dx, dz in cands:
            if not clashes(x + dx, z + dz, rot):
                print(f"   {spot}: ({x + dx:.1f}, {z + dz:.1f}) turn {rot}, moved {math.hypot(dx, dz):.2f}")
                break
        else:
            print(f"   {spot}: nothing clear within 2")
