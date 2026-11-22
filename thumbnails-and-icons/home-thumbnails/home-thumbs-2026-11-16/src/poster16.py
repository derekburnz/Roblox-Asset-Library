"""Poster frame for the gameplay video (brief 2, 2026-11-16): the net lands on a glowing Mythical, word CAUGHT!"""
import os
from PIL import Image
import ads as A
import home16 as Hm
A.W, A.H = 1920, 1080
img = A.bg((255, 255, 255), (60, 165, 255), rays=(255, 255, 255), centre=(0.66, 0.58), ray_alpha=70)
Hm.glow(img, 1270, 600, 600, (255, 190, 230), 220)
A.hero(img, A.cut("cat_Balloon", 820), 1330, 940, rim=24, glow=(255, 80, 170), tilt=-5)
A.hero(img, A.cut("pl_net", 700), 600, 1050, rim=14, tilt=4)
A.sparkles(img, [(900, 330, 90, (255, 255, 255)), (1720, 400, 100, (255, 255, 255)), (1000, 930, 60, (255, 240, 160)),
                 (1760, 830, 70, (255, 240, 160)), (1560, 200, 60, (255, 240, 160))])
A.words(img, "CAUGHT!", 270, 560, 175, Hm.MYTH, -4)
img.convert("RGB").save(os.path.join(os.environ["HOME_OUT"], "CatCafe_VideoPoster_Caught_1920x1080.png"))
