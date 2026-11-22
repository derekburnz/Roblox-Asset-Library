"""Compose a before/after sheet: python3 compose_solid.py out.png "Title" "label|before.png|after.png" ...
A row with before "-" shows only the after image at full width. A row labelled "left ~ right" with before
starting "+" shows two after images side by side, each with its own label. Images are scaled to one column width."""
import sys

from PIL import Image, ImageDraw, ImageFont

out, title, rows = sys.argv[1], sys.argv[2], sys.argv[3:]
COL, GAP, HEAD, LAB = 960, 16, 70, 44
BG, INK, SUB = (247, 240, 230), (60, 44, 36), (140, 110, 95)


def font(sz):
    for f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(f, sz)
        except OSError:
            pass
    return ImageFont.load_default()


def fit(path, w):
    im = Image.open(path).convert("RGB")
    return im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)


tiles = []
for r in rows:
    label, before, after = r.split("|")
    if before.startswith("+"):
        b, a = fit(before[1:], COL), fit(after, COL)
        tiles.append((label, b, a, max(a.height, b.height)))
    elif before == "-":
        a = fit(after, 2 * COL + GAP)
        tiles.append((label, None, a, a.height))
    else:
        b, a = fit(before, COL), fit(after, COL)
        tiles.append((label, b, a, max(a.height, b.height)))
W = 2 * COL + 3 * GAP
H = HEAD + sum(LAB + h + GAP for *_, h in tiles) + GAP
sheet = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(sheet)
d.text((GAP, 18), title, fill=INK, font=font(34))
y = HEAD
for label, b, a, h in tiles:
    if b is None:
        d.text((GAP, y + 8), label, fill=INK, font=font(24))
        sheet.paste(a, (GAP, y + LAB))
    elif " ~ " in label:
        left, right = label.split(" ~ ")
        d.text((GAP, y + 8), left, fill=INK, font=font(24))
        d.text((2 * GAP + COL, y + 8), right, fill=INK, font=font(24))
        sheet.paste(b, (GAP, y + LAB))
        sheet.paste(a, (2 * GAP + COL, y + LAB))
    else:
        d.text((GAP, y + 8), "Before: " + label, fill=SUB, font=font(24))
        d.text((2 * GAP + COL, y + 8), "After", fill=INK, font=font(24))
        sheet.paste(b, (GAP, y + LAB))
        sheet.paste(a, (2 * GAP + COL, y + LAB))
    y += LAB + h + GAP
sheet.save(out, optimize=True)
print("wrote", out, sheet.size)
