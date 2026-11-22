"""Skill gate (blender-asset-qa qa_check) over rbx models rebuilt as Blender parts. python run.py NAME [NAME ...]"""
import json, os, sys
R = "/home/user/Cat-Cafe"
sys.path.insert(0, R + "/assets/cat-cafe/blender"); sys.path.insert(0, R + "/.claude/skills/blender-asset-qa/scripts")
import bpy, common, rbx_preview, qa_check  # noqa
RBX = os.environ.get("QA_RBX", R + "/assets/cat-cafe/rbx")
out = {}
for name in sys.argv[1:]:
    common.reset_scene()
    path = os.path.join(RBX, name + ".model.json")
    objs = rbx_preview.build(path, name)
    parts = []; rbx_preview._walk(json.load(open(path)), parts)
    keep = []
    for ob, pp in zip(objs, parts):
        ob.name = f"{len(keep):03d}_{(pp[0] or 'x')[-28:]}"
        if pp[2].get("Transparency", 0) >= 0.99:
            bpy.data.objects.remove(ob, do_unlink=True)
        else:
            keep.append(ob)
    try:
        r = qa_check.run(objects=[o.name for o in keep], profile="game", uv=False)
    except Exception as e:
        out[name] = {"crash": repr(e)}; continue
    out[name] = {"parts": len(keep), "pass": r["pass"], "errors": r["errors"], "zf": r["zfighting"], "floating": r["floating"],
                 "enclosed": r["enclosed"], "b2b": len(r["back_to_back"]), "ground": r["ground_z"],
                 "warn": [w for w in r["warnings"] if "back-to-back" not in w and "material" not in w][:12]}
json.dump(out, open(os.environ.get("QA_OUT", "out.json"), "w"), indent=1, default=str)
