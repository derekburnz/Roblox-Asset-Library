import json,os,re,sys,collections
R='assets/cat-cafe/rbx'
AREAS=["Alleyway","Park","Neighbourhood","Woods","Sewer","Desert","Ruins","Snowy","WaterPark","Castle"]
EXACT=set("CatCafe_Alley_NightFence CatCafe_Alley_NightFenceSegment CatCafe_Alley_Arch CatCafe_Alley_ArchStreet CatCafe_Alley_Mural CatCafe_Alley_FireEscape CatCafe_Alley_WallDoor CatCafe_Alley_WallWindows CatCafe_Square_Paving CatCafe_Square_SignArch CatCafe_Plot_Cafe_Blush CatCafe_Plot_Cafe_Mint CatCafe_Plot_Cafe_Lilac CatCafe_Plot_Cafe_Butter".split())
src=open('games/cat-cafe/src/server/World/ServerOnlyAssets.luau').read()
EXACT|=set(re.findall(r"^\t(CatCafe_\w+) = true",src,re.M))
TAG=r"(?:[A-Z]\d+)?"
def m(n):
    if n in EXACT: return True
    if re.match(r"^CatCafe_Plot_[\w]+_\d+x\d+$",n): return True
    if re.match(r"^CatCafe_[A-Za-z]+_(Set|Backdrop)"+TAG+"$",n): return True
    if re.match(r"^CatCafe_(Alley_Blocker_|Alley_Building_)\w+$",n) and n.count('_')==3: return True
    for a in AREAS:
        if re.match(f"^CatCafe_Camp_{a}{TAG}$",n) or n==f"CatCafe_Nook_{a}": return True
        if re.match(f"^CatCafe_{a}_(Gate|NightFence){TAG}$",n): return True
    return False
def cnt(o):
    return 1+sum(cnt(c) for c in o.get('children',[]) or o.get('Children',[]))
rows=[]
for f in os.listdir(R):
    if not f.endswith('.model.json'): continue
    n=f[:-11]; rows.append((n,cnt(json.load(open(os.path.join(R,f)))),os.path.getsize(os.path.join(R,f)),m(n)))
tot=sum(r[1] for r in rows); so=sum(r[1] for r in rows if r[3])
print("models",len(rows),"instances",tot,"server-only",so,"client",tot-so)
fam=collections.Counter(); famn=collections.Counter()
for n,c,s,x in rows:
    if not x:
        k='_'.join(n.split('_')[:2]); fam[k]+=c; famn[k]+=1
for k,c in fam.most_common(30): print(f"{c:7d} {famn[k]:4d} {k}")
print("top client models:")
for n,c,s,x in sorted([r for r in rows if not r[3]],key=lambda r:-r[1])[:45]: print(f"{c:6d} {n}")
