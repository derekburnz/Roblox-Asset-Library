"""Home thumbnail F, before and after (Growth 2026-11-16): one small cafe with the starter cat, then the big cafe full of
Mythic cats. 1920x1080; nothing key in the bottom 15%."""
import os
from PIL import Image, ImageDraw
import ads as A
import kit17 as K
OUT = os.environ["HOME_OUT"]
W, H = 1920, 1080
A.W, A.H = W, H
left = K.burst((W, H), (0.25, 0.55), (190, 235, 255), (60, 140, 240), n=14, colours=[(255, 255, 255)], alpha=55)
right = K.burst((W, H), (0.75, 0.5), (255, 250, 170), (255, 140, 30), n=16, colours=[(255, 255, 255)], alpha=75)
m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).polygon([(1010, 0), (W, 0), (W, H), (830, H)], fill=255)
img = left.convert("RGBA"); img.paste(right.convert("RGBA"), (0, 0), m)
c = lambda n, h=None, w=None, folder="cozy": K.pop(K.cutp(n, h, w, folder=folder), 1.12, 1.05)
A.hero(img, c("cafe_mint", w=560), 430, 800, rim=12)
A.hero(img, K.pop(A.cut("cat_Tabby", 300)), 250, 900, rim=12)
A.hero(img, c("cafe", w=880), 1420, 800, rim=14, glow=(255, 255, 255))
for n, h, x, y in (("cat_KingCroissant", 330, 1150, 910), ("cat_Comet", 380, 1440, 915), ("cat_Balloon", 330, 1730, 910)):
    A.hero(img, K.pop(K.cutp(n, h)), x, y, rim=12, glow=(255, 230, 160))
d = ImageDraw.Draw(img)
d.line([(1010, 0), (830, H)], fill=(255, 255, 255, 255), width=18)
# the red arrow from before to after
ar = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ad = ImageDraw.Draw(ar)
for wd, col in ((54, (60, 0, 10, 255)), (34, (235, 30, 50, 255))):
    ad.arc([640, 760, 1120, 1040], 20, 160, fill=col, width=wd)
ad.polygon([(1075, 800), (1190, 900), (1050, 960)], fill=(60, 0, 10, 255)); ad.polygon([(1085, 825), (1160, 898), (1068, 938)], fill=(235, 30, 50, 255))
img.alpha_composite(ar)
K.word(img, "1 CAT", 190, 420, 150, K.T.WHITE, -3)
K.word(img, "100+ CATS!", 230, 1430, 150, K.T.GOLD, -3)
A.sparkles(img, [(1100, 330, 90, (255, 255, 255)), (1800, 420, 70, (255, 255, 255))])
img.convert("RGB").save(os.path.join(OUT, "CatCafe_HomeThumb_F_BeforeAfter_1920x1080.png"), optimize=True)
