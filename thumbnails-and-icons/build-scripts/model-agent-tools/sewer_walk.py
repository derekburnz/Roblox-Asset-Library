import json, math, sys
import bpy  # noqa: F401  (bmesh needs it first)
sys.path.insert(0, ".")
import sewerset as ss
dist, cell = ss.walk_grid()
man = json.load(open("../exports/manifest.json"))
def find(o):
    if isinstance(o, dict):
        if o.get("name") == ss.SET: return o
        for v in o.values():
            r = find(v)
            if r: return r
    if isinstance(o, list):
        for v in o:
            r = find(v)
            if r: return r
pts = find(man)["points_roblox"]
far = max(dist.values())
print("reachable cells", len(dist), "max walk", round(far, 1))
rows = []
for label, lst in pts.items():
    for p in lst:
        d = dist.get(cell(p[0], p[2]))
        if d is None:
            best = None
            for dx in range(-4, 5):
                for dz in range(-4, 5):
                    dd = dist.get(cell(p[0] + dx, p[2] + dz))
                    if dd is not None and (best is None or dd < best): best = dd
            d = best
        rows.append((label, p[0], p[2], p[3], d))
near = [r for r in rows if r[3] == "near"]; deep = [r for r in rows if r[3] == "deep"]
print("near", len(near), "deep", len(deep), "total", len(rows))
print("near max", max(r[4] or 0 for r in near), "deep min", min(r[4] if r[4] is not None else 1e9 for r in deep))
for r in sorted(rows, key=lambda r: (r[4] if r[4] is not None else -1)):
    print(f"{r[0]:16s} {r[1]:7.1f} {r[2]:7.1f} {r[3]:5s} {r[4] if r[4] is None else round(r[4],1)}")
