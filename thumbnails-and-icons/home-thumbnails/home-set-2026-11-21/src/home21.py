"""Home thumbnail set, Nov 21 draft (Growth brief 2026-11-20): four 1920x1080 tiles and one draft sheet.
1 page thumb A as is, 2 Gold Dragon Knight at a full bowl with the bacon peeking in, 3 before and after, 4 bacon cheers
a big glowing cat. Real bacon render, one hero, three words or fewer, warm backgrounds, nothing key under y 918.
gold_bowl.png: cut.py render of CatCafe_Cat_DragonKnight_Sit toned by its GoldTone attributes, FoodBowl and Kibble.
python3 home21.py"""
import math, os, sys, random
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(HERE)
sys.path.insert(0, "/mnt/project-files/Design-Agent/home-type-2026-11-17")
import type17 as T
M = "/mnt/project-files/Model-Agent/"
H17 = M + "home-thumbs-2026-11-17/"; H16 = M + "home-thumbs-2026-11-16/src/cut/"
W, H = 1920, 1080


def cut(path, h=None, w=None, flip=False, sat=1.15, con=1.05):
    im = Image.open(path).convert("RGBA"); im = im.crop(im.getbbox())
    if h: im = im.resize((max(1, int(im.width * h / im.height)), h), Image.LANCZOS)
    elif w: im = im.resize((w, max(1, int(im.height * w / im.width))), Image.LANCZOS)
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    a = im.split()[3]; rgb = ImageEnhance.Contrast(ImageEnhance.Color(im.convert("RGB")).enhance(sat)).enhance(con); rgb.putalpha(a)
    return rgb


def burst(centre, inner, outer, n=16, ray=(255, 255, 255), alpha=60, spin=0.0):
    img = Image.new("RGBA", (W, H)); X, Y = centre[0] * W, centre[1] * H
    rad = Image.radial_gradient("L").resize((W * 2, W * 2)); rad = rad.crop((int(W - X), int(W - Y), int(W - X) + W, int(W - Y) + H))
    img = Image.composite(Image.new("RGBA", (W, H), outer + (255,)), Image.new("RGBA", (W, H), inner + (255,)), rad.point(lambda v: min(255, int(v * 1.6))))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); R = 3 * W
    for i in range(n):
        a0 = 2 * math.pi * i / n + spin; a1 = a0 + math.pi / n
        d.polygon([(X, Y), (X + R * math.cos(a0), Y + R * math.sin(a0)), (X + R * math.cos(a1), Y + R * math.sin(a1))], fill=ray + (alpha,))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(2))); return img


def glow(img, cx, cy, r, rgb, a=200):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).ellipse([cx - r, cy - r, cx + r, cy + r], fill=rgb + (a,))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(r // 3)))


def hero(img, im, cx, bottom, rim=14, glow_rgb=None, tilt=0):
    if tilt: im = im.rotate(tilt, resample=Image.BICUBIC, expand=True)
    pad = 120; lay = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0)); lay.alpha_composite(im, (pad, pad))
    a = lay.split()[3]; x, y = int(cx - lay.width / 2), int(bottom - im.height - pad)
    if glow_rgb:
        g = Image.new("RGBA", lay.size, glow_rgb + (0,)); g.putalpha(a.filter(ImageFilter.MaxFilter(41)).filter(ImageFilter.GaussianBlur(38)).point(lambda v: int(v * 0.9)))
        img.alpha_composite(g, (x, y))
    s = Image.new("RGBA", lay.size, (60, 20, 10, 0)); s.putalpha(a.filter(ImageFilter.MaxFilter(rim * 2 + 1)).filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.5)))
    img.alpha_composite(s, (x + 10, y + 18))
    r = Image.new("RGBA", lay.size, (255, 255, 255, 0)); r.putalpha(a.filter(ImageFilter.MaxFilter(rim * 2 + 1)).filter(ImageFilter.GaussianBlur(1.2)))
    img.alpha_composite(r, (x, y)); img.alpha_composite(lay, (x, y))


