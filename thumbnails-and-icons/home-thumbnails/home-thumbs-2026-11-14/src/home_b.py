"""Home thumbnails, pass B (Derek 18:24 UTC: true to the game, a player and cats in our world). Same big subject and
big title, with the player and a net in a real place from the game. python3 home_b.py"""
import os
from PIL import Image, ImageDraw
import ads as A
from ads import GOLD, WHITE
import home as H
A.W, A.H = 1920, 1080
OUT = H.OUT


def player(img, right, bottom, h=640):
    im = A.cut("pl_net", h, flip=True)
    A.hero(img, im, right - im.width // 2, bottom, rim=12, shadow=True)


def base(sky_in, sky_out, ground, centre=(0.7, 0.5)):
    img = A.bg(sky_in, sky_out, rays=(255, 255, 255), centre=centre, ray_alpha=40)
    A.ground(img, 960, 1150, 1500, 260, ground, 255)
    return img


def behind(img, name, h, cx, bottom):
    g = A.cut(name, h); img.alpha_composite(g, (cx - g.width // 2, bottom - g.height))


def traits():
    img = base((235, 250, 255), (90, 180, 255), (140, 215, 150))
    behind(img, "d_tree", 900, 1500, 960)
    player(img, 1915, 1030)
    A.hero(img, A.cut("t2_neon", 720), 1270, 1075, rim=18, glow=(255, 150, 200), tilt=-3)
    H.title(img, ["CAT", "TRAITS!"], 470, 250, 270)
    return img


def backpack():
    img = base((255, 250, 225), (120, 200, 255), (150, 220, 175))
    behind(img, "cafe_blush", 760, 1380, 930)
    A.hero(img, A.cut("pl_run", 760, flip=True), 1180, 1050, rim=12)
    A.hero(img, A.cut("backpack", 720), 1590, 1075, rim=18, glow=(255, 250, 210), tilt=5)
    H.title(img, ["BACK", "PACK!"], 450, 250, 300, [GOLD, GOLD])
    return img


def worlds():
    img = base((235, 250, 255), (60, 150, 240), (245, 250, 255))
    behind(img, "lm_Snowy_Gate", 880, 1400, 990)
    player(img, 1915, 1030)
    A.hero(img, A.cut("cat_Blizzard", 680), 1270, 1075, rim=18, glow=(220, 245, 255), tilt=-2)
    H.title(img, ["3 NEW", "WORLDS!"], 450, 250, 262)
    return img


def secret():
    img = base((255, 235, 170), (140, 70, 210), (120, 100, 150), centre=(0.5, 0.6))
    behind(img, "lm_Castle_Gate", 760, 960, 960)
    H.glow(img, 760, 760, 520, (255, 240, 190), 120)
    im = A.cut("pl_net", 560, flip=True); A.hero(img, im, 1915 - im.width // 2, 1040, rim=12)
    A.hero(img, A.cut("x_Moonstag", 600), 330, 1078, rim=16, glow=(200, 240, 255), tilt=-3)
    A.hero(img, A.cut("x_Excalipurr", 600, flip=True), 1130, 1078, rim=16, glow=(235, 220, 255), tilt=3)
    A.hero(img, A.cut("x_Phoenix", 680), 730, 1080, rim=18, glow=(255, 235, 150))
    A.words(img, "SECRET CATS!", 250, 960, 150, GOLD, -2)
    return img


def rift():
    img = A.bg((255, 170, 235), (70, 40, 190), rays=(255, 255, 255), centre=(0.72, 0.5), ray_alpha=55)
    sc = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cut", "rift_scene.png")).convert("RGBA")
    k = 1080 / sc.height; sc = sc.resize((int(sc.width * k), 1080), Image.LANCZOS)
    img.alpha_composite(sc, (1920 - sc.width, 0))
    A.hero(img, A.cut("r_ginger_b", 640), 1620, 1075, rim=18, glow=(255, 230, 245), tilt=-5)
    A.hero(img, A.cut("pl_run", 700), 1200, 1050, rim=12)
    H.title(img, ["RACE", "THE RIFT!"], 450, 250, 250)
    return img


if __name__ == "__main__":
    tiles = []
    for i, (n, f) in enumerate((("CatTraits", traits), ("Backpack", backpack), ("3NewWorlds", worlds), ("SecretCats", secret), ("RaceTheRift", rift)), 1):
        im = f().convert("RGB"); im.save(os.path.join(OUT, f"CatCafe_HomeThumb_{i}_{n}_B_1920x1080.png")); tiles.append(im.resize((300, 169), Image.LANCZOS))
    sh = Image.new("RGB", (310 * 3 + 10, 179 * 2 + 10), (24, 24, 30))
    for i, t in enumerate(tiles):
        sh.paste(t, (10 + (i % 3) * 310, 10 + (i // 3) * 179))
    sh.save(os.path.join(OUT, "check_300w_B.png"))
