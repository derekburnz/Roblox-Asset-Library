"""Home page thumbnails, set of 2026-11-16 (Growth-Agent brief home-recs-2026-11-16/briefs/1): A Catch it, B cats at
work, C collection, D cannon. One big hero, one big word or number, bright, nothing that matters in the bottom 15%.
FA_EV=<update-2026-11-12> python3 home16.py [A B C D]"""
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

import ads as A
from ads import C, C2, GOLD, WHITE

A.W, A.H = W, H = 1920, 1080
OUT = os.environ.get("HOME_OUT", "/mnt/project-files/Model-Agent/home-thumbs-2026-11-16")
os.makedirs(OUT, exist_ok=True)
MYTH = ((255, 215, 235), (255, 70, 150), (90, 10, 60))
GREEN = ((225, 255, 170), (70, 215, 70), (10, 70, 20))
RARITY = {"Common": (175, 185, 200), "Rare": (70, 160, 255), "Epic": (180, 90, 255), "Legendary": (255, 180, 30),
          "Mythical": (255, 70, 150)}


def glow(img, cx, cy, r, rgb, a=170):
    g = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(g).ellipse([cx - r, cy - r, cx + r, cy + r], fill=rgb + (a,))
    img.alpha_composite(g.filter(ImageFilter.GaussianBlur(r // 3)))


def streaks(img, x0, y0, x1, y1, n=9, spread=150, rgb=(255, 255, 255), alpha=150, width=16):
    """Speed lines from (x0, y0) toward (x1, y1), fanned `spread` px across."""
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    nx, ny = -dy / L, dx / L
    for i in range(n):
        k = (i / (n - 1) - 0.5) * 2
        s = 0.15 + 0.25 * ((i * 37) % 10) / 10
        e = 0.75 + 0.2 * ((i * 53) % 10) / 10
        ax, ay = x0 + dx * s + nx * k * spread, y0 + dy * s + ny * k * spread
        bx, by = x0 + dx * e + nx * k * spread * 0.55, y0 + dy * e + ny * k * spread * 0.55
        d.line([(ax, ay), (bx, by)], fill=rgb + (alpha,), width=int(width * (1 - abs(k) * 0.5)))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(2)))


def arc(img, pts, rgb, width, alpha=255, ink=None):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    if ink:
        d.line(pts, fill=ink + (alpha,), width=width + 22, joint="curve")
    d.line(pts, fill=rgb + (alpha,), width=width, joint="curve")
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(1.5)))


def bezier(p0, p1, p2, n=40):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
             (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]) for t in [i / n for i in range(n + 1)]]


def catch():
    img = A.bg((255, 255, 255), (60, 165, 255), rays=(255, 255, 255), centre=(0.72, 0.58), ray_alpha=70)
    glow(img, 1400, 600, 560, (255, 190, 230), 210)
    streaks(img, 300, 700, 1150, 560, n=9, spread=230, alpha=150)
    A.hero(img, A.cut("cat_Balloon", 840), 1420, 965, rim=24, rim_rgb=(255, 255, 255), glow=(255, 80, 170), tilt=-7)
    A.hero(img, A.cut("pl_net", 700), 560, 1045, rim=14, tilt=4)
    A.sparkles(img, [(1050, 330, 80, (255, 255, 255)), (1810, 420, 90, (255, 255, 255)), (1080, 900, 60, (255, 240, 160)),
                     (1830, 820, 60, (255, 240, 160))])
    A.words(img, "MYTHICAL!", 250, 620, 170, MYTH, -4)
    return img


def work():
    room = A.photo("/mnt/project-files/Model-Agent/store-and-ads/ads-2026-11-08/Ad_05_DecorateCafe_raw.png", 1.25, 0.5, 0.45, blur=7)
    img = room.convert("RGBA")
    warm = Image.new("RGBA", img.size, (255, 190, 90, 70))
    img.alpha_composite(warm)
    glow(img, 960, 640, 700, (255, 245, 200), 150)
    for name, cx, h, t in (("work_Tabby", 430, 660, -4), ("work_Tuxedo", 1500, 660, 4), ("work_Ginger", 960, 760, 0)):
        A.hero(img, A.cut(name, h), cx, 990, rim=20, glow=(255, 240, 190), tilt=t)
    A.words(img, "$1,000,000", 270, 960, 160, GREEN, -3)
    for (x, y, s) in ((250, 420, 150), (1690, 430, 150), (680, 330, 110), (1250, 330, 110)):
        A.words(img, "$", s, x, y, GREEN, (x % 30) - 15)
    return img


def collection():
    img = A.bg((255, 252, 225), (255, 165, 70), rays=(255, 255, 255), centre=(0.5, 0.6), ray_alpha=60)
    cats = [("cat_Tabby", "Common"), ("cat_Tortie", "Rare"), ("cat_Taxi", "Epic"), ("cat_Void", "Legendary"),
            ("cat_Duckling", "Epic"), ("cat_Calico", "Rare"), ("cat_Blossom", "Legendary"), ("cat_Neon", "Mythical")]
    back, front = cats[:4], [cats[4], cats[7], cats[6]]
    for row, y, h, xs in ((back, 640, 380, (300, 740, 1180, 1620)), (front, 965, 430, (520, 960, 1400))):
        for (name, rar), cx in zip(row, xs):
            glow(img, cx, y - h // 2, h // 2 + 30, RARITY[rar], 170)
            A.hero(img, A.cut(name, h), cx, y, rim=16, rim_rgb=(255, 255, 255), glow=RARITY[rar])
    A.words(img, "100+ CATS!", 250, 960, 130, GOLD, -2)
    return img


def cannon():
    img = A.bg((255, 255, 255), (70, 170, 255), rays=(255, 255, 255), centre=(0.2, 0.9), ray_alpha=65, n=16)
    town = A.cut("cafes", w=2300)
    hazy = Image.new("RGBA", town.size, (190, 225, 255, 0)); hazy.putalpha(town.split()[3].point(lambda v: int(v * 0.45)))
    town.alpha_composite(hazy)
    img.alpha_composite(town, (-150, 1230 - town.height))
    path = bezier((470, 520), (900, 250), (1500, 520))
    arc(img, path, (255, 255, 255), 90, 170)
    streaks(img, 500, 520, 1250, 420, n=7, spread=130, alpha=130, width=14)
    A.hero(img, A.cut("cannon", 820), 330, 1110, rim=16, tilt=0)
    A.hero(img, A.cut("pl_run", 620), 1050, 975, rim=16, glow=(255, 255, 255), tilt=14)
    A.hero(img, A.cut("cat_Comet", 600), 1580, 910, rim=20, glow=(255, 200, 80), tilt=-16)
    A.sparkles(img, [(1300, 330, 80, (255, 255, 255)), (1850, 300, 70, (255, 240, 160))])
    A.words(img, "BOOM!", 290, 1180, 165, GOLD, -5)
    return img


ALL = {"A": ("CatchIt", catch), "B": ("CatsWork", work), "C": ("Collect", collection), "D": ("Cannon", cannon)}

if __name__ == "__main__":
    pick = sys.argv[1:] or list(ALL)
    for k in pick:
        n, f = ALL[k]
        im = f().convert("RGB")
        im.save(os.path.join(OUT, f"CatCafe_HomeThumb_{k}_{n}_1920x1080.png"))
        print("wrote", k)
