"""Game icon variants, 2026-11-17 draft (Derek 2026-11-16: look at the trending icons, make ours stand up to them).
V1 a giant Mythic head with the bacon and net, V2 a giant Secret head in colour, V3 the bacon big with the net."""
import os, sys
from PIL import Image, ImageDraw
import ads as A
import kit17 as K

OUT = os.environ["HOME_OUT"]
BACON = os.environ.get("BACON_NET", "bacon_a")       # the bacon holding the net, net to the picture's left
YEL = ((255, 250, 150), (255, 190, 30), (70, 26, 6))
STYLE = {"SECRET!": K.T.SECRET, "MYTHIC!": K.T.MYTHIC}
BUST = os.environ.get("BACON_BUST", "bacon_j")      # the bacon from the front, for the corner bust


def bacon(h, flip=False, name=None):
    return K.pop(K.cutp(name or BACON, h, flip=flip, folder="."), 1.15, 1.1)


def scene(cat, word, inner, outer, catglow, cat_h=1010, cat_cx=700, cat_top=70, net_at=(850, 70), style=None, word_k=0.88, bust_h=560, bust_at=(225, 1075), word_at=(530, 870)):
    img = K.burst((1024, 1024), (0.62, 0.42), inner, outer, n=16, colours=[(255, 255, 255)], alpha=75)
    K.glow(img, cat_cx, 470, 430, (255, 255, 255), 215)
    A.hero(img, K.pop(K.cutp(cat, cat_h)), cat_cx, cat_top + cat_h, rim=16, rim_rgb=K.INK, glow=catglow)
    net = K.pop(A.cut("net1", 300)).rotate(-24, resample=Image.BICUBIC, expand=True)      # the hoop, about to drop
    A.hero(img, net, net_at[0], net_at[1] + net.height, rim=10, rim_rgb=K.INK, shadow=False)
    A.hero(img, bacon(bust_h, name=BUST), bust_at[0], bust_at[1], rim=14, rim_rgb=K.INK, tilt=-5)          # the grinning bust
    A.sparkles(img, [(930, 520, 110, (255, 255, 255))])
    st = style or K.T.GOLD
    K.T.word(img, word, min(235, K.T.fit(word, int(word_k * 1024), st)), word_at[0], word_at[1], st, -3)
    return img.convert("RGB")


def v1(word="CATCH!"):
    return scene("big_Balloon", word, (170, 240, 255), (20, 120, 250), (255, 120, 200))


def v2(word="SECRET!"):
    return scene("big_Nebula", word, (255, 250, 160), (255, 140, 20), (190, 110, 255), style=K.T.SECRET)


def v3(word="CATCH!"):
    return scene("big_Comet", word, (255, 250, 160), (255, 130, 20), (255, 90, 170))


def v4(word="CATCH!"):
    return scene("big_Excalipurr", word, (200, 250, 255), (40, 110, 240), (255, 220, 90))


ALT = dict(word_k=0.68, bust_h=760, bust_at=(270, 1130), word_at=(620, 900))


def v2b(word="SECRET!"):
    return scene("big_Nebula", word, (255, 250, 160), (255, 140, 20), (190, 110, 255), style=K.T.SECRET, **ALT)


def v3b(word="CATCH!"):
    return scene("big_Comet", word, (255, 250, 160), (255, 130, 20), (255, 90, 170), **ALT)


VARS = {"V2b_SecretOrange_BigBacon": v2b, "V3b_MythicOrange_BigBacon": v3b} if os.environ.get("ICON_ALT") else {"V1_MythicBlue": v1, "V2_SecretOrange": v2, "V3_MythicOrange": v3, "V4_Excalipurr": v4}


def tile(im, s):
    t = im.resize((s, s), Image.LANCZOS)
    m = Image.new("L", (s, s), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, s - 1, s - 1], s // 8, fill=255)
    return t, m


if __name__ == "__main__":
    made = {}
    for k, f in VARS.items():
        im = f(); made[k] = im
        im.save(os.path.join(OUT, f"CatCafe_GameIcon_{k}_1024.png"))
        im.resize((512, 512), Image.LANCZOS).save(os.path.join(OUT, f"CatCafe_GameIcon_{k}_512.png"))
    cur = Image.open(sys.argv[1]).convert("RGB")
    trend = [Image.open(os.path.join(K.HERE, "trend", f"t{i}.png")).convert("RGB") for i in range(8)]
    row = [("now", cur)] + list(made.items())
    sh = Image.new("RGB", (1500, 430), (17, 18, 22))
    d = ImageDraw.Draw(sh)
    for size, y in ((128, 20), (100, 170), (50, 290)):
        x = 20
        for i, t in enumerate(trend[:4]):
            a, m = tile(t, size); sh.paste(a, (x, y), m); x += size + 14
        for name, im in row:
            a, m = tile(im, size); sh.paste(a, (x, y), m)
            if size == 128:
                d.text((x + 4, y + 132), name, fill=(230, 230, 230))
            x += size + 14
        for t in trend[4:]:
            a, m = tile(t, size); sh.paste(a, (x, y), m); x += size + 14
    sh.save(os.path.join(OUT, "icon_compare_trending.png"))
