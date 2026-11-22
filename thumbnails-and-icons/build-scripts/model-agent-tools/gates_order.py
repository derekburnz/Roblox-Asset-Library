import subprocess
p='assets/cat-cafe/exports/gates.md'
head=subprocess.check_output(['git','show','HEAD:'+p]).decode().split('\n'); new=open(p).read().split('\n')
key=lambda l: l.split('|')[1].strip() if l.startswith('| CatCafe') else None
hk={key(l) for l in head if key(l)}
out=list(head); out[2]=new[2]
hd={key(l):l for l in head if key(l)}
prev=None
for l in new:
    k=key(l)
    if not k: continue
    if k not in hk:
        i=next(i for i,x in enumerate(out) if key(x)==prev); out.insert(i+1,l)
    elif hd[k]!=l:
        i=next(i for i,x in enumerate(out) if key(x)==k); out[i]=l; print('row changed',k)
    prev=k
open(p,'w').write('\n'.join(out))
