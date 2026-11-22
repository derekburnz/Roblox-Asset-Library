"""Backdrop parts (not ground or hills) whose footprint crosses the town plate's edge below y 0: python3 seam.py <rbx json> <plate_x> <plate_z>"""
import json, sys, numpy as np
t = json.load(open(sys.argv[1])); PX, PZ = float(sys.argv[2]), float(sys.argv[3])
out = []
def walk(n, model):
    for c in n.get("children", []):
        p = c.get("properties", {})
        m = c["name"] if c["name"].startswith("CatCafe_Town_Backdrop") and c.get("children") is not None and "Size" not in p else model
        if "CFrame" in p and "Size" in p and not any(s in c["name"] for s in ("_Ground", "_Hills")):
            pos = np.array(p["CFrame"]["CFrame"]["position"]); R = np.array(p["CFrame"]["CFrame"]["orientation"])
            e = np.abs(R) @ (np.array(p["Size"]) / 2); lo, hi = pos - e, pos + e
            if lo[1] < -0.01:
                inx, inz = lo[0] < PX and hi[0] > -PX, lo[2] < PZ and hi[2] > -PZ
                crossz = inx and (lo[2] < PZ < hi[2] or lo[2] < -PZ < hi[2])
                crossx = inz and (lo[0] < PX < hi[0] or lo[0] < -PX < hi[0])
                if crossz or crossx:
                    out.append((c["name"], [round(v, 2) for v in pos], [round(v, 2) for v in lo], [round(v, 2) for v in hi]))
        walk(c, m)
walk(t, "")
for o in out: print(o)
print(len(out), "crossing")
