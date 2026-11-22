import re,json,glob,collections,os,sys
src=open('games/cat-cafe/src/server/World/ServerOnlyAssets.luau').read()
def block(name):
    m=re.search(r'local '+name+r'[^=]*= \{(.*?)\n\}',src,re.S); return set(re.findall(r'(CatCafe_\w+) = true',m.group(1)))
EXACT,STATIONS,CLIENT_SIT=block('EXACT'),block('STATIONS'),block('CLIENT_SIT')
AREAS=["Alleyway","Park","Neighbourhood","Woods","Sewer","Desert","Ruins","Snowy","WaterPark","Castle"]
TAG=r'[A-Z]\d+'
def so(n):
    if n in EXACT or n in STATIONS: return True
    if re.match(r'^CatCafe_Plot_\w+_\d+x\d+$',n): return True
    if re.match(r'^CatCafe_Cat_[A-Za-z0-9]+(_Gold)?_Work$',n): return True
    if (re.match(r'^CatCafe_Cat_[A-Za-z0-9]+_Sit$',n) and n not in CLIENT_SIT) or re.match(r'^CatCafe_Cat_[A-Za-z0-9]+_Gold_Sit$',n): return True
    for k in ("Set","Backdrop"):
        if re.match(r'^CatCafe_[A-Za-z]+_'+k+'('+TAG+')?$',n): return True
    if re.match(r'^CatCafe_(Alley_Blocker_|Alley_Building_)[A-Za-z0-9]+$',n): return True
    if n=="CatCafe_Square_Cannon": return True
    for a in AREAS:
        if n=="CatCafe_Camp_Cannon_"+a or n=="CatCafe_Nook_"+a: return True
        if re.match('^CatCafe_Camp_'+a+'('+TAG+')?$',n): return True
        for k in ("Gate","NightFence"):
            if re.match('^CatCafe_'+a+'_'+k+'('+TAG+')?$',n): return True
    return False
def cnt(n): return 1+sum(cnt(c) for c in n.get('children',[]))
rows=[]
for f in glob.glob('assets/cat-cafe/rbx/*.model.json'):
    n=os.path.basename(f)[:-11]
    rows.append((n,cnt(json.load(open(f))),so(n)))
json.dump(rows,open(sys.argv[1],'w'))
tot=sum(c for _,c,_ in rows); cl=sum(c for _,c,s in rows if not s)
print('models',len(rows),'instances',tot,'client keeps',cl, sum(1 for r in rows if not r[2]))
fam=collections.Counter();famn=collections.Counter()
for n,c,s in rows:
    if s: continue
    p=n.split('_'); k='_'.join(p[:2]) if p[1]!='Cat' else ('Cat_Gold' if '_Gold' in n else 'Cat')
    fam[k]+=c;famn[k]+=1
for k,v in fam.most_common(40): print(k,v,famn[k])
