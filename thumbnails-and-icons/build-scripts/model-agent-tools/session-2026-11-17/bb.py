import json,sys,numpy as np,glob,os
R='assets/cat-cafe/rbx/'
def bb(name):
    t=json.load(open(R+name+'.model.json')); lo=np.array([1e9]*3); hi=-lo
    def walk(x):
        nonlocal lo,hi
        for ch in x.get('children',[]):
            p=ch.get('properties',{})
            if 'Size' in p and 'CFrame' in p:
                cf=p['CFrame'].get('CFrame',p['CFrame']); c=np.array(cf['position']); M=np.array(cf['orientation']).reshape(3,3); h=np.abs(M)@(np.array(p['Size'])/2)
                if c[1]+h[1]>0.45:
                    lo=np.minimum(lo,c-h); hi=np.maximum(hi,c+h)
            walk(ch)
    walk(t); return lo,hi
for n in sys.argv[1:]:
    lo,hi=bb(n); print(f"{n:42s} x {lo[0]:6.1f}..{hi[0]:5.1f}  z {lo[2]:6.1f}..{hi[2]:5.1f}  h {hi[1]:.1f}")
