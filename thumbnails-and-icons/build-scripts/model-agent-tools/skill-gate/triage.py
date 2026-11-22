"""Real gaps: for each part the checker calls floating, the box-to-box gap (separating axis, a lower bound) to its
nearest neighbour. Round parts count as their boxes, so a reported gap is at least that big in game."""
import json,glob,os,sys,re
import numpy as np
R="/home/user/Cat-Cafe/assets/cat-cafe/rbx"
def walk(n,out):
    p=n.get("properties") or {}
    if n.get("className") in ("Part","WedgePart"): out.append((n.get("name"),p))
    for c in n.get("children",[]): walk(c,out)
def gap(A,B):
    (ca,Ra,ha),(cb,Rb,hb)=A,B
    d=cb-ca; axes=[Ra[:,i] for i in range(3)]+[Rb[:,i] for i in range(3)]
    for i in range(3):
        for j in range(3):
            x=np.cross(Ra[:,i],Rb[:,j]); n=np.linalg.norm(x)
            if n>1e-6: axes.append(x/n)
    best=-1e9
    for ax in axes:
        ra=sum(abs(ax@Ra[:,i])*ha[i] for i in range(3)); rb=sum(abs(ax@Rb[:,i])*hb[i] for i in range(3))
        best=max(best,abs(d@ax)-ra-rb)
    return best
D=sys.argv[1] if len(sys.argv)>1 else "full"; TH=float(os.environ.get("TH","0.04")); out=[]
for f in sorted(glob.glob(D+"/*.json")):
    k=os.path.basename(f)[:-5]; v=json.load(open(f))[k]
    if not v.get("floating"): continue
    ps=[];walk(json.load(open(f"{R}/{k}.model.json")),ps)
    ps=[p for p in ps if p[1].get("Transparency",0)<0.99]
    box=[(np.array(p["CFrame"]["CFrame"]["position"]),np.array(p["CFrame"]["CFrame"]["orientation"]).T,np.array(p["Size"])/2) for _,p in ps]
    C=np.array([b[0] for b in box]); Rad=np.array([np.linalg.norm(b[2]) for b in box])
    seen=set()
    for x in v["floating"]:
        i=int(x["object"].split("_")[0])
        if i in seen: continue
        seen.add(i)
        dist=np.linalg.norm(C-C[i],axis=1)-Rad-Rad[i]
        g=min((gap(box[i],box[j]) for j in np.where(dist<1.0)[0] if j!=i),default=9.0)
        ground=box[i][0][1]-sum(abs(box[i][1][1,a])*box[i][2][a] for a in range(3))
        if g>TH and ground>0.05:
            out.append((k,i,ps[i][0],round(float(g),3),[round(s,2) for s in ps[i][1]["Size"]],[round(c,1) for c in ps[i][1]["CFrame"]["CFrame"]["position"]],ps[i][1].get("Shape","")))
import collections
by=collections.defaultdict(list)
for o in out: by[o[0]].append(o)
print("models with real gaps:",len(by),"parts:",len(out))
for k,l in sorted(by.items(),key=lambda kv:-len(kv[1])):
    names=collections.Counter(re.sub(r"^CatCafe_","",o[2])[-26:] for o in l)
    print(f"{k} {len(l)} {dict(names.most_common(5))} gaps {sorted({o[3] for o in l})[:6]} e.g. size {l[0][4]} at {l[0][5]} {l[0][6]}")
json.dump(out,open("triage.json","w"))