def sparkle(img, x, y, s, rgb=(255, 255, 255)):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay); k = s * 0.18
    d.polygon([(x, y - s), (x + k, y - k), (x + s, y), (x + k, y + k), (x, y + s), (x - k, y + k), (x - s, y), (x - k, y - k)], fill=rgb + (255,))
    g = lay.filter(ImageFilter.GaussianBlur(s * 0.25)); img.alpha_composite(g); img.alpha_composite(lay)


def coin(img, cx, cy, r, tilt=0.0):
    lay = Image.new("RGBA", (int(r * 2.4), int(r * 2.4)), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); c = r * 1.2
    ry = r * (0.45 + 0.55 * abs(math.cos(tilt)))
    d.ellipse([c - r - 5, c - ry - 5, c + r + 5, c + ry + 5 + r * 0.18], fill=(80, 40, 5, 255))
    d.ellipse([c - r, c - ry + r * 0.16, c + r, c + ry + r * 0.16], fill=(214, 140, 20, 255))
    d.ellipse([c - r, c - ry, c + r, c + ry], fill=(255, 200, 50, 255))
    d.ellipse([c - r * 0.72, c - ry * 0.72, c + r * 0.72, c + ry * 0.72], outline=(225, 150, 20, 255), width=max(3, int(r * 0.09)))
    d.ellipse([c - r * 0.55, c - ry * 0.7, c - r * 0.1, c - ry * 0.35], fill=(255, 245, 190, 200))
    img.alpha_composite(lay, (int(cx - c), int(cy - c)))


def word(img, s, cx, cy, style, max_w, tilt=-3):
    T.word(img, s, int(T.fit(s, max_w, style, start=230) * 1.0), cx, cy, style, tilt)


def tile1():
    return Image.open(M + "page-thumb-2026-11-18/CatCafe_PageThumb_A_OneCatchNet_1920x1080.png").convert("RGBA")


def tile2():
    img = burst((0.62, 0.48), (255, 214, 120), (232, 96, 20), n=18, alpha=55)
    glow(img, 1180, 520, 470, (255, 240, 170), 230)
    for k in range(9):                                        # soft gold rays from behind the cat
        pass
    cat = cut(os.path.join(HERE, "gold_bowl.png"), h=860, sat=1.25, con=1.08)
    hero(img, cat, 1190, 925, rim=16, glow_rgb=(255, 215, 80))
    hero(img, cut(H17 + "bacon-real/real_net.png", h=980, flip=True), 330, 1200, rim=12, tilt=-6)
    for x, y, s in ((1560, 250, 70), (860, 380, 46), (1640, 640, 40), (1500, 820, 30)):
        sparkle(img, x, y, s, (255, 252, 220))
    word(img, "GOLD CAT!", 600, 170, T.GOLD, 900)
    return img


def tile3():
    left = burst((0.25, 0.55), (205, 225, 240), (110, 140, 175), n=14, alpha=40)
    right = burst((0.74, 0.5), (255, 236, 150), (240, 110, 25), n=16, alpha=70)
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).polygon([(1010, 0), (W, 0), (W, H), (850, H)], fill=255)
    img = left.copy(); img.paste(right, (0, 0), m)
    ImageDraw.Draw(img).line([(1010, 0), (850, H)], fill=(255, 255, 255, 255), width=18)
    hero(img, cut(H17 + "cozy/cafe_mint.png", w=600, sat=0.75), 450, 820, rim=12)
    glow(img, 1420, 520, 420, (255, 250, 200), 200)
    hero(img, cut(H17 + "cozy/cafe.png", w=820), 1440, 700, rim=14)
    cats = (("cat_Calico", 1090, 905, 250), ("cat_Duckling", 1270, 900, 240), ("cat_Taxi", 1630, 895, 250),
            ("cat_Tortie", 1810, 905, 240))
    for n, x, y, h in cats:
        hero(img, cut(H16 + n + ".png", h=h), x, y, rim=10)
    hero(img, cut(H16 + "cat_Balloon.png", h=330), 1450, 915, rim=12, glow_rgb=(255, 170, 210))
    rnd = random.Random(4)
    for x, y, r in ((1180, 640, 34), (1700, 600, 30), (1330, 560, 26), (1560, 520, 24), (1760, 760, 28), (1110, 780, 26)):
        coin(img, x, y, r, rnd.uniform(0, 1.2))
    for x, y, s in ((1840, 300, 60), (1150, 330, 44)):
        sparkle(img, x, y, s)
    ar = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ad = ImageDraw.Draw(ar)
    for wd, col in ((50, (70, 10, 10, 255)), (30, (240, 40, 50, 255))):
        ad.arc([620, 330, 1120, 700], 200, 330, fill=col, width=wd)
    ad.polygon([(1060, 330), (1175, 410), (1030, 455)], fill=(70, 10, 10, 255)); ad.polygon([(1068, 352), (1145, 408), (1046, 437)], fill=(240, 40, 50, 255))
    img.alpha_composite(ar)
    word(img, "BEFORE", 430, 170, T.WHITE, 620, tilt=-2)
    word(img, "AFTER!", 1440, 160, T.GOLD, 700, tilt=-3)
    return img


