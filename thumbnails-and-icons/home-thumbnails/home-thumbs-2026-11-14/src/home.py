"""Home page thumbnails that read on a phone (Derek 2026-11-14 18:22 UTC via Growth-Agent): one huge subject, a 2 to 4
word title in very large letters, plain bright background, almost no small detail. 1920x1080. python3 home.py"""
import os
from PIL import Image, ImageDraw, ImageFilter
import ads as A
from ads import GOLD, WHITE
A.W, A.H = 1920, 1080
OUT = os.environ.get("HOME_OUT", "/mnt/project-files/Model-Agent/home-thumbs-2026-11-14")
os.makedirs(OUT, exist_ok=True)


def glow(img, cx, cy, r, rgb, a=170):
    g = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(g).ellipse([cx - r, cy - r, cx + r, cy + r], fill=rgb + (a,))
    img.alpha_composite(g.filter(ImageFilter.GaussianBlur(r // 3)))


def title(img, lines, cx, top, size, styles=None, tilt=-3):
    for i, t in enumerate(lines):
        A.words(img, t, size, cx, top + int(size * 0.5) + int(i * size * 0.98), (styles or [WHITE, GOLD, GOLD])[i], tilt)


def traits():
    img = A.bg((255, 215, 240), (190, 70, 220), rays=(255, 255, 255), centre=(0.72, 0.55), ray_alpha=55)
    glow(img, 1400, 600, 480, (255, 255, 255), 120)
    A.hero(img, A.cut("t2_neon", 1040), 1400, 1075, rim=22, glow=(255, 150, 200), tilt=-3)
    title(img, ["CAT", "TRAITS!"], 520, 250, 300)
    return img


def backpack():
    img = A.bg((255, 250, 200), (255, 140, 60), rays=(255, 255, 255), centre=(0.72, 0.55), ray_alpha=60)
    glow(img, 1420, 600, 480, (255, 255, 255), 120)
    A.hero(img, A.cut("backpack", 960), 1420, 1050, rim=22, glow=(255, 250, 210), tilt=6)
    title(img, ["BACK", "PACK!"], 500, 250, 320, [GOLD, GOLD])
    return img


def worlds():
    img = A.bg((235, 250, 255), (60, 150, 240), rays=(255, 255, 255), centre=(0.7, 0.5), ray_alpha=55)
    A.ground(img, 960, 1120, 1400, 200, (245, 250, 255), 255)
    g = A.cut("lm_Snowy_Gate", 900)
    img.alpha_composite(g, (1380 - g.width // 2, 990 - g.height))
    A.hero(img, A.cut("cat_Blizzard", 780), 1380, 1075, rim=22, glow=(220, 245, 255), tilt=-2)
    title(img, ["3 NEW", "WORLDS!"], 520, 250, 290)
    return img


def secret():
    img = A.bg((255, 225, 150), (120, 50, 200), rays=(255, 250, 220), centre=(0.5, 0.62), ray_alpha=55)
    glow(img, 960, 700, 560, (255, 240, 190), 140)
    A.hero(img, A.cut("x_Moonstag", 760), 400, 1078, rim=18, glow=(200, 240, 255), tilt=-3)
    A.hero(img, A.cut("x_Excalipurr", 760, flip=True), 1520, 1078, rim=18, glow=(235, 220, 255), tilt=3)
    A.hero(img, A.cut("x_Phoenix", 840), 960, 1080, rim=22, glow=(255, 235, 150))
    A.words(img, "SECRET CATS!", 262, 960, 150, GOLD, -2)
    return img


def rift():
    img = A.bg((255, 170, 235), (70, 40, 190), rays=(255, 255, 255), centre=(0.72, 0.5), ray_alpha=55)
    for r, c in ((500, (255, 255, 255)), (400, (255, 120, 210)), (290, (255, 215, 245)), (180, (255, 255, 255))):
        d = ImageDraw.Draw(img); d.ellipse([1420 - r, 520 - r, 1420 + r, 520 + r], fill=c + (255,))
    A.hero(img, A.cut("r_ginger_b", 900), 1400, 1075, rim=22, glow=(255, 230, 245), tilt=-5)
    title(img, ["RACE", "THE RIFT!"], 500, 250, 270)
    return img


if __name__ == "__main__":
    tiles = []
    for i, (n, f) in enumerate((("CatTraits", traits), ("Backpack", backpack), ("3NewWorlds", worlds), ("SecretCats", secret), ("RaceTheRift", rift)), 1):
        im = f().convert("RGB"); im.save(os.path.join(OUT, f"CatCafe_HomeThumb_{i}_{n}_1920x1080.png")); tiles.append(im.resize((300, 169), Image.LANCZOS))
    sh = Image.new("RGB", (310 * 3 + 10, 179 * 2 + 10), (24, 24, 30))
    for i, t in enumerate(tiles):
        sh.paste(t, (10 + (i % 3) * 310, 10 + (i // 3) * 179))
    sh.save(os.path.join(OUT, "check_300w.png"))
