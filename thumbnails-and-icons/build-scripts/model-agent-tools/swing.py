"""Write a posed copy of the back door's model.json: python3 swing.py in.json out.json leaf_deg flap_deg sign(0/1)"""
import json, math, sys
import numpy as np
src, dst, leaf, flap, sign = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5] == "1"
t = json.load(open(src))
def ry(a):
    a = math.radians(a); return np.array([[math.cos(a), 0, math.sin(a)], [0, 1, 0], [-math.sin(a), 0, math.cos(a)]])
def rx(a):
    a = math.radians(a); return np.array([[1, 0, 0], [0, math.cos(a), -math.sin(a)], [0, math.sin(a), math.cos(a)]])
def piv(m):
    return np.array(m["properties"]["WorldPivotData"]["OptionalCFrame"]["position"], float)
def apply(n, R, c):
    for ch in n.get("children", []):
        p = ch.get("properties", {})
        if "CFrame" in p:
            cf = p["CFrame"]["CFrame"]
            cf["position"] = (c + R @ (np.array(cf["position"]) - c)).tolist()
            cf["orientation"] = (R @ np.array(cf["orientation"])).tolist()
        apply(ch, R, c)
def find(n, suffix):
    for ch in n.get("children", []):
        if ch.get("className") == "Model" and ch["name"].endswith(suffix):
            return ch
        r = find(ch, suffix)
        if r: return r
leafm = find(t, "_Leaf")
if not sign:
    leafm["children"] = [c for c in leafm["children"] if "_Sign" not in c["name"]]
fl = find(t, "_Flap")
apply(fl, rx(flap), piv(fl))            # flap first, in the shut leaf's frame
apply(leafm, ry(leaf), piv(leafm))
json.dump(t, open(dst, "w"))