def tile4():
    img = burst((0.62, 0.5), (255, 190, 220), (240, 70, 120), n=18, ray=(255, 230, 120), alpha=70, spin=0.1)
    glow(img, 1240, 520, 480, (255, 245, 200), 230)
    hero(img, cut(H17 + "cut17/big_Excalipurr.png", h=820, sat=1.2), 1260, 905, rim=18, glow_rgb=(255, 230, 120), tilt=-4)
    hero(img, cut(H17 + "bacon-real/real_cheer.png", h=900), 430, 1150, rim=12, tilt=4)
    for x, y, s in ((1700, 230, 80), (870, 560, 50), (1720, 700, 44), (1620, 880, 30)):
        sparkle(img, x, y, s)
    word(img, "I GOT IT!", 620, 160, T.GOLD, 860, tilt=-4)
    return img


def sheet(tiles, names):
    pad = 24; tw, th = 900, 506
    sh = Image.new("RGB", (pad + 2 * (tw + pad), 80 + 2 * (th + 60 + 190) + pad), (30, 28, 36)); d = ImageDraw.Draw(sh)
    f = ImageFont.truetype(T.FONT, 34); fs = ImageFont.truetype("/mnt/project-files/Model-Agent/store-and-ads/update-2026-11-12/fonts/LilitaOne-Regular.ttf", 24)
    d.text((pad, 20), "Home set draft, Nov 21: nothing uploads before Derek's OK", font=f, fill=(255, 240, 200))
    for i, (t, n) in enumerate(zip(tiles, names)):
        x = pad + (i % 2) * (tw + pad); y = 80 + (i // 2) * (th + 60 + 190)
        sh.paste(t.convert("RGB").resize((tw, th), Image.LANCZOS), (x, y))
        d.text((x, y + th + 8), n, font=fs, fill=(230, 230, 240))
        sh.paste(t.convert("RGB").resize((300, 169), Image.LANCZOS), (x, y + th + 44))
        sh.paste(t.convert("RGB").resize((150, 84), Image.LANCZOS), (x + 320, y + th + 44))
    return sh


if __name__ == "__main__":
    names = ["1 One cat mid-catch (page thumb A)", "2 Gold Mythical at the bowl", "3 Before and after", "4 Bacon cheers a big cat"]
    files = ["CatCafe_Home21_1_OneCatchNet", "CatCafe_Home21_2_GoldCatBowl", "CatCafe_Home21_3_BeforeAfter", "CatCafe_Home21_4_IGotIt"]
    tiles = [tile1(), tile2(), tile3(), tile4()]
    for t, n in zip(tiles, files):
        t.convert("RGB").save(os.path.join(OUT, n + "_1920x1080.png"))
    sheet(tiles, names).save(os.path.join(OUT, "DRAFT_SHEET_home_set_2026-11-21.png"))
    print("ok")
