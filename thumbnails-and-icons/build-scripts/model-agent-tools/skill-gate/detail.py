import json,sys,os
sys.path.insert(0,"/home/user/Cat-Cafe/assets/cat-cafe/blender")
R="/home/user/Cat-Cafe/assets/cat-cafe/rbx"
def walk(n,out,path=""):
    nm=n.get("name") or n.get("Name") or ""
    p=n.get("properties") or n.get("Properties") or {}
    if "CFrame" in p and "Size" in p: out.append((nm,n.get("className") or n.get("ClassName"),p))
    for c in n.get("children",[]) or n.get("Children",[]): walk(c,out)
name=sys.argv[1]; D=sys.argv[2] if len(sys.argv)>2 else "o2"
parts=[];walk(json.load(open(f"{R}/{name}.model.json")),parts)
vis=[p for p in parts if p[2].get("Transparency",0)<0.99]
r=json.load(open(f"{D}/{name}.json"))[name]
def show(i):
    n,c,p=vis[i]; cf=p["CFrame"]; pos=cf["CFrame"]["position"]
    return f"[{i}] {n[-22:]} {c} size {[round(x,3) for x in p['Size']]} pos {[round(x,3) for x in pos]} col {[round(x,2) for x in p.get('Color',[])]} sh {p.get("Shape","")} tr {p.get('Transparency',0)} mat {p.get('Material','')}"
print(len(parts),len(vis),r["parts"])
for z in r["zf"][:int(os.environ.get("N","8"))]:
    a,b=[int(x.split("_")[0]) for x in z["where"].split("<->")]
    print(z["tri_pairs"]); print("  ",show(a)); print("  ",show(b))
print("FLOAT",r["floating"][:6])
