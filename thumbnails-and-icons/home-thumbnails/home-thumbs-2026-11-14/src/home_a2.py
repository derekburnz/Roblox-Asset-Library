"""Home thumbnails, set A with Derek's changes (2026-11-14 18:37 UTC): no avatar, everything bigger for phones, a
cooler cat running down the Rift path at you, cats in the bag, the Castle behind 3 NEW WORLDS, the three Secret cats
side by side, a wizard cat casting a trait with effects. python3 home_a2.py"""
import math, os, random
from PIL import Image, ImageDraw, ImageFilter
import ads as A
from ads import GOLD, WHITE
import home as H
A.W, A.H = 1920, 1080
OUT = H.OUT
CUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cut")


def trim(name, h, flip=False):
    im = Image.open(os.path.join(CUT, name + ".png")).convert("RGBA"); im = im.crop(im.getbbox())
    im = im.resize((int(im.width * h / im.height), int(h)), Image.LANCZOS)
    return im.transpose(Image.FLIP_LEFT_RIGHT) if flip else im


def full(name):
    im = Image.open(os.path.join(CUT, name + ".png")).convert("RGBA")
    return im.resize((1920, 1080), Image.LANCZOS) if im.size != (1920, 1080) else im


def traits():
    img = A.bg((255, 215, 245), (120, 50, 210), rays=(255, 255, 255), centre=(0.68, 0.62), ray_alpha=50)
    cx, cy = 1400, 660
    for r, a in ((470, 70), (360, 110), (250, 150)):                       # the trait's aura round the cat
        H.glow(img, cx, cy, r, (255, 120, 220), a)
    d = ImageDraw.Draw(img)
    for r in (455, 350):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255, 230), width=14)
    A.hero(img, trim("mage", 760), 430, 1075, rim=18, glow=(200, 170, 255), tilt=-3)
    beam = Image.new("RGBA", img.size, (0, 0, 0, 0)); bd = ImageDraw.Draw(beam)
    bd.line([(640, 600), (1130, 640)], fill=(255, 250, 190, 255), width=46)
    img.alpha_composite(beam.filter(ImageFilter.GaussianBlur(16))); ImageDraw.Draw(img).line([(640, 600), (1130, 640)], fill=(255, 255, 255, 255), width=14)
    A.hero(img, trim("t2_neon", 800), cx, 1078, rim=20, glow=(255, 170, 230), tilt=3)
    rnd = random.Random(4)
    A.sparkles(img, [(int(640 + (1130 - 640) * t), int(600 + 40 * t + rnd.uniform(-70, 70)), int(rnd.uniform(46, 80)), (255, 250, 180)) for t in (0.1, 0.35, 0.6, 0.85)]
               + [(1050, 420, 90, (255, 255, 255)), (1790, 430, 80, (255, 255, 255)), (1770, 900, 70, (255, 250, 180))])
    A.words(img, "CAT TRAITS!", 262, 960, 150, GOLD, -2)
    return img


def backpack():
    img = A.bg((255, 250, 200), (255, 140, 60), rays=(255, 255, 255), centre=(0.72, 0.55), ray_alpha=60)
    H.glow(img, 1380, 600, 520, (255, 255, 255), 130)
    A.hero(img, trim("bag_cats", 1060), 1380, 1078, rim=22, glow=(255, 250, 210), tilt=4)
    H.title(img, ["BACK", "PACK!"], 470, 230, 340, [GOLD, GOLD])
    return img


def worlds():
    img = A.bg((255, 245, 215), (110, 190, 255), rays=(255, 255, 255), centre=(0.5, 0.35), ray_alpha=45)
    sc = full("sc_castle"); sc = sc.resize((2200, 1238), Image.LANCZOS)
    img.alpha_composite(sc, (-330, 60))
    A.hero(img, trim("cat_Queen", 660), 1500, 1078, rim=20, glow=(255, 240, 180), tilt=-2)
    A.words(img, "3 NEW WORLDS!", 236, 960, 140, GOLD, -2)
    return img


def secret():
    img = A.bg((255, 225, 150), (120, 50, 200), rays=(255, 250, 220), centre=(0.5, 0.62), ray_alpha=55)
    for n, cx, g, fl in (("x_Moonstag", 330, (200, 240, 255), False), ("x_Phoenix", 960, (255, 235, 150), False), ("x_Excalipurr", 1590, (235, 220, 255), True)):
        H.glow(img, cx, 720, 330, g, 150)
        im = trim(n, 790, flip=fl)
        if im.width > 620:
            im = im.resize((620, int(im.height * 620 / im.width)), Image.LANCZOS)
        A.hero(img, im, cx, 1076, rim=18, glow=g)
    A.words(img, "SECRET CATS!", 262, 960, 150, GOLD, -2)
    return img


def rift():
    img = A.bg((255, 150, 225), (40, 24, 120), rays=(255, 255, 255), centre=(0.72, 0.42), ray_alpha=45)
    A.stars(img, 11, 120, 1080)
    H.glow(img, 1380, 430, 520, (255, 150, 230), 150)
    img.alpha_composite(full("sc_rift"))
    A.sparkles(img, [(980, 420, 80, (255, 255, 255)), (1800, 700, 70, (255, 240, 170))])
    H.title(img, ["RACE", "THE RIFT!"], 500, 230, 280)
    return img


if __name__ == "__main__":
    tiles = []
    for i, (n, f) in enumerate((("CatTraits", traits), ("Backpack", backpack), ("3NewWorlds", worlds), ("SecretCats", secret), ("RaceTheRift", rift)), 1):
        im = f().convert("RGB"); im.save(os.path.join(OUT, f"CatCafe_HomeThumb_{i}_{n}_1920x1080.png")); tiles.append(im.resize((300, 169), Image.LANCZOS))
    sh = Image.new("RGB", (310 * 3 + 10, 179 * 2 + 10), (24, 24, 30))
    for i, t in enumerate(tiles):
        sh.paste(t, (10 + (i % 3) * 310, 10 + (i // 3) * 179))
    sh.save(os.path.join(OUT, "check_300w.png"))
