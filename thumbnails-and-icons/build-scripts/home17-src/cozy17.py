"""Eight cosy ads, one wide 1920x1080 picture each (Roblox Ads Manager size, Derek 2026-11-16 20:07 UTC), in the look of
his winners (Shhh, Cosy Nights, Cosy Cat Cafe, Spa Day, Mystic Pool, Decorate) with Mythic and Secret cats; no bacon.
Key art stays inside the centre 90%; the CATCH A CAT CAFE tag sits bottom right. Names _v2.
Props and sitting cats come from cozy.sh (cozy/), big cats from cut17/."""
import os
import sys

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

import ads as A
import kit17 as K

OUT = os.environ["HOME_OUT"]
W, H = 1920, 1080
A.W, A.H = W, H
GOLD, WHITE, HOT, VIO, PINK, SKY, MINT = A.GOLD, A.WHITE, A.HOT, A.VIO, A.PINK, A.SKY, A.MINT
c = lambda n, h=None, w=None, flip=False: K.pop(K.cutp(n, h, w, flip, folder="cozy"), 1.12, 1.05)
big = lambda n, h: K.pop(K.cutp(n, h))
ICONS = "/home/claude/Cat-Cafe/assets/cat-cafe/exports/icons"
art = lambda n, size: Image.open(os.path.join(ICONS, f"CatCafe_Icon_Arcade_{n}.png")).convert("RGBA").resize((size, size), Image.LANCZOS)


