import sys
from PIL import Image, ImageDraw, ImageFont
S, NEWICONS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
W = 1800
INK, SUB, RED, GRN = (40, 30, 30), (90, 70, 60), (150, 60, 50), (40, 120, 70)
blocks = []
head = Image.new("RGB", (W, 140), "white")
d = ImageDraw.Draw(head)
d.text((20, 14), "F93 nets: L1 Basic, L2 Sturdy, L3 Pro and the new L4 Master, with a sitting Tabby for scale", font=F, fill=INK)
d.text((20, 62), "Left to right: Basic, Sturdy, Pro, Master. Each has a rim (_Hoop), strands (_Bag) over a see-through", font=f, fill=SUB)
d.text((20, 96), "cone (_Bag_Glass), and one Grip on the black wrap. The rim's far edge stays the farthest point from the Grip.", font=f, fill=SUB)
blocks.append(head)
for view, label in (("top", "from above"), ("side", "from the side")):
    for tag, col, img in (("before (today, three levels)", RED, f"{S}/old_{view}.png"), ("after", GRN, f"{S}/new_{view}.png")):
        im = Image.new("RGB", (W, 40 + 800), "white")
        d = ImageDraw.Draw(im)
        d.text((20, 6), f"{tag}, {label}", font=f, fill=col)
        im.paste(Image.open(img).convert("RGB"), (0, 40))
        blocks.append(im)
# shop pictures: old and new on the cream shop card colour
cream, dark = (243, 238, 226), (58, 56, 68)
row = Image.new("RGB", (W, 40 + 2 * 380 + 40), "white")
d = ImageDraw.Draw(row)
d.text((20, 6), "Shop pictures (exports/icons/CatCafe_Icon_Net_L1 to L4): before on top, after below", font=f, fill=INK)
for r, (bg, files) in enumerate(((cream, [f"{S}/old/CatCafe_Icon_Net_L{n}.png" for n in (1, 2, 3)]),
                                 (cream, [f"{NEWICONS}/CatCafe_Icon_Net_L{n}.png" for n in (1, 2, 3, 4)]))):
    y = 40 + r * 400
    for i in range(4):
        x = 20 + i * 445
        card = Image.new("RGB", (420, 380), bg)
        if i < len(files):
            ic = Image.open(files[i]).convert("RGBA").resize((360, 360), Image.LANCZOS)
            card.paste(ic, (30, 10), ic)
        else:
            ImageDraw.Draw(card).text((150, 170), "(none)", font=f, fill=(160, 150, 150))
        row.paste(card, (x, y))
blocks.append(row)
sheet = Image.new("RGB", (W, sum(b.height for b in blocks)), "white")
y = 0
for b in blocks:
    sheet.paste(b, (0, y))
    y += b.height
sheet = sheet.resize((int(W * 0.7), int(sheet.height * 0.7)), Image.LANCZOS)
sheet.save(OUT, quality=88, optimize=True)
print(sheet.size)
