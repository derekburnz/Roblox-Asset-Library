"""The Mystic Pool (#3314, trait-station.md section 1): the Park's Picnic Basket camp extra reworked into the trait
station. DRAFT for Derek's look (2026-11-11), not wired into build_all yet.

  CatCafe_Camp_Park_MysticPool        a round stone basin of glowing liquid on a starry mosaic disc, ringed by five
                                      standing rune stones whose gems are the five rarity colours in order (grey,
                                      green, blue, gold, purple: the colour steps the pool walks through), a MYSTIC
                                      POOL board on a post, and Sage Sorrel, an old silver wizard cat with a white
                                      beard, a tall starry violet hat and a robe, sitting on a stone plinth by the
                                      pool with a staff topped by a glowing orb.
                                      Child pieces: `_Water` (the liquid; the client tints it per rarity), `_Orb`
                                      (the staff's orb, glows), Sorrel's hinged sitting-cat pieces (Head, Eye1, Eye2,
                                      EarL, EarR, Tail, LegF1, LegF2) with `_Hat` riding the Head and `_Robe`.
                                      Attachments: PromptAnchor (front of the pool, 1.5 up), BangAnchor (2 over the
                                      sign), CatDrop (3 over the pool's middle, where the rolled cat floats before the
                                      drop), PoolCentre (the liquid's surface middle), OrbGlow (the orb).

Pivot at the base centre on the camp's ground, front -Z, no turn, at the Picnic station's spot.

Run on its own (draft): python mysticpool.py   (with the bpy module), or blender -b -P mysticpool.py
"""

import math
import os
import sys

from mathutils import Matrix, Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import cats  # noqa: E402
import common  # noqa: E402
import palette  # noqa: E402
import props  # noqa: E402
from common import RB, Builder, scale_mesh, text_width  # noqa: E402

NAME = "CatCafe_Camp_Park_MysticPool"
ATTACHMENTS = {}

DISC_R, DISC_Y = 5.2, 0.2                       # the mosaic disc under it all
POOL_R, RIM_T, RIM_Y, LIQ_Y = 2.4, 0.55, 1.1, 0.95
STONE, STONE_DARK = "fur_silver", "concrete"
ROBE, ROBE_TRIM, STAR = "galaxy_blue", "aurora_violet", "sparkle"
HAT = "aurora_violet"
RARITY_GEMS = ("rarity_common", "leaf_green", "rarity_rare", "rarity_legend", "rarity_epic")
SORREL = dict(rarity="Common", fur="fur_silver", second="fur_smoke_light", eyes="eye_violet", pattern="solid",
              muzzle="fur_white", nose="nose_dark", scale=1.9)
SORREL_AT = (-3.6, 0.0, 0.9)                     # Roblox: left of the pool, a little back
PLINTH_H = 0.7


def _anchor(att, p):
    ATTACHMENTS[att] = p


def _disc(b):
    """A starry mosaic disc: night-sky tiles in a ring pattern with gold and sparkle stars, a gold edge."""
    segs = 24
    b.cyl((0, DISC_Y / 2, 0), DISC_R + 0.15, DISC_Y, "gold_mid", segments=segs)
    b.cyl((0, DISC_Y + 0.01, 0), DISC_R, 0.04, "night_sky", segments=segs)
    for k in range(segs):
        a = 2 * math.pi * k / segs
        r = DISC_R - 0.45
        b.box((r * math.cos(a), DISC_Y + 0.04, r * math.sin(a)), (0.35, 0.03, 0.35),
              ("galaxy_blue", "aurora_violet")[k % 2], rot=Matrix.Rotation(-a, 3, "Y"))
    for (x, z, s) in ((3.4, -2.6, 0.32), (-1.2, -3.9, 0.24), (2.0, 3.6, 0.28), (4.1, 1.2, 0.2), (-2.4, 3.9, 0.22),
                      (0.9, -4.3, 0.18)):
        b.box((x, DISC_Y + 0.05, z), (s, 0.03, s * 0.25), STAR)
        b.box((x, DISC_Y + 0.055, z), (s * 0.25, 0.03, s), STAR)


def _basin(b, water):
    """The round stone basin: a ring of chunky blocks, a darker plinth under them, a glowing liquid inside."""
    n = 16
    for k in range(n):
        a = 2 * math.pi * k / n
        r = POOL_R + RIM_T / 2
        R = Matrix.Rotation(-a, 3, "Y")
        b.box((r * math.cos(a), (DISC_Y + RIM_Y) / 2, r * math.sin(a)),
              (RIM_T + 0.1, RIM_Y - DISC_Y, 2 * math.pi * r / n + 0.08), (STONE, "fur_smoke_light")[k % 2], rot=R)
        b.box((r * math.cos(a), RIM_Y + 0.06, r * math.sin(a)), (RIM_T + 0.2, 0.12, 2 * math.pi * r / n + 0.1),
              "offwhite", rot=R)
    b.cyl((0, DISC_Y + 0.05, 0), POOL_R + 0.05, 0.1, STONE_DARK, segments=n)          # the basin floor
    # the liquid reaches a hair into the rim so its side never shares a plane with the stones
    water.cyl((0, (DISC_Y + 0.1 + LIQ_Y) / 2, 0), POOL_R + 0.02, LIQ_Y - DISC_Y - 0.1, "rarity_epic", segments=n)
    _anchor("PoolCentre", (0.0, LIQ_Y, 0.0))
    _anchor("CatDrop", (0.0, LIQ_Y + 3.0, 0.0))


