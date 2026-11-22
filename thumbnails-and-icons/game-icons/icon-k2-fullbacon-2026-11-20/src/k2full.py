"""K2 icon with the whole bacon in frame (Derek 2026-11-20 12:50 UTC: "the new icon has the bacons characters legs cut
off fix that"). Same orange burst and big Excalipurr face as K2, the real bacon full body on the left, head to shoes,
pointing at the cat. Also the 1H and NOW chips (device-improvements small.py).   python3 k2full.py [pose]"""
import os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
sys.path.insert(0, "/mnt/project-files/Model-Agent/home-set-2026-11-21/src")
sys.path.insert(0, "/mnt/project-files/Model-Agent/device-improvements-2026-11-21/src")
import home21 as H
from small import chip
H.W = H.H = S = 1024
C = "/mnt/project-files/Model-Agent/home-thumbs-2026-11-17/"
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INK = (50, 20, 10)


def hero(img, im, cx, bottom, rim):
    pad = 60; lay = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0)); lay.alpha_composite(im, (pad, pad))
    a = lay.split()[3]; x, y = int(cx - lay.width / 2), int(bottom - im.height - pad)
    r = Image.new("RGBA", lay.size, INK + (0,)); r.putalpha(a.filter(ImageFilter.MaxFilter(rim * 2 + 1)).filter(ImageFilter.GaussianBlur(1.0)))
    img.alpha_composite(r, (x, y)); img.alpha_composite(lay, (x, y))


BGS = {"orange": ((255, 250, 170), (255, 120, 15)), "blue": ((200, 240, 255), (25, 95, 235)), "pink": ((255, 220, 240), (240, 60, 140)),
       "purple": ((240, 220, 255), (130, 60, 230))}


def k2(pose, cat="Excalipurr", bgname="orange"):
    img = H.burst((0.5, 0.42), *BGS[bgname], n=16, alpha=70)
    H.glow(img, 512, 470, 430, (255, 255, 255), 190)
    b = H.cut(C + "bacon-real/" + pose + ".png", h=580, flip=False, sat=1.15, con=1.1)
    hero(img, b, BX, 985, 12)
    c = Image.open(C + f"cut17/big_{cat}.png").convert("RGBA"); c = c.crop(c.getbbox()); c = c.crop((0, 0, c.width, int(c.height * 0.97)))
    c = H.cut.__wrapped__(c) if hasattr(H.cut, "__wrapped__") else c
    c = c.resize((CW, int(c.height * CW / c.width)), Image.LANCZOS)
    a = c.split()[3]; rgb = ImageEnhance.Contrast(ImageEnhance.Color(c.convert("RGB")).enhance(1.2)).enhance(1.08); rgb.putalpha(a)
    hero(img, rgb, CX, S + CB, 18)
    H.sparkle(img, *SP, 90)
    return img


pose = "real_cheer"
BX = 300
CAT = sys.argv[1] if len(sys.argv) > 1 else "Excalipurr"
BG = sys.argv[2] if len(sys.argv) > 2 else "orange"
TAG = sys.argv[3] if len(sys.argv) > 3 else "K2b"
CW = int(sys.argv[4]) if len(sys.argv) > 4 else 700
CX = int(sys.argv[5]) if len(sys.argv) > 5 else 660
CB = int(sys.argv[6]) if len(sys.argv) > 6 else 60
SP = (130, 150) if CAT == "Moonstag" else (930, 150)
base = k2(pose, CAT, BG)
for tag, label in (("Plain", None), ("1H", "1H"), ("Now", "NOW!")):
    im = base.copy()
    if label:
        ch = chip(label); im.alpha_composite(ch, (S - ch.width - 6, 20))
    im = im.convert("RGB"); n = f"CatCafe_GameIcon_{TAG}_{tag}"
    im.save(os.path.join(OUT, n + "_1024.png")); im.resize((512, 512), Image.LANCZOS).save(os.path.join(OUT, n + "_512.png"))
print("ok")