def lines(img, rows, cx=470, top=120, base=280, tilt=4, maxw=820):
    y = top
    for text, style in rows:
        s = min(base, int(maxw * 1.75 / max(4, len(text))))
        A.words(img, text, s, cx, y + s // 2, style, tilt)
        y += int(s * 0.98)
    return y


def zs(img, x, y, k=1.0):
    for i, s in enumerate((110, 150, 190)):
        A.words(img, "Z", int(s * k), int(x + i * 110 * k), int(y - i * 120 * k), WHITE, 10)


def on(img, prop, cat, cx, bottom, sink=0.42, glow=None, rim=12, cat_dx=0):
    A.hero(img, prop, cx, bottom, rim=rim, glow=glow)
    A.hero(img, cat, cx + cat_dx, bottom - int(prop.height * sink), rim=rim, shadow=False)


def a1():
    """Derek's proven Shhh ad (F20, 2026-11-12), same layout: the sleeping orange kitten in its hole in the dim cellar."""
    bd = art("Backdrop", W); y0 = (bd.height - H) // 2
    img = ImageEnhance.Brightness(bd.crop((0, y0, W, y0 + H)).filter(ImageFilter.GaussianBlur(6))).enhance(0.6)
    size, cx, cy = 980, 640, 760
    for n, dy in (("Hole", 0), ("Kitten", -int(size * 0.2)), ("HoleFront", 0)):
        img.alpha_composite(art(n, size), (cx - size // 2, cy - size // 2 + dy))
    A.words(img, "SHHH!", 300, 1400, 420, VIO, -5)
    A.pill(img, "DON'T WAKE THE KITTEN", 1380, 700, 72, tilt=-5)
    for (x, y, s) in ((960, 330, 110), (1060, 210, 150), (1190, 90, 190)):
        A.words(img, "Z", s, x, y, WHITE, 10)
    return img


def a2():
    img = A.bg((70, 60, 160), (16, 14, 60), centre=(0.62, 0.55))
    A.stars(img, 13, 90, 620)
    d = ImageDraw.Draw(img)
    d.ellipse([1540, 90, 1780, 330], fill=(255, 246, 200, 255)); d.ellipse([1480, 60, 1700, 280], fill=(38, 32, 110, 255))
    A.ground(img, 1150, 1010, 1100, 150, (40, 50, 110))
    cafe = c("cafe", w=1150); night = ImageEnhance.Brightness(cafe).enhance(0.66)
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse([700, 600, 1700, 1010], fill=(255, 200, 110, 150))
    img.alpha_composite(g.filter(ImageFilter.GaussianBlur(110)))
    A.hero(img, night, 1220, 1010, rim=0, glow=(255, 210, 130))
    lines(img, [("COSY", GOLD), ("NIGHTS", WHITE)], 450, 110, 270)
    A.hero(img, c("sit_Nebula", 430), 360, 1010, rim=12, glow=(200, 150, 255))
    A.sparkles(img, [(620, 640, 70, (255, 255, 255))])
    return img


def a3():
    """Cosy Cafe: one big cute Mythic cat on a cushion with a coffee (after Derek's Cosy Cat Cafe ad, F12)."""
    img = A.bg((255, 240, 220), (238, 150, 128), centre=(0.68, 0.5))
    A.dots(img, (255, 255, 255), 12, 30, 70)
    K.glow(img, 1300, 600, 520, (255, 250, 230), 220)
    A.hero(img, c("cushion", w=900), 1300, 1010, rim=12)
    A.hero(img, big("cat_Comet", 760), 1290, 900, rim=14, glow=(255, 250, 230), shadow=False)
    A.hero(img, c("coffee", w=300), 800, 1000, rim=10)
    lines(img, [("COSY", WHITE), ("CAT", GOLD), ("CAFE", GOLD)], 430, 100, 270)
    A.heart(img, 1720, 230, 90)
    return img


def a4():
    img = A.bg((215, 245, 255), (60, 130, 240), rays=(255, 255, 255), centre=(0.68, 0.55), ray_alpha=70)
    A.hero(img, c("gate", w=1150), 1290, 1000, rim=0, shadow=False)
    K.glow(img, 1290, 620, 460, (255, 240, 170), 210)
    A.hero(img, big("big_Excalipurr", 720), 1290, 1010, rim=14, glow=(255, 220, 90))
    y = lines(img, [("EXCALI", GOLD), ("PURR!", GOLD)], 450, 150, 270)
    A.pill(img, "SECRET CAT", 450, y + 70, 80, tilt=4)
    A.sparkles(img, [(900, 300, 90, (255, 255, 255)), (1720, 520, 70, (255, 240, 150))])
    return img


def a5():
    img = A.bg((215, 250, 250), (110, 205, 220), centre=(0.68, 0.5))
    A.dots(img, (255, 255, 255), 25, 34, 130, 20, 80)
    A.hero(img, c("tubcat", 860), 1320, 1020, rim=12, glow=(255, 255, 255))
    lines(img, [("CAT", WHITE), ("SPA", HOT), ("DAY!", GOLD)], 430, 100, 280)
    return img


def a6():
    img = A.bg((70, 80, 170), (14, 16, 64), centre=(0.66, 0.6))
    A.stars(img, 6, 90, 600)
    K.glow(img, 1280, 650, 520, (255, 170, 220), 160)
    on(img, c("cushion", w=980), c("sit_Moonstag", 640), 1280, 1010, 0.4, glow=(255, 190, 230))
    lines(img, [("SECRET", VIO), ("NAP", PINK)], 460, 150, 290)
    zs(img, 1560, 420, 0.8)
    return img


def a7():
    img = A.bg((180, 120, 245), (50, 24, 120), rays=(255, 180, 250), centre=(0.68, 0.55), ray_alpha=45)
    A.hero(img, c("pool", 900), 1330, 1020, rim=10, glow=(230, 160, 255))
    A.hero(img, c("sit_Comet", 430), 930, 1010, rim=12, glow=(255, 200, 255), shadow=False)
    y = lines(img, [("NEW!", WHITE)], 300, 90, 170)
    lines(img, [("MYSTIC", GOLD), ("POOL", GOLD)], 430, y + 10, 260)
    return img


def a8():
    img = A.bg((255, 232, 215), (255, 170, 150), rays=(255, 255, 255), centre=(0.5, 0.75), ray_alpha=60)
    A.ground(img, 960, 1010, 1000, 110, (255, 205, 190))
    A.hero(img, c("seat", w=560), 400, 1000, rim=12)
    A.hero(img, c("bed", w=480), 1540, 1000, rim=12)
    on(img, c("cushion", w=640), c("sit_KingCroissant", 520), 980, 1010, 0.4, glow=(255, 250, 230))
    A.words(img, "DECORATE!", 250, 960, 190, GOLD, 0)
    return img


ADS = [("C1_ShhhKitten", a1), ("C2_CosyNights", a2), ("C3_CosyCatCafe", a3), ("C4_Excalipurr", a4), ("C5_CatSpaDay", a5),
       ("C6_SecretNap", a6), ("C7_MysticPool", a7), ("C8_Decorate", a8)]
if __name__ == "__main__":
    pick = sys.argv[1:]
    for name, f in ADS:
        if pick and not any(p in name for p in pick):
            continue
        img = f()
        A.logo(img, 1640, 990, 44)
        p = os.path.join(OUT, f"Ad_{name}_v2_1920x1080.png")
        img.convert("RGB").save(p, optimize=True)
        print("wrote", name, os.path.getsize(p) // 1024, "KB")
