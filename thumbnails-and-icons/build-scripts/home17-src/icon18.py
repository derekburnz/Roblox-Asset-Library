"""Game icon, 2026-11-16 20:07 UTC (Derek: "do a bacon holding a cat for the icon"): the real bacon, big and happy, holding a
cute Mythic or Secret cat close to the camera. No word, so it reads at 50 px. Layers: bacon, cat, then the bacon's arms."""
import os
import sys
from PIL import Image, ImageDraw
import ads as A
import kit17 as K
OUT = os.environ["HOME_OUT"]
HERE = os.path.dirname(os.path.abspath(__file__))


def scene(cat, inner, outer, catglow, cat_h=560, word=None, style=None):
    S = 1024
    img = K.burst((S, S), (0.5, 0.45), inner, outer, n=16, colours=[(255, 255, 255)], alpha=75)
    K.glow(img, 512, 520, 470, (255, 255, 255), 200)
    body = Image.open(os.path.join(HERE, "real_hold.png")).convert("RGBA")
    arms = Image.open(os.path.join(HERE, "real_hold_arms.png")).convert("RGBA")
    box = body.getbbox(); k = 1180 / (box[3] - box[1])
    def lay(im):
        im = K.pop(im.crop(box), 1.15, 1.1)
        return im.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS)
    b, a = lay(body), lay(arms)
    x0, y0 = 512 - b.width // 2, 40
    # ink rim behind the bacon
    A.hero(img, b, 512, y0 + b.height, rim=16, rim_rgb=K.INK, shadow=False)
    c = K.pop(K.cutp(cat, cat_h))
    A.hero(img, c, 512, 1010, rim=14, rim_rgb=K.INK, glow=catglow, shadow=False)
    img.alpha_composite(a, (x0, y0))
    A.sparkles(img, [(880, 250, 120, (255, 255, 255)), (140, 420, 80, (255, 255, 255))])
    if word:
        st = style or K.T.GOLD
        K.T.word(img, word, min(190, K.T.fit(word, int(0.7 * S), st)), 512, 930, st, -3)
    return img.convert("RGB")


VARS = {
    "H1_HoldMythic_Orange": lambda: scene("cat_Comet", (255, 250, 160), (255, 130, 20), (255, 90, 170)),
    "H2_HoldSecret_Blue": lambda: scene("big_Excalipurr", (200, 250, 255), (30, 110, 245), (255, 220, 90)),
    "H3_HoldMythic_Blue": lambda: scene("cat_Balloon", (190, 245, 255), (30, 120, 250), (255, 120, 200)),
}
if __name__ == "__main__":
    for kname, f in VARS.items():
        im = f()
        im.save(os.path.join(OUT, f"CatCafe_GameIcon_{kname}_1024.png"))
        im.resize((512, 512), Image.LANCZOS).save(os.path.join(OUT, f"CatCafe_GameIcon_{kname}_512.png"))
        print("wrote", kname)
