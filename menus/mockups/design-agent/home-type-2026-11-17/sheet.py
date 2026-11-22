"""Icon check: our icon variants beside 8 Top Trending tiles at 100 and 50 px, rounded like the Home page, on its dark
background (Growth brief 5-tweaks, 17:45 UTC: "the Home icon must hold up next to the Top Trending tiles").

    python3 sheet.py OUT.png icon1.png [icon2.png ...]     (each icon 512 or 1024 square; label = file name)
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

REF = "/mnt/project-files/Model-Agent/home-thumbs-2026-11-17/refs/bdde9f16-top_trending.png"
# (x, y) of the tile's top left in Derek's Top Trending screenshot; every tile is 127 px
TILES = [(154, 49), (17, 255), (154, 255), (1113, 255), (17, 462), (154, 462), (154, 668), (565, 668)]
NAMES = ["Throw Food", "NOW", "New Update", "Name a Pet", "Cozy Scoops", "Raise Catboy", "Net a Fish", "Name Animal"]
BG = (25, 27, 32)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def rounded(im, s):
    t = im.convert("RGB").resize((s, s), Image.LANCZOS)
    m = Image.new("L", (s, s), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, s - 1, s - 1], max(4, s // 12), fill=255)
    return t, m


def sheet(out, icons):
    ref = Image.open(REF).convert("RGB")
    trend = [ref.crop((x, y, x + 127, y + 127)) for x, y in TILES]
    ours = [(os.path.splitext(os.path.basename(p))[0][-18:], Image.open(p)) for p in icons]
    f = ImageFont.truetype(FONT, 13)
    rows = []
    # one row per our icon: our icon first, then the 8 trending tiles, at 100 and again at 50
    for label, im in ours:
        rows.append((label, [im] + trend))
    cell100, cell50, gap = 100, 50, 14
    w = 20 + 9 * (cell100 + gap) + 30 + 9 * (cell50 + 8) + 20
    h = 50 + len(rows) * (cell100 + 40) + 10
    sh = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(sh)
    d.text((20, 14), "100 px", font=f, fill=(200, 200, 210))
    d.text((20 + 9 * (cell100 + gap) + 30, 14), "50 px", font=f, fill=(200, 200, 210))
    for r, (label, tiles) in enumerate(rows):
        y = 40 + r * (cell100 + 40)
        x = 20
        for i, im in enumerate(tiles):
            t, m = rounded(im, cell100)
            if i == 0:
                d.rounded_rectangle([x - 4, y - 4, x + cell100 + 3, y + cell100 + 3], 12, outline=(255, 210, 60), width=3)
            sh.paste(t, (x, y), m)
            d.text((x, y + cell100 + 6), label if i == 0 else NAMES[i - 1], font=f, fill=(230, 230, 235))
            x += cell100 + gap
        x += 30
        for i, im in enumerate(tiles):
            t, m = rounded(im, cell50)
            if i == 0:
                d.rounded_rectangle([x - 3, y - 3, x + cell50 + 2, y + cell50 + 2], 8, outline=(255, 210, 60), width=2)
            sh.paste(t, (x, y), m)
            x += cell50 + 8
    sh.save(out)


if __name__ == "__main__":
    sheet(sys.argv[1], sys.argv[2:])