def _rune_stones(b):
    """Five standing stones round the back of the pool, each with a gem in one rarity colour, left to right in
    the order the pool's colour climbs: grey, green, blue, gold, purple."""
    for i, gem in enumerate(RARITY_GEMS):
        a = math.radians(200 + i * 35)              # an arc behind the pool
        r = POOL_R + 1.6
        x, z = r * math.cos(a), -r * math.sin(a)
        h = 1.6 + 0.35 * (2 - abs(i - 2))           # tallest in the middle
        R = Matrix.Rotation(-(a + math.pi / 2), 3, "Y")
        b.box((x, DISC_Y + h / 2, z), (0.7, h, 0.45), STONE, rot=R)
        b.box((x, DISC_Y + h + 0.12, z), (0.55, 0.25, 0.38), STONE_DARK, rot=R)       # a cap
        gx, gz = x - 0.24 * math.cos(a), z + 0.24 * math.sin(a)                        # on the pool-facing side
        b.box((gx, DISC_Y + h - 0.45, gz), (0.3, 0.3, 0.3), gem, rot=R @ Matrix.Rotation(math.radians(45), 3, "Z"))


def _sign(b):
    """MYSTIC POOL on a dark board on a carved post, front right. Returns the board's top."""
    x, z = 3.9, -2.9
    b.span((x - 0.22, DISC_Y, z - 0.22), (x + 0.22, DISC_Y + 2.9, z + 0.22), "dark_wood")
    hw, y0, y1 = 1.55, DISC_Y + 2.9, DISC_Y + 4.3
    b.span((x - hw, y0, z - 0.12), (x + hw, y1, z + 0.12), "dark_wood")
    b.span((x - hw + 0.12, y0 + 0.12, z - 0.15), (x + hw - 0.12, y1 - 0.12, z - 0.12), "night_sky")
    for s, y, sw in (("MYSTIC", y0 + 0.72, "sparkle"), ("POOL", y0 + 0.2, "aurora_violet")):
        w = text_width(s, 0.09)
        b.text(s, (x + w / 2, y, z - 0.15), 0.09, 0.04, sw, right=(-1, 0, 0))
    b.span((x - hw - 0.1, y1, z - 0.2), (x + hw + 0.1, y1 + 0.15, z + 0.2), "gold_mid")
    b.box((x, y1 + 0.45, z), (0.35, 0.35, 0.12), "gold_light", rot=Matrix.Rotation(math.radians(45), 3, "Z"))
    return (x, y1 + 0.6, z)


def _plinth(b):
    x, _, z = SORREL_AT
    b.cyl((x, DISC_Y + PLINTH_H / 2, z), 1.25, PLINTH_H, STONE_DARK, segments=10)
    b.cyl((x, DISC_Y + PLINTH_H + 0.05, z), 1.15, 0.1, "aurora_violet", segments=10)   # a violet cushion top


def _staff(b, orb):
    """Sorrel's staff, planted on the plinth at the cat's right (toward the pool), its orb at the top."""
    x, _, z = SORREL_AT
    sx, sz = x + 1.0, z - 0.55
    top = DISC_Y + PLINTH_H + 4.4
    b.cyl((sx, (DISC_Y + PLINTH_H + top) / 2, sz), 0.08, top - DISC_Y - PLINTH_H, "dark_wood", segments=8)
    for k in range(3):                                                            # gold bands
        b.cyl((sx, top - 0.2 - 0.35 * k, sz), 0.1, 0.07, "gold_mid", segments=8)
    for k in range(4):                                                            # prongs holding the orb
        a = 2 * math.pi * k / 4 + math.pi / 4
        b.box((sx + 0.2 * math.cos(a), top + 0.18, sz + 0.2 * math.sin(a)), (0.06, 0.4, 0.06), "gold_mid")
    orb.ball((sx, top + 0.42, sz), 0.32, "rarity_epic")
    _anchor("OrbGlow", (sx, top + 0.42, sz))


def _hat(ctx):
    """A tall pointed wizard hat on the head frame (origin on the head's top, z up, y to the back): a wide brim,
    a cone in four steps that droops back at its tip, a gold band with a crescent and a few stars."""
    P = ctx.pen("head")
    P.cyl((0, 0.02, 0.03), 0.78, 0.06, HAT, segments=16)                                    # brim
    P.cyl((0, 0.02, 0.1), 0.5, 0.1, "gold_mid", segments=16)                                 # band
    steps = ((0.49, 0.38, 0.35, 0.0), (0.38, 0.27, 0.35, 0.05), (0.27, 0.16, 0.3, 0.14), (0.16, 0.05, 0.28, 0.28))
    z, y = 0.15, 0.02
    for r0, r1, h, back in steps:
        P.cyl((0, y + back, z + h / 2), r0, h, HAT, r2=r1, segments=12)
        z += h
        y += back * 0.6
    ctx.main.crescent(P.p((0, -0.5, 0.42)), 0.12 * P.s, 0.06 * P.s, 0.04 * P.s, "gold_light")
    for (x, zz, s) in ((0.25, 0.55, 0.1), (-0.2, 0.8, 0.08), (0.12, 1.0, 0.07)):
        P.box((x, -0.38 + zz * 0.25, zz), (s, 0.03, s * 0.28), STAR)
        P.box((x, -0.38 + zz * 0.25, zz), (s * 0.28, 0.03, s), STAR)


