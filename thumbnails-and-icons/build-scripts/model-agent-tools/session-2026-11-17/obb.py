import numpy as np, sys, collections
def load(p):
    P=[]
    for l in open(p):
        f=l.rstrip('\n').split('\t')
        try:
            c=np.array(list(map(float,f[3:6]))); R=np.array(list(map(float,f[6:15]))).reshape(3,3); s=np.array(list(map(float,f[15:18]))); tr=float(f[18])
        except Exception: continue
        if tr>=0.95 or s.max()>200: continue
        P.append((f[0],c,R,s/2))
    return P
def sat(a,b,shrink=0.05):
    ca,Ra,ha=a[1],a[2],np.maximum(a[3]-shrink,0.001); cb,Rb,hb=b[1],b[2],np.maximum(b[3]-shrink,0.001)
    A=[Ra[:,i] for i in range(3)]; B=[Rb[:,i] for i in range(3)]
    t=cb-ca
    axes=A+B+[np.cross(x,y) for x in A for y in B]
    for ax in axes:
        n=np.linalg.norm(ax)
        if n<1e-6: continue
        ax=ax/n
        ra=sum(ha[i]*abs(np.dot(A[i],ax)) for i in range(3)); rb=sum(hb[i]*abs(np.dot(B[i],ax)) for i in range(3))
        if abs(np.dot(t,ax))>ra+rb: return False
    return True
def rad(p): return np.linalg.norm(p[3])
def hits(A,B,shift=np.zeros(3),shrink=0.05):
    out=collections.Counter()
    for a in A:
        a2=(a[0],a[1]+shift,a[2],a[3]); ra=rad(a)
        for b in B:
            if np.linalg.norm(b[1]-a2[1])>ra+rad(b): continue
            if sat(a2,b,shrink): out[b[0].rsplit('.',1)[0]]+=1
    return out
