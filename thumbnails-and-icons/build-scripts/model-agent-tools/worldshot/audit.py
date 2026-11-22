"""World clip audit from world-parts.tsv: pairs of different placed models whose visible parts sink into each other.
usage: python audit.py parts.tsv [min_depth=0.3] > report"""
import sys, collections, math
import numpy as np
tsv = sys.argv[1]; MIN = float(sys.argv[2]) if len(sys.argv) > 2 else 0.3
P = []
for l in open(tsv):
    f = l.rstrip("\n").split("\t")
    try:
        c = np.array(list(map(float, f[3:6]))); R = np.array(list(map(float, f[6:15]))).reshape(3, 3)
        s = np.array(list(map(float, f[15:18]))); tr = float(f[18])
    except Exception:
        continue
    if tr >= 0.5 or s.max() > 60:          # invisible, glass, and big slabs, walls and floors
        continue
    owner = f[21] or f[0].rsplit(".", 1)[0]
    if any(k in owner for k in ("Zones", "WalkUp", "Backdrop", "Sky", "Clouds")) or ".Plots." in owner or "Plot" in owner.split(".")[2:3]:
        continue
    h = s / 2
    ext = np.abs(R) @ h
    P.append((owner, c, R, h, c - ext, c + ext, f[0].rsplit(".", 1)[-1], f[2]))
print("parts", len(P), file=sys.stderr)
CELL = 6.0
grid = collections.defaultdict(list)
for i, p in enumerate(P):
    lo, hi = p[4], p[5]
    for gx in range(int(lo[0] // CELL), int(hi[0] // CELL) + 1):
        for gz in range(int(lo[2] // CELL), int(hi[2] // CELL) + 1):
            grid[(gx, gz)].append(i)
def depth(a, b):
    A = [a[2][:, i] for i in range(3)]; B = [b[2][:, i] for i in range(3)]
    t = b[1] - a[1]; best = 1e9
    for ax in A + B + [np.cross(x, y) for x in A for y in B]:
        n = np.linalg.norm(ax)
        if n < 1e-6: continue
        ax = ax / n
        ra = sum(a[3][i] * abs(A[i] @ ax) for i in range(3)); rb = sum(b[3][i] * abs(B[i] @ ax) for i in range(3))
        d = ra + rb - abs(t @ ax)
        if d <= 0: return 0.0
        best = min(best, d)
    return best
seen = set(); pairs = collections.defaultdict(list)
for cell, idx in grid.items():
    for ii in range(len(idx)):
        a = P[idx[ii]]
        for jj in range(ii + 1, len(idx)):
            b = P[idx[jj]]
            if a[0] == b[0]: continue
            # owners nested in each other (a set and its own sub-model) are one placed thing
            if a[0].startswith(b[0] + ".") or b[0].startswith(a[0] + "."): continue
            key = (idx[ii], idx[jj])
            if key in seen: continue
            if (a[4] > b[5] - 0.08).any() or (b[4] > a[5] - 0.08).any(): continue
            seen.add(key)
            d = depth(a, b)
            thin = min(2 * a[3].min(), 2 * b[3].min())
            through = d >= 0.08 and thin >= 0.1 and d >= 0.85 * thin
            if d >= MIN or through:
                # a ball or cylinder drawn as a box overstates the depth a little
                round_ = a[7] in ("Ball", "Cylinder") or b[7] in ("Ball", "Cylinder")
                k = tuple(sorted((a[0], b[0])))
                pairs[k].append((d, a[1], a[6], b[6], round_, through))
rows = []
for k, v in pairs.items():
    v.sort(key=lambda r: -r[0])
    d, at, na, nb, rnd, _ = v[0]
    rows.append((d, len(v), k, at, na, nb, rnd, sum(1 for r in v if r[5])))
rows.sort(key=lambda r: -r[0])
print("| depth | parts | thin parts right through | model A | model B | at (x, y, z) |"); print("|---|---|---|---|---|---|")
for d, n, k, at, na, nb, rnd, th in rows:
    a, b = (s.replace("Workspace.World.", "") for s in k)
    print(f"| {d:.2f}{'~' if rnd else ''} | {n} | {th} | {a} | {b} | {at[0]:.0f}, {at[1]:.1f}, {at[2]:.0f} |")
