"""Game page "what you do" thumbnails for #5285 (Growth ask 2026-11-18): one simple idea each, the cosy cafe
behind, CATCH CUTE CATS in the in-game menu look (Fredoka One, cream letters, cocoa ink).
A: one cute cat mid-catch with the net.  B: the cafe full of cats.   python3 thumb18.py [A B]"""
import os
import sys

from PIL import Image, ImageEnhance, ImageFilter

import ads as A
import home16 as Hm
import kit17 as K

W, H = 1920, 1080
A.W, A.H = W, H
OUT = os.environ["THUMB_OUT"]
FONT = os.environ["MENU_FONT"]
ROOM = "/mnt/project-files/Model-Agent/store-and-ads/ads-2026-11-08/Ad_05_DecorateCafe_raw.png"
# Theme.colors cream F6EBDD to a warm latte, cocoaDeep 3A2E2A ink: the menu title look
MENU = ((255, 250, 240), (246, 222, 190), (58, 46, 42))


def room(zoom, cx, cy, blur, bright=1.0):
    img = A.photo(ROOM, zoom, cx, cy, blur=blur).convert("RGBA")
    img = ImageEnhance.Brightness(img).enhance(bright)
    img.alpha_composite(Image.new("RGBA", img.size, (255, 200, 140, 40)))
    return img


def title(img, cy=150, max_w=1640):
    size = K.T.fit("CATCH CUTE CATS", max_w, MENU, start=230, font=FONT)
    K.T.word(img, "CATCH CUTE CATS", size, W // 2, cy, MENU, -2, font=FONT)


def bacon(name, h, flip=False):
    return K.pop(K.cutp(name, h, flip=flip, folder="bacon-real"), 1.1, 1.05)


def take_a():
    img = ImageEnhance.Color(room(1.25, 0.5, 0.62, blur=12, bright=0.98)).enhance(1.25)
    K.vignette(img, 70, (90, 50, 30))
    K.glow(img, 1180, 640, 430, (255, 248, 230), 200)
    Hm.streaks(img, 1000, 600, 1090, 620, n=5, spread=180, alpha=120)
    cat = K.pop(K.cutp("jump_Balloon", 640, folder="cut"), 1.2, 1.06)
    A.hero(img, cat, 1240, 1000, rim=18, rim_rgb=(255, 255, 255), glow=(255, 150, 200), tilt=-8)
    A.hero(img, bacon("real_net", 1200, flip=True), 650, 1480, rim=14, tilt=2)
    A.sparkles(img, [(1600, 330, 80, (255, 255, 255))])
    title(img)
    return img


def take_b():
    img = room(1.05, 0.5, 0.55, blur=5, bright=1.0)
    K.vignette(img, 60, (90, 50, 30))
    back = [("cat_Calico", 250, 700, 300), ("cat_Duckling", 620, 690, 290), ("cat_Taxi", 1310, 690, 300),
            ("cat_Tortie", 1680, 700, 300)]
    mid = [("cat_Blossom", 150, 900, 380), ("cat_Tabby", 520, 930, 380), ("cat_Neon", 1420, 930, 380),
           ("cat_Comet", 1780, 910, 370)]
    for name, cx, bottom, h in back:
        A.hero(img, K.pop(K.cutp(name, h, folder="cut")), cx, bottom, rim=10)
    for name, cx, bottom, h in mid:
        A.hero(img, K.pop(K.cutp(name, h, folder="cut")), cx, bottom, rim=12)
    K.glow(img, 960, 640, 360, (255, 248, 230), 190)
    A.hero(img, K.pop(K.cutp("cat_Balloon", 640, folder="cut"), 1.2, 1.06), 960, 1050, rim=18,
           glow=(255, 150, 200), tilt=-3)
    A.sparkles(img, [(1200, 360, 80, (255, 255, 255))])
    title(img)
    return img


ALL = {"A": ("OneCatchNet", take_a), "B": ("CafeFullOfCats", take_b)}

if __name__ == "__main__":
    for k in (sys.argv[1:] or list(ALL)):
        n, f = ALL[k]
        f().convert("RGB").save(os.path.join(OUT, f"CatCafe_PageThumb_{k}_{n}_1920x1080.png"))
        print("wrote", k)
