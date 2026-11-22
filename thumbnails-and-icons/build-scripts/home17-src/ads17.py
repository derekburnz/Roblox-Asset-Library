"""Ad pictures, 2026-11-17 draft (Growth brief 5): six hooks with the coolest Mythic and Secret cats and the bacon,
each square (1080x1080) and tall (1080x1920). Names follow the ad folder plus _v2."""
import os
import sys

from PIL import Image

import ads as A
import home16 as Hm
import kit17 as K
from ads import GOLD

OUT = os.environ["HOME_OUT"]
NET = os.environ.get("BACON_NET", "bacon_a")
JUMP = os.environ.get("BACON_JUMP", "bacon_k")
CHEER = os.environ.get("BACON_CHEER", "bacon_h")
POINT = os.environ.get("BACON_POINT", "bacon_i")
YEL = ((255, 250, 150), (255, 190, 30), (70, 26, 6))
VIO = ((255, 235, 255), (200, 120, 255), (50, 10, 90))


def bacon(name, h, flip=False):
    return K.pop(K.cutp(name, h, flip=flip, folder="."), 1.15, 1.1)


def fit_words(img, text, size, cx, cy, style, tilt=-3):
    """One or two lines (split on |), each as wide as the picture allows."""
    lines = text.split("|")
    for i, ln in enumerate(lines):
        s = min(size, int(img.width * 2.0 / max(4, len(ln))))
        K.word(img, ln, s, cx, cy + int(i * size * 0.95), style, tilt)


