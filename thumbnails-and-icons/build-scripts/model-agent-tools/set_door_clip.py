"""F80 door sets on the cafe (run from assets/cat-cafe): shut and swung, every part of the set (front doors at the
front pivot, back door at the back pivot, a flap riding its leaf) against the shell, interior, Tier 1 to 5 and the
night ClosedSign. SAT depth > MIN.
    python3 set_door_clip.py FireEscape NeonPaw"""
import json
import math
import sys

import numpy as np

MIN = 0.01
door, flap = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else None)


def Ry(deg):
    a = math.radians(deg)
    return np.array([[math.cos(a), 0, math.sin(a)], [0, 1, 0], [-math.sin(a), 0, math.cos(a)]])


def load(path):
    """[(model name, part name, centre, R, half size)] and {model name: pivot} in the file's space."""
    parts, pivots = [], {}

    def walk(node, model):
        for c in node.get("children", []):
            p = c.get("properties", {})
            if c.get("className") == "Model":
                piv = p.get("WorldPivotData", {}).get("OptionalCFrame")
                if piv:
                    pivots[c["name"]] = np.array(piv["position"], float)
                walk(c, c["name"])
                continue
            if "CFrame" in p and "Size" in p:
                cf = p["CFrame"]["CFrame"]
                parts.append((model, c["name"], np.array(cf["position"], float), np.array(cf["orientation"], float),
                              np.array(p["Size"], float) / 2))
            walk(c, model)
    t = json.load(open(path))
    walk(t, t.get("name", path.split("/")[-1].split(".")[0]))
    return parts, pivots


def placed(parts, pos, rot):
    R = Ry(rot)
    return [(m, n, np.array(pos, float) + R @ c, R @ Rp, h) for (m, n, c, Rp, h) in parts]


def swing(parts, model_key, pivot, deg):
    R = Ry(deg)
    return [(m, n, pivot + R @ (c - pivot), R @ Rp, h) if model_key in m else (m, n, c, Rp, h)
            for (m, n, c, Rp, h) in parts]


def depth(a, b):
    (_, _, ca, Ra, ha), (_, _, cb, Rb, hb) = a, b
    if np.linalg.norm(cb - ca) > np.linalg.norm(ha) + np.linalg.norm(hb):
        return 0.0
    axes = [Ra[:, i] for i in range(3)] + [Rb[:, i] for i in range(3)]
    for i in range(3):
        for j in range(3):
            v = np.cross(Ra[:, i], Rb[:, j])
            if np.linalg.norm(v) > 1e-6:
                axes.append(v / np.linalg.norm(v))
    d = cb - ca
    best = 1e9
    for ax in axes:
        o = np.sum(np.abs(Ra.T @ ax) * ha) + np.sum(np.abs(Rb.T @ ax) * hb) - abs(d @ ax)
        if o <= 0:
            return 0.0
        best = min(best, o)
    return best


env = []
for n in ("Cafe_Blush", "Interior", "Tier1", "Tier2", "Tier3", "Tier4", "Tier5", "ClosedSign"):
    env += load(f"rbx/CatCafe_Plot_{n}.model.json")[0]
fp, fpiv = load(f"rbx/CatCafe_Door_{door}_Front.model.json")
bp, bpiv = load(f"rbx/CatCafe_Door_{door}_Back.model.json")
front = placed(fp, (0, 0, -14), 0)
back = placed(bp, (-8, 0, 14.5), 180)
R180 = Ry(180)
fpiv = {k: np.array((0, 0, -14.0)) + v for k, v in fpiv.items()}
bpiv = {k: np.array((-8, 0, 14.5)) + R180 @ v for k, v in bpiv.items()}
if flap:
    back += placed(load(f"rbx/CatCafe_CatFlap_{flap}.model.json")[0], (-8, 0.22, 14.72), 180)
leafL = next(k for k in fpiv if k.endswith("_LeafL"))
leafR = next(k for k in fpiv if k.endswith("_LeafR"))
leafB = next(k for k in bpiv if k.endswith("_Leaf"))


def report(label, mine):
    lo = np.min([c for _, _, c, _, _ in mine], axis=0) - 4
    hi = np.max([c for _, _, c, _, _ in mine], axis=0) + 4
    near = [p for p in env if np.all(p[2] > lo) and np.all(p[2] < hi)]
    hits = []
    for a in mine:
        for b in near:
            d = depth(a, b)
            if d > MIN:
                hits.append((d, a[0].split("_", 3)[-1], a[1].split("_", 3)[-1], b[1], b[2].round(2)))
    hits.sort(key=lambda r: -r[0])
    print(f"{label}: {len(hits)}")
    for r in hits[:8]:
        print(f"   {r[0]:.3f} {r[1]}/{r[2]} vs {r[3]} at {r[4]}")


for deg in (0, 45, 90):
    f = swing(swing(front, leafL, fpiv[leafL], -deg), leafR, fpiv[leafR], deg)
    report(f"front open {deg}", f)
    tag = (leafB, "CatFlap_")
    b = [(m, n, bpiv[leafB] + Ry(-deg) @ (c - bpiv[leafB]), Ry(-deg) @ R, h) if (leafB in m or "_Sign" in m or "CatFlap_" in m)
         else (m, n, c, R, h) for (m, n, c, R, h) in back]
    report(f"back open {deg}", b)
