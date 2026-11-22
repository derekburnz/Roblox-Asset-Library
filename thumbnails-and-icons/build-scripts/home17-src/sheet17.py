"""One draft sheet for Derek: icons (with the current one and trending tiles at 100 and 50 px), thumbs A to E at 150 px
high and larger, and the six ads in both sizes."""
import glob, os, sys
from PIL import Image, ImageDraw, ImageFont
D = sys.argv[1]
F = ImageFont.truetype("/mnt/project-files/Model-Agent/store-and-ads/update-2026-11-12/fonts/LilitaOne-Regular.ttf", 34)
f2 = ImageFont.truetype("/mnt/project-files/Model-Agent/store-and-ads/update-2026-11-12/fonts/LilitaOne-Regular.ttf", 24)
W = 2000
sh = Image.new("RGB", (W, 2380), (17, 18, 22)); d = ImageDraw.Draw(sh)
def rt(im, s):
    t = im.convert("RGB").resize((s, s), Image.LANCZOS); m = Image.new("L", (s, s), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, s - 1, s - 1], s // 8, fill=255); return t, m
y = 20
d.text((30, y), "1. GAME ICON: three choices (now, then V1, V2, V3)", font=F, fill=(255, 255, 255)); y += 55
icons = [("Now", "/mnt/project-files/Model-Agent/home-thumbs-2026-11-16/CatCafe_GameIcon_CatAndNet_1024.png")] + \
    [(k, os.path.join(D, f"CatCafe_GameIcon_{k}_1024.png")) for k in ("V1_MythicBlue", "V2_SecretOrange", "V3_MythicOrange")]
x = 30
for name, p in icons:
    t, m = rt(Image.open(p), 340); sh.paste(t, (x, y), m); d.text((x + 6, y + 346), name.replace("_", " "), font=f2, fill=(220, 220, 220)); x += 365
trend = [Image.open(os.path.join(D, "..", "trend", f"t{i}.png")) for i in range(8)]
tx = 1770
d.text((tx - 20, y - 2), "Next to trending", font=f2, fill=(220, 220, 220))
row = trend[:2] + [Image.open(p) for _, p in icons] + trend[2:4]
yy = y + 34
for s in (100, 50):
    xx = 1760 - 0
    cols = row
    xx = W - 30 - (len(cols) // 2) * (s + 8)
    for i, im in enumerate(cols):
        t, m = rt(im, s); sh.paste(t, (xx + (i % 4) * (s + 8) - (s + 8) * 0, yy + (i // 4) * (s + 8)), m)
    yy += 2 * (s + 8) + 14
y += 400
d.text((30, y), "2. HOME THUMBNAILS A to E (E unchanged, it is the test control)", font=F, fill=(255, 255, 255)); y += 55
th = sorted(glob.glob(os.path.join(D, "CatCafe_HomeThumb_*_1920x1080.png")))
for i, p in enumerate(th):
    im = Image.open(p).convert("RGB")
    if i < 4:
        sh.paste(im.resize((640, 360), Image.LANCZOS), (30 + (i % 3) * 655, y + (i // 3) * 375))
    else:
        sh.paste(im.resize((640, 360), Image.LANCZOS), (30 + 655, y + 375))
for i, p in enumerate(th):
    sh.paste(Image.open(p).convert("RGB").resize((267, 150), Image.LANCZOS), (30 + 2 * 655 + (i % 2) * 280, y + 375 + (i // 2) * 160 - (0 if i < 4 else 0)))
d.text((30 + 2 * 655, y + 375 + 3 * 160 - 150 + 110, ), "", font=f2, fill=(220, 220, 220))
y += 2 * 375 + 130
d.text((30, y), "3. ADS: six hooks, square and tall", font=F, fill=(255, 255, 255)); y += 55
sq = sorted(glob.glob(os.path.join(D, "Ad_*_1080x1080.png"))); tl = sorted(glob.glob(os.path.join(D, "Ad_*_1080x1920.png")))
for i, p in enumerate(sq):
    sh.paste(Image.open(p).convert("RGB").resize((315, 315), Image.LANCZOS), (30 + i * 325, y))
for i, p in enumerate(tl):
    sh.paste(Image.open(p).convert("RGB").resize((315, 560), Image.LANCZOS), (30 + i * 325, y + 325))
sh.save(os.path.join(D, "DRAFT_SHEET_everything.png"))
sh.resize((1500, int(sh.height * 0.75)), Image.LANCZOS).save(os.path.join(D, "DRAFT_SHEET_everything_small.jpg"), quality=90)
print("sheet", sh.size, y + 325 + 560)
