"""Clip check for an area set's Roblox model (run from assets/cat-cafe):
    python3 set_clip.py CatCafe_Park_Set [points]
1. pairs of colliding parts from different pieces that sink into each other deeper than 0.15 (SAT depth),
2. with `points`: spots from the manifest whose cat box (2 x 2.5 x 2 standing on the spot) meets a colliding part;
   a trap spot with a turn (5th element) also needs a 3.4 x 3.4 footprint clear for its world-placed prop.
"""
import json
import sys
from collections import defaultdict

import numpy as np

name = sys.argv[1]
want_points = "points" in sys.argv[2:]
tree = json.load(open(f"rbx/{name}.model.json"))
parts = []


def walk(node):
    for c in node.get("children", []):
        p = c.get("properties", {})
        if "CFrame" in p and p.get("CanCollide"):
            cf = p["CFrame"]["CFrame"]
            R = np.array(cf["orientation"], float)          # rows; columns are the part's local axes in world
            parts.append((c["name"], np.array(cf["position"], float), R, np.array(p["Size"], float) / 2))
        walk(c)


walk(tree)
total = 0


def count(node):
    global total
    for c in node.get("children", []):
        if c.get("className") in ("Part", "WedgePart", "TrussPart", "CornerWedgePart"):
            total += 1
        count(c)


count(tree)


def axes(R):
    return [R[:, i] for i in range(3)]


def depth(a, b):
    """SAT penetration depth of two oriented boxes (0 when apart)."""
    (_, ca, Ra, ha), (_, cb, Rb, hb) = a, b
    A, Bx = axes(Ra), axes(Rb)
    d = cb - ca
    best = 1e9
    cand = A + Bx + [np.cross(u, v) for u in A for v in Bx]
    for ax in cand:
        n = np.linalg.norm(ax)
        if n < 1e-6:
            continue
        ax = ax / n
        ra = sum(ha[i] * abs(A[i] @ ax) for i in range(3))
        rb = sum(hb[i] * abs(Bx[i] @ ax) for i in range(3))
        ov = ra + rb - abs(d @ ax)
        if ov <= 0:
            return 0.0
        best = min(best, ov)
    return best


def aabb(p):
    _, c, R, h = p
    e = np.abs(R) @ h
    return c - e, c + e


def piece(n):
    rest = n[len(name) + 1:]
    return rest.split("_", 1)[0] if rest[:3].isdigit() else "ground"


boxes = [aabb(p) for p in parts]
lo = np.array([b[0] for b in boxes])
hi = np.array([b[1] for b in boxes])
pieces = [piece(p[0]) for p in parts]
names = {}
for p, pc in zip(parts, pieces):
    names.setdefault(pc, p[0][len(name) + 1:])
worst = defaultdict(float)
where = {}
for i in range(len(parts)):
    m = np.all((lo[i + 1:] < hi[i]) & (hi[i + 1:] > lo[i]), axis=1)
    for j in np.nonzero(m)[0] + i + 1:
        if pieces[i] == pieces[j] or "ground" in (pieces[i], pieces[j]) or                 parts[i][0].endswith("_Barrier") or parts[j][0].endswith("_Barrier"):   # invisible walls overlap
            continue
        dd = depth(parts[i], parts[j])
        if dd > 0.15:
            k = tuple(sorted((pieces[i], pieces[j])))
            if dd > worst[k]:
                worst[k] = dd
                where[k] = (i, j)
print(f"{total} parts; {len(worst)} piece pairs overlap more than 0.15:")
for (a, b), dd in sorted(worst.items(), key=lambda kv: -kv[1]):
    print(f"   {dd:.2f}  {names[a]}  x  {names[b]}")
    if "-v" in sys.argv:
        for q in where[(a, b)]:
            print("        ", parts[q][0][len(name) + 1:], np.round(parts[q][1], 2), np.round(parts[q][3] * 2, 2))

if want_points:
    man = json.load(open("exports/manifest.json"))

    def find(o):
        if isinstance(o, dict):
            if name in o and isinstance(o[name], dict):
                return o[name]
            for v in o.values():
                r = find(v)
                if r:
                    return r
        if isinstance(o, list):
            for v in o:
                if isinstance(v, dict) and v.get("name") == name:
                    return v
                r = find(v)
                if r:
                    return r
        return None

    pts = find(man)["points_roblox"]
    print("spots inside a colliding part (a 2 x 2.5 x 2 cat box on the floor):")
    bad = 0
    floor_y = 0.0
    for label, lst in pts.items():
        for pt in lst:
            x, y, z = pt[:3]
            half = np.array([1.0, 1.25, 1.0])
            if label.startswith("trap_") and len(pt) > 4:
                half = np.array([1.7, 1.25, 1.7])
            cat = ("cat", np.array([x, y + 0.05 + 1.25, z]), np.eye(3), half)
            clo, chi = aabb(cat)
            m = np.all((lo < chi) & (hi > clo), axis=1)
            hits = [parts[j][0][len(name) + 1:] for j in np.nonzero(m)[0] if depth(cat, parts[j]) > 0.02]
            if hits:
                bad += 1
                print(f"   {label} {pt}: {', '.join(sorted(set(hits))[:4])}")
    print(f"{bad} spots blocked")
