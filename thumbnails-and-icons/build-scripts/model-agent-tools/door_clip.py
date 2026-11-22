"""Clip check of the back door against a cafe shell, shut and with the leaf swung (run from assets/cat-cafe):
    python3 door_clip.py CatCafe_Plot_Cafe_Blush [angles...]
Every part of the door (all of them, colliding or not) against every part of the shell, SAT depth > 0.005."""
import json
import math
import sys

import numpy as np

shell = sys.argv[1]
angles = [float(a) for a in sys.argv[2:]] or [0.0, -45.0, -90.0]


def parts_of(name):
    out = []

    def walk(node, model):
        for c in node.get("children", []):
            p = c.get("properties", {})
            m = c["name"] if c.get("className") == "Model" else model
            if "CFrame" in p and "Size" in p:
                cf = p["CFrame"]["CFrame"]
                out.append((m, c["name"], np.array(cf["position"], float), np.array(cf["orientation"], float),
                            np.array(p["Size"], float) / 2))
            walk(c, m)
    walk(json.load(open(f"rbx/{name}.model.json")), name)
    return out


def depth(a, b):
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


door = parts_of("CatCafe_Plot_BackDoor")
sh = [p for p in parts_of(shell)]
hinge = None
t = json.load(open("rbx/CatCafe_Plot_BackDoor.model.json"))
for c in t["children"]:
    if c["name"].endswith("_Leaf"):
        hinge = np.array(c["properties"]["WorldPivotData"]["OptionalCFrame"]["position"], float)
for ang in angles:
    a = math.radians(ang)
    Ry = np.array([[math.cos(a), 0, math.sin(a)], [0, 1, 0], [-math.sin(a), 0, math.cos(a)]])
    moved = []
    for (m, n, c, R, h) in door:
        if "_Leaf" in m or "_Flap" in m or "_Sign" in m:
            c, R = hinge + Ry @ (c - hinge), Ry @ R
        moved.append((m, n, c, R, h))
    lo = np.array([-12.5, -0.5, 13.0]); hi = np.array([-3.5, 9.0, 22.0])
    near = [p for p in sh if np.all(p[2] + 3 > lo) and np.all(p[2] - 3 < hi)]
    hits = []
    for a_ in moved:
        for b_ in near:
            d = depth(a_, b_)
            if d > 0.005:
                hits.append((d, a_[0].replace("CatCafe_Plot_BackDoor", "Door"), a_[1], b_[1], b_[2].round(2), b_[4] * 2))
    hits.sort(key=lambda r: -r[0])
    print(f"leaf at {ang:+.0f}: {len(hits)} overlaps")
    for r in hits[:12]:
        print(f"   {r[0]:.3f} {r[1]}/{r[2]} vs {r[3]} at {r[4]} size {r[5].round(2)}")
