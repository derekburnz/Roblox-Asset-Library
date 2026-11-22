import json,subprocess
p='assets/cat-cafe/exports/manifest.json'
raw=subprocess.check_output(['git','show','HEAD:'+p]).decode()
head=json.loads(raw); new=json.load(open(p))
hn=[a['name'] for a in head['assets']]; nd={a['name']:a for a in new['assets']}
hd={a['name']:a for a in head['assets']}
print('changed existing',[n for n in hn if n in nd and nd[n]!=hd[n]][:5],'removed',[n for n in hn if n not in nd][:5])
order=list(hn); prev=None
for a in new['assets']:
    n=a['name']
    if n not in hn: order.insert(order.index(prev)+1,n)
    prev=n
new['assets']=[nd[n] for n in order]
out=json.dumps(new,indent=2,ensure_ascii=('\\u' in raw))
if raw.endswith('\n'): out+='\n'
open(p,'w').write(out)