def _beard(ctx):
    """A white beard and brows on the face frame (front of the face, z up): a tapered beard in three blocks."""
    P = ctx.pen("face")
    for i, (w, h, z) in enumerate(((0.62, 0.16, -0.26), (0.48, 0.18, -0.42), (0.28, 0.16, -0.58))):
        P.box((0, -0.06, z), (w, 0.18, h), "fur_white")
    for sx in (1, -1):
        P.box((sx * 0.2, -0.06, 0.2), (0.24, 0.1, 0.07), "fur_white")             # bushy brows


def _robe(b):
    """The robe over the sitting body (Blender axes on the seat): a wide skirt over the haunches, a body over the
    chest, a violet trim and gold buttons, a few stars, open at the front so the chest shows."""
    b.box((0, 0.1, 0.32), (1.05, 0.95, 0.5), ROBE)                      # skirt over the haunches
    b.box((0, 0.22, 0.75), (0.86, 0.5, 0.45), ROBE)                     # over the back of the chest
    for sx in (1, -1):
        b.box((sx * 0.4, -0.05, 0.75), (0.08, 0.45, 0.45), ROBE)       # its sides
        b.box((sx * 0.4, -0.29, 0.6), (0.1, 0.04, 0.7), ROBE_TRIM)     # trim down the opening
    b.box((0, -0.38, 0.1), (1.07, 0.04, 0.12), ROBE_TRIM)               # hem
    for z in (0.55, 0.7, 0.85):
        b.sphere((0.3, -0.33, z), 0.035, "gold_mid", segments=6, rings=4)
    for (x, y, z, s) in ((0.53, 0.1, 0.35, 0.14), (-0.53, 0.25, 0.4, 0.12), (0.2, 0.58, 0.6, 0.12)):
        b.box((x, y, z), (s, s * 0.25, 0.03) if abs(x) < 0.5 else (0.03, s, s * 0.25), STAR)


def build_mystic_pool(mat):
    b, water, orb = RB(), RB(), RB()
    _disc(b)
    _basin(b, water)
    _rune_stones(b)
    top = _sign(b)
    _plinth(b)
    _staff(b, orb)
    _anchor("PromptAnchor", (0.0, 1.5, -POOL_R - 1.4))
    _anchor("BangAnchor", (top[0], top[1] + 2.0, top[2]))
    objs = [b.finalize(NAME, mat), water.finalize(NAME + "_Water", mat), orb.finalize(NAME + "_Orb", mat)]

    base = NAME + "_Sorrel"
    cat = cats.build_cat("Sorrel", mat, spec=SORREL, base=base, body="sit")
    d = cats.dims(SORREL, "sit")
    k = cats.scale_of(SORREL, "sit")
    ctx = props.Ctx(SORREL, "sit", d)
    _hat(ctx)
    hat = ctx.main.finalize(base + "_Hat", mat, location=tuple(v * k for v in d["pivots"]["Head"]))
    scale_mesh(hat, k)
    hat["rides"] = "Head"
    bctx = props.Ctx(SORREL, "sit", d)
    _beard(bctx)
    beard = bctx.main.finalize(base + "_Beard", mat, location=tuple(v * k for v in d["pivots"]["Head"]))
    scale_mesh(beard, k)
    beard["rides"] = "Head"
    rb = Builder()
    _robe(rb)
    robe = rb.finalize(base + "_Robe", mat)
    scale_mesh(robe, k)
    x, _, z = SORREL_AT
    for ob in cat + [hat, beard, robe]:
        ob.location = ob.location + Vector(RB.p(x, DISC_Y + PLINTH_H + 0.1, z))
    return objs + cat + [hat, beard, robe]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "..", "exports")
    concepts = os.path.join(here, "..", "..", "..", "docs", "concepts", "cat-cafe")
    common.reset_scene()
    png = os.path.join(out, palette.TEXTURE_NAME + ".png")
    palette.write_palette_png(png)
    mat = common.palette_material(png)
    objs = build_mystic_pool(mat)
    print("triangles:", common.tri_count(objs))
    common.export_asset(objs, NAME, out, glb=True)
    os.makedirs(concepts, exist_ok=True)
    for az, tag in ((35, "front"), (-50, "side")):
        common.render_preview(objs, os.path.join(concepts, f"{NAME}_draft_{tag}.png"), res=(1280, 960), samples=48,
                              azimuth=az, elevation=24)
    print("attachments:", ATTACHMENTS)


if __name__ == "__main__":
    main()
