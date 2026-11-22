"""Walk check for any area set, from its Roblox model (run from assets/cat-cafe):
    python3 walk_grid.py CatCafe_Neighbourhood_SetV32 [gate_x,gate_z] [--inside x0,x1,z0,z1] [--png out.png] [-v]
Rasterises every colliding part onto a 0.5 stud grid and walks it from the gate (Dijkstra, 8-way):
  walk: a part blocks when it rises more than 1.05 above the floor and starts below 5 (a player walking, no jumps)
  hop:  only parts topping 7.2 or more block (a player who jumps every low fence), barriers always block
A player is about 2 wide, so blocked cells grow by 0.9. Prints the farthest walk and each spot's walk distance.
"""
import heapq
import json
import math
import sys

import numpy as np

name = sys.argv[1]


def opt(flag):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else None


taken = {sys.argv.index(f) + 1 for f in ("--png", "--inside") if f in sys.argv}
args = [a for k, a in enumerate(sys.argv[2:], 2) if not a.startswith("-") and k not in taken]
gate = tuple(float(v) for v in args[0].split(",")) if args else None
png = opt("--png")
inside = tuple(float(v) for v in opt("--inside").split(",")) if opt("--inside") else None
tree = json.load(open(f"rbx/{name}.model.json"))
parts = []


def walk(node):
    for c in node.get("children", []):
        p = c.get("properties", {})
        if "CFrame" in p and p.get("CanCollide"):
            cf = p["CFrame"]["CFrame"]
            parts.append((c["name"], np.array(cf["position"], float), np.array(cf["orientation"], float),
                          np.array(p["Size"], float) / 2))
        walk(c)


walk(tree)
RES, R = 0.5, 0.9
lo = np.min([c - np.abs(Rm) @ h for _, c, Rm, h in parts], axis=0)
hi = np.max([c + np.abs(Rm) @ h for _, c, Rm, h in parts], axis=0)
x0, z0 = lo[0] - 2, lo[2] - 2
nx, nz = int((hi[0] - x0 + 2) / RES) + 1, int((hi[2] - z0 + 2) / RES) + 1
xs = x0 + np.arange(nx) * RES
zs = z0 + np.arange(nz) * RES
walk_block = np.zeros((nx, nz), bool)
hop_block = np.zeros((nx, nz), bool)
for n, c, Rm, h in parts:
    e = np.abs(Rm) @ h
    ylo, yhi = c[1] - e[1], c[1] + e[1]
    barrier = n.endswith("_Barrier")
    w = yhi > 1.05 and ylo < 5.0
    hp = barrier or (yhi >= 7.2 and ylo < 5.0)
    if not (w or hp):
        continue
    i0, i1 = np.searchsorted(xs, c[0] - e[0] - R), np.searchsorted(xs, c[0] + e[0] + R)
    j0, j1 = np.searchsorted(zs, c[2] - e[2] - R), np.searchsorted(zs, c[2] + e[2] + R)
    if i1 <= i0 or j1 <= j0:
        continue
    gx, gz = np.meshgrid(xs[i0:i1] - c[0], zs[j0:j1] - c[2], indexing="ij")
    # the cell centre in the part's frame, ignoring height; footprint test on the part's two most horizontal axes
    loc = np.stack([gx, np.zeros_like(gx), gz], -1) @ Rm      # columns of Rm are the local axes
    up = np.abs(Rm[1, :])
    k = np.argmax(up)                                          # the axis closest to vertical
    m = np.ones(gx.shape, bool)
    for a in range(3):
        if a == k:
            continue
        m &= np.abs(loc[..., a]) <= h[a] + R
    if w:
        walk_block[i0:i1, j0:j1] |= m
    if hp:
        hop_block[i0:i1, j0:j1] |= m


if inside:                                                     # the walls' inner faces: nothing outside counts
    out = ((xs[:, None] < inside[0]) | (xs[:, None] > inside[1]) | (zs[None, :] < inside[2]) |
           (zs[None, :] > inside[3]))
    walk_block |= out
    hop_block |= out


def cell(x, z):
    return int(round((x - x0) / RES)), int(round((z - z0) / RES))


def dijkstra(block, start):
    dist = np.full(block.shape, np.inf)
    s = cell(*start)
    if block[s]:                                               # start on the nearest free cell
        free = np.argwhere(~block)
        s = tuple(free[np.argmin(((free - np.array(s)) ** 2).sum(1))])
    dist[s] = 0.0
    q = [(0.0, s)]
    steps = [(dx, dz, RES * math.hypot(dx, dz)) for dx in (-1, 0, 1) for dz in (-1, 0, 1) if dx or dz]
    while q:
        d, (i, j) = heapq.heappop(q)
        if d > dist[i, j]:
            continue
        for dx, dz, w in steps:
            a, b = i + dx, j + dz
            if 0 <= a < nx and 0 <= b < nz and not block[a, b]:
                if dx and dz and (block[i + dx, j] or block[i, j + dz]):
                    continue                                   # no corner cutting
                nd = d + w
                if nd < dist[a, b]:
                    dist[a, b] = nd
                    heapq.heappush(q, (nd, (a, b)))
    return dist


if gate is None:
    gate = ((lo[0] + hi[0]) / 2, lo[2] + 3.0)
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
for mode, block in (("walk", walk_block), ("hop", hop_block)):
    dist = dijkstra(block, gate)
    ok = np.isfinite(dist)
    far = np.unravel_index(np.argmax(np.where(ok, dist, -1)), dist.shape)
    print(f"{mode}: reachable {ok.sum() * RES * RES:.0f} sq studs, farthest {dist[far]:.0f} at "
          f"({xs[far[0]]:.0f}, {zs[far[1]]:.0f})")
    rows = []
    for label, lst in pts.items():
        for p in lst:
            i, j = cell(p[0], p[2])
            best = np.inf
            r = 2 if p[1] < 1.5 else 8                         # a seat or deck: from the floor beside it
            for a in range(max(0, i - r), min(nx, i + r + 1)):
                for b in range(max(0, j - r), min(nz, j + r + 1)):
                    best = min(best, dist[a, b])
            rows.append((label, p[0], p[1], p[2], p[3] if len(p) > 3 else "", best))
    unreached = [r for r in rows if not np.isfinite(r[5])]
    zone = {}
    for r in rows:
        if np.isfinite(r[5]):
            zone.setdefault(r[4], []).append(r[5])
    print("   " + ", ".join(f"{z or 'all'} {len(v)} spots, walk {min(v):.0f} to {max(v):.0f}"
                            for z, v in sorted(zone.items())))
    for r in unreached:
        print(f"   NOT REACHED {r[0]} ({r[1]}, {r[2]}, {r[3]}) {r[4]}")
    if "-v" in sys.argv:
        for r in sorted(rows, key=lambda r: r[5]):
            print(f"   {r[0]:16s} {r[1]:7.1f} {r[3]:7.1f} {r[4]:5s} {r[5]:6.0f}")
    if png and mode == "walk":
        from PIL import Image
        img = np.zeros((nz, nx, 3), np.uint8)
        d = np.where(ok, dist, 0)
        t = (d / max(1, d.max()) * 255).astype(np.uint8)
        img[..., 0], img[..., 1], img[..., 2] = t.T, (255 - t).T, 60
        img[block.T] = (40, 40, 40)
        img[~ok.T & ~block.T] = (255, 255, 255)
        Image.fromarray(img[::-1]).resize((nx * 2, nz * 2)).save(png)
