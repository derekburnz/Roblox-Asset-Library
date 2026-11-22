"""Resolve a merge of main into a model branch for the two generated files. Run in the worktree mid-merge.
Takes main's file and re-inserts the rows this branch added (ours minus merge-base), each after its predecessor."""
import json, re, subprocess, sys
def show(ref, p): return subprocess.check_output(['git','show',f'{ref}:{p}']).decode()
base=subprocess.check_output(['git','merge-base','HEAD','MERGE_HEAD']).decode().strip()
# manifest
p='assets/cat-cafe/exports/manifest.json'
ro,rb,rt=show('HEAD',p),show(base,p),show('MERGE_HEAD',p)
o,b,t=json.loads(ro),json.loads(rb),json.loads(rt)
bn={a['name'] for a in b['assets']}; tn=[a['name'] for a in t['assets']]; td={a['name']:a for a in t['assets']}
prev=None; added=0
for a in o['assets']:
    n=a['name']
    if n not in bn and n not in td:
        i=tn.index(prev)+1 if prev in tn else len(tn); tn.insert(i,n); td[n]=a; added+=1
    elif n not in bn: print('both added',n)
    elif n in td and a!=next(x for x in b['assets'] if x['name']==n): td[n]=a; print('ours changed',n)
    prev=n
t['assets']=[td[n] for n in tn]
out=json.dumps(t,indent=2,ensure_ascii=('\\u' in rt))+('\n' if rt.endswith('\n') else '')
open(p,'w').write(out); print('manifest rows added',added)
# gates
p='assets/cat-cafe/exports/gates.md'
lo,lb,lt=[show(r,p).split('\n') for r in ('HEAD',base,'MERGE_HEAD')]
key=lambda l: l.split('|')[1].strip() if l.startswith('| CatCafe') else None
bk={key(l):l for l in lb if key(l)}; tk={key(l) for l in lt if key(l)}
out=list(lt); prev=None; added=0
for l in lo:
    k=key(l)
    if not k: continue
    if k not in bk and k not in tk:
        i=next((i for i,x in enumerate(out) if key(x)==prev),len(out)-1); out.insert(i+1,l); added+=1
    elif k in bk and bk[k]!=l and k in tk:
        i=next(i for i,x in enumerate(out) if key(x)==k); out[i]=l; print('gates ours changed',k)
    prev=k
num=lambda s: [int(x) for x in re.findall(r'(\d+) assets: (\d+) PASS \((\d+) with warnings\), (\d+) FAIL',s)[0]]
no,nb,nt=num(lo[2]),num(lb[2]),num(lt[2]); nn=[nt[i]+no[i]-nb[i] for i in range(4)]
out[2]=re.sub(r'\d+ assets: \d+ PASS \(\d+ with warnings\), \d+ FAIL',f'{nn[0]} assets: {nn[1]} PASS ({nn[2]} with warnings), {nn[3]} FAIL',lt[2])
open(p,'w').write('\n'.join(out)); print('gates rows added',added,nn)
rows=sum(1 for l in out if key(l)); print('gate rows',rows,'manifest',len(tn))
