"""Copy model jsons without the sub-models whose names end with the given suffixes (day renders, hidden pieces).
    python3 strip.py out_dir suffixes,comma in1.model.json [in2 ...]"""
import json, os, sys
out, sufs = sys.argv[1], tuple(sys.argv[2].split(","))
def prune(node):
    node["children"] = [c for c in node.get("children", []) if not (c.get("className") == "Model" and c["name"].endswith(sufs))]
    for c in node["children"]:
        prune(c)
for p in sys.argv[3:]:
    t = json.load(open(p)); prune(t)
    json.dump(t, open(os.path.join(out, os.path.basename(p)), "w"))
