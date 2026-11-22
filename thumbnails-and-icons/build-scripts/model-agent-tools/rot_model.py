"""Rotate an rbx model.json about its origin: python3 rot_model.py <in> <out> <rx deg> [ry deg] [rz deg] (applied X, then Y, then Z)."""
import json, math, sys
import numpy as np
src, dst = sys.argv[1], sys.argv[2]
rx, ry, rz = (math.radians(float(v)) for v in (sys.argv[3:6] + ["0", "0"])[:3])
def X(a): return np.array([[1, 0, 0], [0, math.cos(a), -math.sin(a)], [0, math.sin(a), math.cos(a)]])
def Y(a): return np.array([[math.cos(a), 0, math.sin(a)], [0, 1, 0], [-math.sin(a), 0, math.cos(a)]])
def Z(a): return np.array([[math.cos(a), -math.sin(a), 0], [math.sin(a), math.cos(a), 0], [0, 0, 1]])
R = Z(rz) @ Y(ry) @ X(rx)
t = json.load(open(src))
def walk(n):
    for c in n.get("children", []):
        p = c.get("properties", {})
        if "CFrame" in p and c.get("className") != "Attachment":
            cf = p["CFrame"]["CFrame"]
            cf["position"] = list(R @ np.array(cf["position"], float))
            cf["orientation"] = (R @ np.array(cf["orientation"], float)).tolist()
        walk(c)
walk(t)
json.dump(t, open(dst, "w"))
