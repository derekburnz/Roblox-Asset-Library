import json,subprocess,collections,sys,re
N=sys.argv[1];T=sys.argv[2]
old=json.loads(subprocess.check_output(['git','show',f'origin/main:assets/cat-cafe/rbx/{N}.model.json']))
new=json.load(open(f'assets/cat-cafe/rbx/{N}.model.json'))
def cnt(n): return 1+sum(cnt(c) for c in n.get('children',[]))
def models(d,out):
    if d.get('className')=='Model': out.append(d.get('name'))
    for c in d.get('children',[]): models(c,out)
    return out
def parts(d,out,path=''):
    p=path+'/'+str(d.get('name'))
    if d.get('className') in('Part','WedgePart','TrussPart'):
        out[(p,json.dumps(d.get('properties',{}),sort_keys=True),json.dumps(d.get('children',[]),sort_keys=True))]+=1
    for c in d.get('children',[]): parts(c,out,p)
    return out
print('instances',cnt(old),'->',cnt(new),'models same',models(old,[])==models(new,[]),len(models(new,[])))
a=parts(old,collections.Counter());b=parts(new,collections.Counter())
print('removed',sum((a-b).values()),'added',sum((b-a).values()))
g=lambda k:re.sub(r'^.*_\d+_','',k[0].split('/')[-1])
print('removed by group',collections.Counter(g(k) for k in (a-b).elements()).most_common(8))
print('added by group',collections.Counter(g(k) for k in (b-a).elements()).most_common(8))
m=json.load(open('assets/cat-cafe/exports/manifest.json'));t=json.load(open(T+'/out/manifest.json'))
v=m['assets'];tv=t['assets']
if isinstance(v,dict): e=v[N];n=tv[N]
else: e=[x for x in v if x.get('name')==N][0];n=[x for x in tv if x.get('name')==N][0]
for kk in n:
    if kk in('files','preview','views'):continue
    if e.get(kk)!=n[kk] and kk in('triangles','rbx_parts','size'): print(kk, e.get(kk),'->',n[kk])
    e[kk]=n[kk]
open('assets/cat-cafe/exports/manifest.json','w').write(json.dumps(m,indent=2)+'\n')
import shutil
for x in ('fbx','glb'): shutil.copy(f'{T}/out/{N}.{x}',f'assets/cat-cafe/exports/{N}.{x}')
