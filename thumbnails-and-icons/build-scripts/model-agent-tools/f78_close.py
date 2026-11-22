"""Close three-quarter views of themed cats, walking and sitting, front-left and back-right, from a little above.
usage: python f78_close.py -- <blender_dir> <out_dir> Cat,Cat"""
import os
import sys

argv = sys.argv[sys.argv.index("--") + 1:]
BL, OUT = argv[0], argv[1]
sys.path.insert(0, BL)
import bpy  # noqa: E402
from mathutils import Matrix  # noqa: E402

import cats  # noqa: E402
import common  # noqa: E402
import palette  # noqa: E402

src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "f78_roles.py")).read()
ns = {}
exec("import bpy, common\nfrom mathutils import Matrix\n" + src[src.index("def copies("):src.index("def tree(ob):")], ns)
copies, ortho = ns["copies"], ns["ortho"]
os.makedirs(OUT, exist_ok=True)
common.reset_scene()
png = os.path.join(OUT, "pal.png")
palette.write_palette_png(png)
palette.write_metal_png(png.replace(".png", "_Metal.png"))
mat = common.palette_material(png)
for name in argv[2].split(","):
    walk = cats.build_cat(name, mat, body="walk")
    sit = cats.build_cat(name, mat, body="sit")
    bpy.context.view_layer.update()
    for ob in walk + sit:
        ob.hide_render = True
    shown = copies(walk, Matrix.Translation((0, 0, 0))) + copies(sit, Matrix.Translation((1.7, 0, 0)))
    for view, az in (("f", 35), ("b", 215)):
        ortho(shown, os.path.join(OUT, f"_c_{name}_{view}.png"), az, el=28, res=(900, 600), samples=24)
    for o in shown + walk + sit:
        bpy.data.objects.remove(o, do_unlink=True)
    print(name, "done", flush=True)
