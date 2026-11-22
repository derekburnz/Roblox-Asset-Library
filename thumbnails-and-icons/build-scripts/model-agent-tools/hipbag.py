import re
p="cats.py"; s=open(p).read()
helper = open("/tmp/claude-0/-home-user/222b7bc1-d218-5ad1-8308-8622d7b16e8e/scratchpad/tools/hipbag_helper.txt").read()
i=s.index("def _body_a(spec, c, d):")
s=s[:i]+helper.lstrip("\n")+"\n\n"+s[i:]
a_end = '''                  spec["mane"][(i + 5) % len(spec["mane"])], bevel=False)
    return b
'''
# first occurrence = A, second = B, third = S (if present)
idxs=[m.start() for m in re.finditer(re.escape(a_end), s)]
print("occurrences", len(idxs))
A_hook='''    if spec.get("bag"):                                 # on the right hip, the strap round the waist behind it
        yb = y0 + 0.24 * sy
        _hip_bag(b, spec, -hx - 0.01, yb, z0 - 0.04,
                 [((0, yb, top + 0.012), (sx + 0.03, 0.07, 0.03)), ((hx + 0.012, yb, z0), (0.03, 0.07, sz)),
                  ((0, yb, bottom - 0.012), (sx + 0.03, 0.07, 0.03))])
'''
B_hook='''    if spec.get("bag"):                                 # on the right haunch, the strap over its top
        yb = hy0 + hsy * 0.22
        _hip_bag(b, spec, -hsx / 2 - 0.01, yb, hsz * 0.56,
                 [((0, yb, hsz + 0.012), (hsx + 0.03, 0.07, 0.03)),
                  ((hsx / 2 + 0.012, yb, hsz * 0.55), (0.03, 0.07, hsz * 0.9))])
'''
S_hook='''    if spec.get("bag"):                                 # low on the right side, behind the arm, the strap round the waist
        yb, zb, bot = cy0 + csy * 0.24, cz0 - csz / 2 + 0.16, cz0 - csz / 2
        _hip_bag(b, spec, -csx / 2 - 0.01, yb, zb,
                 [((0, front - 0.012, bot + 0.1), (csx + 0.03, 0.03, 0.07)),
                  ((0, cy0 + csy / 2 + 0.012, bot + 0.1), (csx + 0.03, 0.03, 0.07)),
                  ((csx / 2 + 0.012, cy0, bot + 0.1), (0.03, csy + 0.03, 0.07))])
'''
hooks=[A_hook,B_hook,S_hook][:len(idxs)]
for pos,hook in sorted(zip(idxs,hooks), reverse=True):
    cut=pos+len(a_end)-len("    return b\n")
    s=s[:cut]+hook+s[cut:]
assert len(idxs)>=2
if len(idxs)==2:
    s_end = '''                            ((-0.04, cy0 + csy / 2 + 0.02, cz0 + 0.06), (0.34, 0.07, 0.26), 1, 0)])
'''
    assert s.count(s_end)==1
    s=s.replace(s_end, s_end+S_hook)
bags = {
 'Tabby': ('caramel_wood', 'dark_wood', 'fish'),
 'Tuxedo': ('bowl_red', 'fur_ink', 'newspaper'),
 'Ginger': ('leaf_dark', 'leaf_green', 'sunflower'),
 'Blue': ('pastel_butter', 'fur_cream', 'yarn'),
 'Brownie': ('fur_cream', 'mint', 'brownies'),
 'Biscuit': ('shirt_blue', 'pastel_sky', 'cookies'),
 'Pepper': ('mint', 'leaf_dark', 'chilis'),
 'Butter': ('fur_strawberry', 'offwhite', 'bread'),
 'Moss': ('caramel_wood', 'dark_wood', 'moss'),
 'Acorn': ('leaf_green', 'leaf_dark', 'acorns'),
 'Bramble': ('fur_oat', 'caramel_wood', 'berries'),
 'Fern': ('terracotta', 'caramel_wood', 'ferns'),
}
for name,(bg,fl,kind) in bags.items():
    m=re.search(r'\n    "%s":\s+dict\(.*?\),\n'%name, s, re.S)
    assert m, name
    block=m.group(0)
    nb=block[:-3]+', bag=("%s", "%s", "%s")),\n'%(bg,fl,kind)
    s=s.replace(block,nb,1)
open(p,"w").write(s)
print("ok")
