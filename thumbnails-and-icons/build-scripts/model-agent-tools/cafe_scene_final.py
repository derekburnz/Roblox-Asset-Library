"""Furnished Tier 5 cafe at the final Layout points (points.py): python3 scene_final.py <iw> <id> <shell rbx dir> <out dir>
Prints rbx_shot2 model args. PLAN=1 drops interior parts above y 9; the roof is stripped unless ROOF=1."""
import json, os, subprocess, sys
S = "/tmp/claude-0/-home-user-purr-pot/97c3c0a8-cf18-5efa-864c-5f61e996490a/scratchpad"
sys.argv_saved = list(sys.argv)
iw, idp, shell_dir, out = float(sys.argv[1]), float(sys.argv[2]), sys.argv[3], sys.argv[4]
HWI, HDI = iw / 2, idp / 2
pts = json.loads(subprocess.check_output(["python3", S + "/big/points.py", str(iw), str(idp), "--json"]))["points"]
# reuse scene.py's helpers (strip, floor, put) without its furniture
src = open(S + "/big/scene.py").read().split("args.append(floor(")[0]
sys.argv = [sys.argv[0], str(iw), str(idp), shell_dir, out]
g = {"__name__": "scene"}
exec(src, g)
put, args, strip, floor = g["put"], g["args"], g["strip"], g["floor"]
roof = os.environ.get("ROOF", "0") == "0"
def hv(v):
    return eval(str(v), {"halfW": HWI, "halfD": HDI}) if isinstance(v, str) else v
args.append(floor(os.path.join(out, "floor.model.json")) + "@0,0,0")
for m in ("CatCafe_Plot_Cafe_Blush", "CatCafe_Plot_Interior", "CatCafe_Plot_Tier1", "CatCafe_Plot_Tier2",
          "CatCafe_Plot_Tier3", "CatCafe_Plot_Tier4", "CatCafe_Plot_Tier5", "CatCafe_Plot_BackDoor"):
    args.append(strip(m, os.path.join(shell_dir, m + ".model.json"), os.path.join(out, m + ".model.json"), roof) + "@0,0,0")
put("CatCafe_Furniture_Counter", 0, HDI - 3)
put("CatCafe_Furniture_EspressoMachine_L3", 3, HDI - 3, 0, 3)
put("CatCafe_Cafe_Oven", 6.1, HDI - 1.75)
T = []
for i in range(6):
    x, y, z, lane = pts[f"tables[{i + 1}]"]
    T.append((x, z))
    put("CatCafe_Furniture_TableRound", x, z)
    put("CatCafe_Furniture_Chair", x - 2.4, z, -90)
    put("CatCafe_Furniture_Chair", x + 2.4, z, 90)
for i, (v, s) in {0: ("A", -1), 1: ("C", 1), 2: ("E", -1), 4: ("B", 1), 5: ("Rich", -1)}.items():
    x, z = T[i]
    put(f"CatCafe_NPC_Customer_{v}_Sit", x + s * 2.4, z, -90 * s)
for k in (1, 2):
    x, y, z = pts[f"spotFurniture.entertainer_{k}"]
    put("CatCafe_Furniture_CatTree", x, z)
put("CatCafe_Decor_FishTank", -HWI + 2, 0, 90)
x, y, z = pts["decorAnchors.plants"]; put("CatCafe_Decor_WindowPlants", x, hv(z), 0, y)
x, y, z = pts["decorAnchors.rug"]; put("CatCafe_Decor_Rug", x, z)
x, y, z = pts["decorAnchors.neon_sign"]; put("CatCafe_Decor_NeonSign", x, hv(z), 0, y)
x, y, z = pts["INDEX_SPOTS.alley"]; put("CatCafe_Decor_MuralPrint", x, hv(z), 0, y)
x, y, z = pts["INDEX_SPOTS.park"]; put("CatCafe_Decor_ParkBench", hv(x), z, 90)
x, y, z = pts["INDEX_SPOTS.neighbourhood"]; put("CatCafe_Decor_MailboxPlanter", hv(x), z)
x, y, z = pts["INDEX_SPOTS.woods"]; put("CatCafe_Decor_MushroomLamp", hv(x), hv(z))
put("CatCafe_Decor_PipeFountain", HWI - 1.4, HDI - 1.4)
names = ["BlossomTree", "RetroJukebox", "CrateShelf", "BathtubSofa", "TrophyShelf", "PlantPot", "DuckFountain", "IceCreamCounter"]
for i in range(8):
    x, y, z, r = pts[f"decorSpots[{i + 1}]"]
    put(f"CatCafe_Decor_{names[i]}", hv(x), hv(z), r)
for key, n in (("beds", 6), ("napSpots", 4)):
    for i in range(n):
        x, y, z, r = pts[f"{key}[{i + 1}]"]
        put("CatCafe_Furniture_CatBed", x, z, r)
w = [(pts[f"spots.waiter_{k}"][0], pts[f"spots.waiter_{k}"][2]) for k in (1, 2, 3)]
e = [pts[f"spots.entertainer_{k}"] for k in (1, 2)]
cats = [("Tabby", -0.2, HDI - 2.55, 3, 0), ("Calico", -5.2, HDI - 3, 0, 0), ("Siamese", 6.2, HDI - 5.5, 0, 0),
        ("Calico", w[0][0], w[0][1], 0, 0), ("Tabby", w[1][0], w[1][1], 0, 0), ("Siamese", w[2][0], w[2][1], 0, 0),
        ("Tabby", -4, -HDI + 2.5, 0, 180), ("Calico", 4, -HDI + 2.5, 0, 180),
        ("Siamese", e[0][0], e[0][2], e[0][1], 0), ("Tabby", e[1][0], e[1][2], e[1][1], 0)]
for n, x, z, y, r in cats:
    put(f"CatCafe_Cat_{n}_Sit", x, z, r, y)
print("\n".join(args))
