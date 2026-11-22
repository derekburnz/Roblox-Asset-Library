"""Game icon candidate (brief 1, 2026-11-16): one big cat with the net, thick dark outline, solid bright ground, one
sparkle. Plus the test sheet: current against new at 150, 100 and 50 px on a white and a dark tile."""
import os, sys
from PIL import Image, ImageDraw, ImageFilter
import ads as A
OUT = os.environ.get("HOME_OUT")
INK = (60, 24, 10)

def icon(cat="face_Ginger", inner=(140, 235, 255), outer=(30, 150, 245)):
    A.W, A.H = 1024, 1024
    img = A.bg(inner, outer, rays=(255, 255, 255), centre=(0.5, 0.56), ray_alpha=50, n=12)
    A.hero(img, A.cut(cat, 760), 440, 1000, rim=20, rim_rgb=INK, glow=(255, 255, 255))
    net = A.cut("net4", 400).rotate(-12, resample=Image.BICUBIC, expand=True)
    A.hero(img, net, 745, 500, rim=14, rim_rgb=INK)
    A.sparkles(img, [(905, 640, 130, (255, 255, 255))])
    return img.convert("RGB")

if __name__ == "__main__":
    new = icon()
    new.save(os.path.join(OUT, "CatCafe_GameIcon_CatAndNet_1024.png"))
    new.resize((512, 512), Image.LANCZOS).save(os.path.join(OUT, "CatCafe_GameIcon_CatAndNet_512.png"))
    cur = Image.open(sys.argv[1]).convert("RGB")
    sh = Image.new("RGB", (760, 420), (255, 255, 255))
    ImageDraw.Draw(sh).rectangle([380, 0, 760, 420], fill=(25, 27, 32))
    for col, x0 in ((0, 0), (1, 380)):
        for row, im in enumerate((cur, new)):
            x = x0 + 20
            for s in (150, 100, 50):
                t = im.resize((s, s), Image.LANCZOS)
                m = Image.new("L", (s, s), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, s - 1, s - 1], s // 6, fill=255)
                sh.paste(t, (x, 30 + row * 190), m); x += s + 15
    sh.save(os.path.join(OUT, "icon_test_sheet.png"))
