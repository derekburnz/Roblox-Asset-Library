"""Game icon options K1 to K3, 2026-11-17 (Growth: Home tile about 1 click per 200 views against about 1 in 50 for the
genre middle). The live icon J1 puts the bacon's face first and the cat small and low. These put ONE big cat face
first: eyes at about 40% height, the head fills most of the tile, legs run off the foot, so it reads at 50 px.
Nothing uploaded. Run: HOME_OUT=<out> CUTS=<home-thumbs-2026-11-17> TYPE17=<this src> EV_FONTS=<update-2026-11-12/fonts>
FA_EV=<update-2026-11-12> python3 icon20.py"""
import os

from PIL import Image

import ads as A
import kit17 as K

OUT = os.environ["HOME_OUT"]
CUTS = os.environ["CUTS"]
S = 1024
WHITE = (255, 255, 255)


def head(name, keep):
    """The front-on hero cut-out, cropped to its top `keep` part (the head and a little body)."""
    im = Image.open(os.path.join(CUTS, "cut17", f"big_{name}.png")).convert("RGBA")
    im = im.crop(im.getbbox())
    im = im.crop((0, 0, im.width, int(im.height * keep)))
    return K.pop(im, 1.2, 1.08)


def fitw(im, w):
    return im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)


def bg(inner, outer):
    img = K.burst((S, S), (0.5, 0.42), inner, outer, n=16, colours=[WHITE], alpha=70)
    K.glow(img, 512, 470, 430, WHITE, 190)
    return img


def k1():
    """King Croissant's face, nothing else: orange cat on blue."""
    img = bg((200, 240, 255), (25, 95, 235))
    c = fitw(head("KingCroissant", 0.78), 860)
    A.hero(img, c, 520, S + 30, rim=18, rim_rgb=K.INK, shadow=False)
    A.sparkles(img, [(905, 170, 110, WHITE), (110, 300, 70, WHITE)])
    return img


def k2():
    """Excalipurr's face big in front, the real bacon peeking from behind on the left: both faces read."""
    img = bg((255, 250, 170), (255, 120, 15))
    b = Image.open(os.path.join(CUTS, "bacon-real", "real_bust.png")).convert("RGBA")
    b = K.pop(b.crop(b.getbbox()), 1.15, 1.1)
    b = b.resize((int(b.width * 760 / b.height), 760), Image.LANCZOS)
    A.hero(img, b, 225, 760, rim=14, rim_rgb=K.INK, shadow=False)
    c = fitw(head("Excalipurr", 0.97), 800)
    A.hero(img, c, 680, S + 60, rim=18, rim_rgb=K.INK, shadow=False)
    A.sparkles(img, [(930, 150, 100, WHITE)])
    return img


def k3():
    """Balloon Cat's face with one word on top, for a word-versus-no-word test against K1."""
    img = bg((215, 255, 245), (10, 165, 170))
    c = fitw(head("Balloon", 0.80), 720)
    A.hero(img, c, 512, S + 40, rim=18, rim_rgb=K.INK, shadow=False)
    K.word(img, "CATCH!", 200, 512, 150, tilt=-4)
    A.sparkles(img, [(905, 330, 80, WHITE)])
    return img


VARS = {"K1_FaceKingCroissant_Blue": k1, "K2_FaceExcalipurr_Bacon_Orange": k2, "K3_FaceBalloon_Catch_Teal": k3}

if __name__ == "__main__":
    ims = {}
    for name, f in VARS.items():
        im = f().convert("RGB")
        ims[name] = im
        im.save(os.path.join(OUT, f"CatCafe_GameIcon_{name}_1024.png"))
        im.resize((512, 512), Image.LANCZOS).save(os.path.join(OUT, f"CatCafe_GameIcon_{name}_512.png"))
    # The sheet: the live icon J1 first, then K1 to K3, each at full size and at 150, 100 and 50 px on Home's dark grey.
    live = Image.open(os.path.join(CUTS, "drafts", "CatCafe_GameIcon_J1_HoldExcalipurr_Blue_1024.png")).convert("RGB")
    row = [("LIVE J1", live)] + [(n.split("_")[0], im) for n, im in ims.items()]
    T = 480
    sheet = Image.new("RGB", (len(row) * (T + 30) + 30, T + 260), (25, 27, 31))
    for i, (_, im) in enumerate(row):
        x = 30 + i * (T + 30)
        sheet.paste(im.resize((T, T), Image.LANCZOS), (x, 30))
        xx = x
        for s in (150, 100, 50):
            sheet.paste(im.resize((s, s), Image.LANCZOS), (xx, T + 60))
            xx += s + 20
    sheet.save(os.path.join(OUT, "SHEET_icon_options_K1_K3_vs_live.jpg"), quality=90)
