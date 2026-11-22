"""Game icon, 2026-11-16 20:36 UTC (Derek: "use excalipurr but make sure its actually being held in arms"): one render of the
real bacon with Excalipurr hugged in both arms (bacon_real.py pose carry, BACON_CAT). No word, so it reads at 50 px."""
import os
from PIL import Image
import ads as A
import kit17 as K
OUT = os.environ["HOME_OUT"]
HERE = os.path.dirname(os.path.abspath(__file__))


def scene(inner, outer, h=1420, y0=24):
    S = 1024
    img = K.burst((S, S), (0.5, 0.45), inner, outer, n=16, colours=[(255, 255, 255)], alpha=75)
    K.glow(img, 512, 520, 470, (255, 255, 255), 200)
    b = Image.open(os.path.join(HERE, "real_carry.png")).convert("RGBA")
    b = K.pop(b.crop(b.getbbox()), 1.15, 1.1)
    k = h / b.height
    b = b.resize((int(b.width * k), int(b.height * k)), Image.LANCZOS)
    A.hero(img, b, 512, y0 + b.height, rim=16, rim_rgb=K.INK, shadow=False)
    A.sparkles(img, [(890, 230, 120, (255, 255, 255)), (130, 400, 80, (255, 255, 255))])
    return img.convert("RGB")


VARS = {
    "J1_HoldExcalipurr_Blue": lambda: scene((200, 250, 255), (30, 110, 245)),
    "J2_HoldExcalipurr_Orange": lambda: scene((255, 250, 160), (255, 130, 20)),
}
if __name__ == "__main__":
    ims = {}
    for kname, f in VARS.items():
        im = f(); ims[kname] = im
        im.save(os.path.join(OUT, f"CatCafe_GameIcon_{kname}_1024.png"))
        im.resize((512, 512), Image.LANCZOS).save(os.path.join(OUT, f"CatCafe_GameIcon_{kname}_512.png"))
    sheet = Image.new("RGB", (1024 * 2 + 60, 1024 + 40 + 190), (24, 26, 32))
    for i, im in enumerate(ims.values()):
        sheet.paste(im, (20 + i * 1044, 20))
        for j, s in enumerate((150, 100, 50)):
            sheet.paste(im.resize((s, s), Image.LANCZOS), (20 + i * 1044 + j * 170, 1064))
    sheet.save(os.path.join(OUT, "DRAFT_SHEET_icon_bacon_holding_excalipurr.jpg"), quality=90)
