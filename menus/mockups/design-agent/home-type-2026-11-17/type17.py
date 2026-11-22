"""Home icon and thumbnail words in the Top Trending style (Design-Agent, 2026-11-16, Growth brief 5-tweaks).

What the trending tiles do with their one word (NOW!, NEW UPDATE!, NAME A PET, AXOLOTL +100): a chunky rounded font,
a bright top-to-bottom gradient, a gloss band on the top half of the letters, a thin light line inside a very thick
dark outline, a solid 3D extrude under the letters, and a soft drop shadow. It must read at 50 px.

Drop-in for Model-Agent's A.words: word(img, text, size, cx, cy, style, tilt). Or render(text, size, style) returns
the RGBA layer to place yourself. style = (top, bottom, ink) colours, see the presets below.

    python3 type17.py          writes demo.png (every preset) next to this file
"""
import math
import os

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.environ.get(
    "TYPE_FONT", "/mnt/project-files/Model-Agent/store-and-ads/update-2026-11-12/fonts/LuckiestGuy-Regular.ttf")

# (top of the letters, bottom of the letters, outline and extrude ink)
GOLD = ((255, 246, 140), (255, 170, 20), (70, 30, 5))
MYTHIC = ((255, 225, 245), (255, 60, 160), (80, 8, 50))
SECRET = ((235, 215, 255), (150, 70, 255), (30, 8, 60))
MONEY = ((230, 255, 170), (60, 205, 60), (10, 60, 15))
SKY = ((235, 250, 255), (60, 170, 255), (10, 40, 100))
WHITE = ((255, 255, 255), (220, 232, 255), (30, 30, 60))
PRESETS = {"GOLD": GOLD, "MYTHIC": MYTHIC, "SECRET": SECRET, "MONEY": MONEY, "SKY": SKY, "WHITE": WHITE}


def _mask(text, font, pad, stroke=0):
    d = ImageDraw.Draw(Image.new("L", (8, 8)))
    l, t, r, b = d.textbbox((0, 0), text, font=font, stroke_width=stroke)
    w, h = r - l + pad * 2, b - t + pad * 2
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).text((pad - l, pad - t), text, font=font, fill=255, stroke_width=stroke, stroke_fill=255)
    return m


def render(text, size, style=GOLD, stroke=None, depth=None, inner=None, font=None):
    """The word as an RGBA layer, untilted. stroke: dark outline px (default size/7); depth: extrude px (size/9)."""
    top, bottom, ink = style
    f = ImageFont.truetype(font or FONT, size)
    stroke = stroke or max(8, size // 7)
    depth = depth or max(5, size // 9)
    inner = inner or max(3, size // 34)
    pad = stroke + depth + size // 6
    fill = _mask(text, f, pad)  # the letters
    outer = _mask(text, f, pad, stroke)  # letters plus the dark outline
    light = _mask(text, f, pad, inner)  # letters plus the thin light line
    W, H = fill.size
    lay = Image.new("RGBA", (W, H + depth), (0, 0, 0, 0))
    # drop shadow, soft, under everything
    sh = Image.new("RGBA", lay.size, (0, 0, 0, 0))
    sh.paste((0, 0, 0, 120), (0, depth + size // 18), outer)
    lay.alpha_composite(sh.filter(ImageFilter.GaussianBlur(size // 16)))
    # 3D extrude: the outline shape stacked down, darkest at the bottom
    dark = tuple(int(c * 0.55) for c in ink)
    for k in range(depth, 0, -1):
        lay.paste(dark + (255,), (0, k), outer)
    lay.paste(ink + (255,), (0, 0), outer)
    # the thin light line just inside the outline
    lay.paste((255, 255, 255, 255), (0, 0), light)
    # gradient fill across the letters' own height
    bbox = fill.getbbox() or (0, 0, W, H)
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    y0, y1 = bbox[1], bbox[3]
    for y in range(H):
        u = min(1.0, max(0.0, (y - y0) / max(1, y1 - y0)))
        u = u ** 1.2
        gd.line([(0, y), (W, y)], fill=tuple(int(top[i] + (bottom[i] - top[i]) * u) for i in range(3)) + (255,))
    lay.paste(grad, (0, 0), fill)
    # gloss: a soft white band over the top 45% of the letters, shrunk off the edges
    gloss = Image.new("L", (W, H), 0)
    ImageDraw.Draw(gloss).rectangle([0, y0, W, y0 + int((y1 - y0) * 0.42)], fill=120)
    shrunk = fill.filter(ImageFilter.MinFilter(max(3, (size // 22) | 1)))
    gloss = ImageChops.multiply(gloss, shrunk).filter(ImageFilter.GaussianBlur(max(1, size // 60)))
    lay.paste((255, 255, 255, 255), (0, 0), gloss)
    return lay


def place(img, layer, cx, cy, tilt=0):
    if tilt:
        layer = layer.rotate(tilt, resample=Image.BICUBIC, expand=True)
    img.alpha_composite(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)))
    return layer.size


def word(img, text, size, cx, cy, style=GOLD, tilt=0, font=None, stroke=None):
    """Same call as Model-Agent's A.words. Lines split on \\n are stacked, each centred."""
    lines = text.split("\n")
    layers = [render(line, size, style, stroke=stroke, font=font) for line in lines]
    gap = -int(size * 0.32)  # the extrude and padding overlap between lines
    total = sum(l.height for l in layers) + gap * (len(layers) - 1)
    block = Image.new("RGBA", (max(l.width for l in layers), total), (0, 0, 0, 0))
    y = 0
    for l in layers:
        block.alpha_composite(l, ((block.width - l.width) // 2, y))
        y += l.height + gap
    return place(img, block, cx, cy, tilt)


def fit(text, max_w, style=GOLD, start=260, font=None):
    """The biggest size whose rendered word is at most max_w px wide."""
    size = start
    while size > 20 and render(text, size, style, font=font).width > max_w:
        size -= 6
    return size


if __name__ == "__main__":
    demo = Image.new("RGBA", (1600, 1300), (60, 150, 255, 255))
    y = 110
    for (name, st), w in zip(PRESETS.items(), ("CATCH!", "MYTHIC!", "SECRET CAT!", "$1,000,000", "BOOM!", "100+ CATS!")):
        word(demo, w, 140, 520, y, st, tilt=-4 if name in ("GOLD", "MYTHIC") else 0)
        word(demo, name, 50, 1300, y, st)
        y += 200
    demo.convert("RGB").save(os.path.join(HERE, "demo.png"))
