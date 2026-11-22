import sys, json
B = "/home/user/Cat-Cafe/assets/cat-cafe/blender"
sys.path.insert(0, B)
sys.path.insert(0, "/home/user/Cat-Cafe/.claude/skills/blender-asset-qa/scripts")
import bpy  # noqa
import common, cats, qa_check
names = sys.argv[sys.argv.index("--") + 1:]
png = B + "/../exports/CatCafe_Palette.png"
for n in names:
    for body in ("walk", "sit", "work"):
        common.reset_scene(); mat = common.palette_material(png)
        objs = cats.build_cat(n, mat, body=body)
        r = qa_check.run(objects=[o.name for o in objs], profile="game", eps=0.001, tol=0.003)
        errs = [e for e in r["errors"] if "UV" not in str(e)]
        print(n, body, "pass" if not errs else "FAIL", "|", "; ".join(str(e)[:160] for e in errs[:4]))