def duo(tall, word, style, cat, inner, outer, colours, alpha, catglow, who=None, cat_k=1.0):
    """The net shot: the bacon low on the left reaching the net over one giant cat."""
    W, H = (1080, 1920) if tall else (1080, 1080)
    A.W, A.H = W, H
    img = K.burst((W, H), (0.62, 0.5 if tall else 0.48), inner, outer, n=16, colours=colours, alpha=alpha)
    cy = int(H * (0.5 if tall else 0.5))
    K.glow(img, int(W * 0.62), cy, int(W * 0.48), (255, 255, 255), 220)
    ch = int((1050 if tall else 820) * cat_k)
    A.hero(img, K.pop(K.cutp(cat, ch)), int(W * (0.56 if tall else 0.69)), int(H * (0.74 if tall else 0.96)), rim=18,
           rim_rgb=(255, 255, 255), glow=catglow, tilt=-3)
    name = who or NET
    if name == NET:
        A.hero(img, bacon(name, 1500 if tall else 1350, flip=True), int(W * (0.42 if tall else 0.42)),
               int(H * (1.02 if tall else 1.27)), rim=16, tilt=4)
    else:
        A.hero(img, bacon(name, 1050 if tall else 900), int(W * (0.36 if name == POINT else 0.3)), int(H * (1.08 if tall else 1.36)),
               rim=16, tilt=3)
    A.sparkles(img, [(int(W * 0.9), int(H * 0.3), 120, (255, 255, 255)), (int(W * 0.12), int(H * 0.36), 100, (255, 255, 255)),
                     (int(W * 0.9), int(H * 0.62), 80, (255, 245, 170))])
    fit_words(img, word, 250 if tall else 210, W // 2, int(H * (0.1 if tall else 0.12)), style)
    return img


def cannon(tall):
    W, H = (1080, 1920) if tall else (1080, 1080)
    A.W, A.H = W, H
    img = K.burst((W, H), (0.2, 0.85), (255, 255, 255), (50, 150, 255), n=18, alpha=75)
    y0 = H - 1080 if tall else 0
    Hm.arc(img, Hm.bezier((260, y0 + 620), (520, y0 + 250), (900, y0 + 420)), (255, 255, 255), 100, 180)
    A.hero(img, A.cut("cannon", 760), 250, H + 60, rim=16)
    K.glow(img, 410, y0 + 520, 170, (255, 255, 255), 230)
    A.hero(img, bacon(CHEER, 640), 500, y0 + 950, rim=18, glow=(255, 255, 255), tilt=-18)
    A.hero(img, K.pop(K.cutp("big_DragonKnight", 470)), 850, y0 + 760, rim=18, glow=(255, 200, 80), tilt=-14)
    if tall:
        A.hero(img, K.pop(K.cutp("big_KingCroissant", 520)), 760, 720, rim=18, glow=(255, 200, 80), tilt=10)
    fit_words(img, "RIDE THE|CANNON!", 230 if tall else 190, W // 2, int(H * (0.09 if tall else 0.11)), K.T.GOLD)
    return img


def wall(tall):
    W, H = (1080, 1920) if tall else (1080, 1080)
    A.W, A.H = W, H
    img = K.burst((W, H), (0.5, 0.55), (255, 252, 225), (255, 140, 60), n=18, alpha=70)
    names = ["cat_Neon", "cat_Sphinx", "cat_Blizzard", "cat_DragonKnight", "cat_Wisp", "cat_KingCroissant", "cat_Midnight",
             "cat_Water", "cat_Aurora", "cat_JadeGuardian", "cat_Eclipse", "cat_Balloon"]
    rows = 4 if tall else 2
    per = 3 if tall else 4
    top = int(H * 0.3) if tall else int(H * 0.36)
    step = (H - top) // rows
    k = 0
    for r in range(rows):
        for c in range(per):
            cx = int(W * (c + 0.5) / per)
            A.hero(img, K.pop(K.cutp(names[k % len(names)], int(step * 0.82))), cx, top + (r + 1) * step - 20, rim=12,
                   glow=Hm.RARITY["Mythical"]); k += 1
    K.glow(img, W // 2, int(H * 0.62), 360, (255, 255, 255), 235)
    A.hero(img, K.pop(K.cutp("big_Comet", 760 if tall else 620)), W // 2, int(H * (0.84 if tall else 0.99)), rim=22,
           glow=(255, 70, 150))
    fit_words(img, "CATCH|110+ CATS!", 230 if tall else 190, W // 2, int(H * (0.08 if tall else 0.1)), K.T.GOLD)
    return img


def earn(tall):
    W, H = (1080, 1920) if tall else (1080, 1080)
    A.W, A.H = W, H
    room = A.photo("/mnt/project-files/Model-Agent/store-and-ads/ads-2026-11-08/Ad_05_DecorateCafe_raw.png", 1.6 if tall else 1.3,
                   0.5, 0.45, blur=8)
    img = room.convert("RGBA")
    img.alpha_composite(Image.new("RGBA", img.size, (255, 190, 90, 80)))
    K.glow(img, int(W * 0.6), int(H * 0.6), 560, (255, 245, 200), 180)
    A.hero(img, K.pop(A.cut("work_Ginger", 1000 if tall else 800)), int(W * 0.62), int(H * (0.82 if tall else 1.02)), rim=22,
           glow=(255, 240, 190), tilt=-3)
    A.hero(img, bacon(CHEER, 1000 if tall else 860), int(W * 0.26), int(H * (1.04 if tall else 1.34)), rim=16, tilt=3)
    for (x, y, s) in ((0.2, 0.36, 150), (0.9, 0.34, 150), (0.88, 0.7, 120)):
        K.word(img, "$", s, int(W * x), int(H * y), K.T.MONEY, 8)
    fit_words(img, "CATS EARN|$$$ FOR YOU", 210 if tall else 175, W // 2, int(H * (0.08 if tall else 0.1)), K.T.MONEY)
    return img


ADS = {
    "01_Mythic": lambda t: duo(t, "MYTHIC!", K.T.MYTHIC, "big_Comet", (255, 255, 255), (40, 140, 255), K.RAINBOW, 110, (255, 80, 170)),
    "02_OneIn100": lambda t: duo(t, "1 IN 100!", K.T.SECRET, "big_Neon", (255, 240, 255), (120, 40, 220), [(255, 255, 255)], 70,
                                 (120, 255, 230), who=CHEER),
    "03_SecretCat": lambda t: duo(t, "SECRET|CAT!", K.T.SECRET, "big_Phoenix", (255, 250, 170), (230, 60, 60), [(255, 255, 255)], 80,
                                  (255, 200, 60), who=POINT, cat_k=1.05),
    "04_Cannon": cannon,
    "05_CatchThemAll": wall,
    "06_CatsEarn": earn,
}

if __name__ == "__main__":
    for k in (sys.argv[1:] or list(ADS)):
        for tall in (False, True):
            ADS[k](tall).convert("RGB").save(os.path.join(OUT, f"Ad_{k}_v2_{'1080x1920' if tall else '1080x1080'}.png"))
        print("wrote", k)
