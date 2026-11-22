"""Join the parts of several model files (same pivot) into clusters that touch (gap < TOUCH) and list every cluster
apart from the biggest, with its gap to the rest. Usage: cross_float.py a.model.json b.model.json ..."""
import json, sys
import numpy as np
TOUCH = 0.02
def load(path):
    t = json.load(open(path)); out = []
    def walk(n, model):
        for c in n.get("children", []):
            p = c.get("properties", {})
            if c.get("className") == "Model":
                walk(c, c["name"]); continue
            if "Size" in p:
                cf = p["CFrame"]["CFrame"]; R = np.array(cf["orientation"]); s = np.array(p["Size"]) / 2
                ext = np.abs(R) @ s; c0 = np.array(cf["position"])
                out.append((model, c.get("name"), c0 - ext, c0 + ext))
            walk(c, model)
    walk(t, t.get("name"))
    return out
parts = [p for f in sys.argv[1:] for p in load(f)]
# the plot floor the cafe stands on: a slab under y=0 across the plot
parts.append(("floor", "floor", np.array([-40.0, -1.0, -40.0]), np.array([40.0, 0.0, 40.0])))
n = len(parts); par = list(range(n))
def f(i):
    while par[i] != i:
        par[i] = par[par[i]]; i = par[i]
    return i
lo = np.array([p[2] for p in parts]); hi = np.array([p[3] for p in parts])
for i in range(n):
    d = np.maximum(0, np.maximum(lo[i] - hi, lo - hi[i]))
    for j in np.where(np.linalg.norm(d, axis=1) < TOUCH)[0]:
        par[f(i)] = f(j)
groups = {}
for i in range(n): groups.setdefault(f(i), []).append(i)
big = max(groups.values(), key=len)
rest = np.array(big)
for g in sorted(groups.values(), key=len):
    if g is big: continue
    glo, ghi = lo[g].min(0), hi[g].max(0)
    d = np.maximum(0, np.maximum(glo - hi[rest], lo[rest] - ghi)); gap = float(np.linalg.norm(d, axis=1).min())
    models = sorted({str(parts[i][0]) for i in g})
    print(f"{gap:.2f}", len(g), models, np.round((glo + ghi) / 2, 2).tolist(), np.round(ghi - glo, 2).tolist())
print(len(groups) - 1, "loose clusters")
