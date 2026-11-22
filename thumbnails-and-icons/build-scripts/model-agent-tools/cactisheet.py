import os, sys
B = "/home/user/Cat-Cafe/assets/cat-cafe/blender"
sys.path.insert(0, B)
import bpy  # noqa
import common, desertset as ds, ruinsset as rs
OUT = sys.argv[sys.argv.index("--out") + 1]
which = sys.argv[sys.argv.index("--set") + 1]
os.makedirs(OUT, exist_ok=True)
D0 = [("pot", lambda m: ds.pot(m)), ("crate", ds.crate), ("rock", ds.rock), ("shrub", ds.shrub), ("lamp", ds.lamp),
     ("canopy", ds.canopy), ("wagon", ds.wagon), ("palm_stump", ds.palm_stump), ("signpost", ds.signpost),
     ("palm", ds.palm), ("oasis_pool", ds.oasis_pool), ("well", ds.well), ("obelisk", ds.obelisk),
     ("obelisk_broken", lambda m: ds.obelisk(m, broken=True)), ("spire", ds.spire), ("rock_arch", ds.rock_arch),
     ("pyramid", ds.pyramid), ("trap_sand_dune", ds.trap_sand_dune), ("trap_clay_urn", ds.trap_clay_urn),
     ("trap_collapsed_canopy", ds.trap_collapsed_canopy)]
D = [("cactus_paddle", lambda m: ds.soft_cactus(m, 0)), ("cactus_barrel", lambda m: ds.soft_cactus(m, 1)), ("cactus_arm", lambda m: ds.soft_cactus(m, 2))]
R = [("column", rs.column), ("column_broken", lambda m: rs.column(m, broken=True)), ("drums", rs.drums),
     ("fountain", rs.fountain), ("throne", rs.throne), ("brazier", rs.brazier), ("stone_urn", rs.stone_urn),
     ("rubble", rs.rubble), ("gargoyle", rs.gargoyle), ("gate_pylon", rs.gate_pylon), ("fallen_lintel", rs.fallen_lintel),
     ("pier", rs.pier), ("trap_rubble_pile", rs.trap_rubble_pile), ("trap_stone_urn", rs.trap_stone_urn)]
png = os.path.join(B, "..", "exports", "CatCafe_Palette.png")
for name, fn in (D if which == "desert" else R):
    common.reset_scene(); mat = common.palette_material(png)
    try:
        objs = fn(mat)
        objs = [o for o in objs if o is not None]
        common.render_preview(objs, os.path.join(OUT, f"{which}_{name}.png"), res=(360, 300), samples=12)
        print("ok", name, common.tri_count(objs))
    except Exception as e:
        print("FAIL", name, repr(e))
