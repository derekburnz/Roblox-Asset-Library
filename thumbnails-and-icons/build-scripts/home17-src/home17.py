"""Home thumbnails, 2026-11-17 draft: the Nov 16 set reworked from Derek's bacon examples and the Top Trending page
(Growth brief 5): subject fills the frame, glossy cats, the bacon big, one chunky word. E (Back Pack) stays as it is."""
import os
import sys

from PIL import Image

import ads as A
import home16 as Hm
import kit17 as K
from ads import GOLD

W, H = 1920, 1080
OUT = os.environ["HOME_OUT"]
NET = os.environ.get("BACON_NET", "bacon_a")
JUMP = os.environ.get("BACON_JUMP", "bacon_k")
CHEER = os.environ.get("BACON_CHEER", "bacon_h")
POINT = os.environ.get("BACON_POINT", "bacon_i")


def bacon(name, h, flip=False):
    return K.pop(K.cutp(name, h, flip=flip, folder="."), 1.15, 1.1)


def size():
    A.W, A.H = W, H


def catch():
    size()
    img = K.burst((W, H), (0.7, 0.5), (255, 255, 255), (40, 140, 255), n=18, colours=K.RAINBOW, alpha=110)
    K.glow(img, 1340, 560, 620, (255, 255, 255), 220)
    Hm.streaks(img, 420, 760, 1050, 560, n=8, spread=260, alpha=150)
    A.hero(img, K.pop(K.cutp("big_Balloon", 1010)), 1450, 1090, rim=24, rim_rgb=(255, 255, 255), glow=(255, 80, 170), tilt=-5)
    A.hero(img, bacon(NET, 1500, flip=True), 470, 1500, rim=16, tilt=2)
    A.sparkles(img, [(1830, 330, 100, (255, 255, 255)), (1090, 930, 70, (255, 240, 160)), (1840, 800, 70, (255, 240, 160))])
    K.word(img, "MYTHIC!", 270, 500, 170, K.T.MYTHIC, -4)
    return img


def work():
    size()
    room = A.photo("/mnt/project-files/Model-Agent/store-and-ads/ads-2026-11-08/Ad_05_DecorateCafe_raw.png", 1.3, 0.5, 0.45, blur=8)
    img = room.convert("RGBA")
    img.alpha_composite(Image.new("RGBA", img.size, (255, 190, 90, 80)))
    ray = K.burst((W, H), (0.62, 0.55), (255, 240, 150), (255, 170, 40), n=18, alpha=90)
    ray.putalpha(150)
    img.alpha_composite(ray)
    K.glow(img, 1180, 620, 620, (255, 250, 210), 190)
    for name, cx, h in (("work_Tabby", 1720, 520), ("work_Tuxedo", 760, 500)):
        A.hero(img, K.pop(A.cut(name, h)), cx, 930, rim=14, glow=(255, 240, 190))
    A.hero(img, K.pop(A.cut("work_Ginger", 900)), 1250, 1100, rim=22, glow=(255, 240, 190), tilt=-3)
    A.hero(img, bacon(CHEER, 1150), 360, 1420, rim=16, tilt=3)
    for (x, y, s) in ((760, 400, 150), (1740, 330, 150)):
        K.word(img, "$", s, x, y, K.T.MONEY, (x % 30) - 15)
    K.word(img, "CATS WORK!", 250, 1040, 170, K.T.MONEY, -3)
    return img


def collection():
    size()
    img = K.burst((W, H), (0.5, 0.55), (255, 252, 225), (255, 150, 60), n=18, alpha=70)
    back = [("cat_Neon", 300), ("cat_Sphinx", 610), ("cat_Blizzard", 1310), ("cat_DragonKnight", 1620)]
    for name, cx in back:
                A.hero(img, K.pop(K.cutp(name, 400)), cx, 720, rim=14)
    front = [("cat_KingCroissant", 590, "Mythical"), ("cat_Midnight", 1340, "Mythical"),
             ("cat_Water", 1680, "Mythical")]
    for name, cx, rar in front:
        A.hero(img, K.pop(K.cutp(name, 430)), cx, 1010, rim=14)
    A.hero(img, bacon(os.environ.get("BACON_BUST", "bacon_j"), 500), 250, 1110, rim=14, tilt=-4)
    K.glow(img, 960, 600, 430, (255, 255, 255), 230)
    A.hero(img, K.pop(K.cutp("big_Comet", 860)), 960, 1070, rim=24, glow=(255, 70, 150), tilt=-2)
    A.sparkles(img, [(640, 420, 90, (255, 255, 255)), (1290, 400, 90, (255, 255, 255))])
    K.word(img, "100+ CATS!", 260, 960, 150, K.T.GOLD, -2)
    return img


def cannon():
    size()
    img = K.burst((W, H), (0.2, 0.9), (255, 255, 255), (50, 150, 255), n=18, alpha=75)
    town = A.cut("cafes", w=2300)
    hazy = Image.new("RGBA", town.size, (190, 225, 255, 0)); hazy.putalpha(town.split()[3].point(lambda v: int(v * 0.45)))
    town.alpha_composite(hazy)
    img.alpha_composite(town, (-150, 1260 - town.height))
    Hm.arc(img, Hm.bezier((430, 560), (900, 240), (1560, 520)), (255, 255, 255), 110, 180)
    Hm.streaks(img, 460, 560, 1150, 430, n=8, spread=170, alpha=140, width=16)
    A.hero(img, A.cut("cannon", 820), 300, 1150, rim=16, tilt=0)
    K.glow(img, 520, 520, 190, (255, 255, 255), 230)                       # the puff at the muzzle
    A.hero(img, bacon(CHEER, 800), 1040, 1040, rim=18, glow=(255, 255, 255), tilt=-18)
    A.hero(img, K.pop(K.cutp("big_DragonKnight", 640)), 1620, 760, rim=20, glow=(255, 200, 80), tilt=-14)
    A.sparkles(img, [(1320, 300, 90, (255, 255, 255)), (1850, 290, 80, (255, 240, 160))])
    K.word(img, "BOOM!", 280, 540, 165, K.T.GOLD, -5)
    return img


ALL = {"A": ("CatchIt", catch), "B": ("CatsWork", work), "C": ("Collect", collection), "D": ("Cannon", cannon)}

if __name__ == "__main__":
    for k in (sys.argv[1:] or list(ALL)):
        n, f = ALL[k]
        f().convert("RGB").save(os.path.join(OUT, f"CatCafe_HomeThumb_{k}_{n}_1920x1080.png"))
        print("wrote", k)
