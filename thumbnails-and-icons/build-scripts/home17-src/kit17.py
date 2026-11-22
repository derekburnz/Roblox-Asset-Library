"""Helpers for the 2026-11-17 store picture set (Derek 2026-11-16: glossy, subject fills the frame, big bacon, one word)."""
import colorsys
import math
import os

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

import ads as A

HERE = os.path.dirname(os.path.abspath(__file__))
INK = (50, 20, 10)
RAINBOW = [(255, 90, 110), (255, 170, 60), (255, 230, 80), (110, 225, 120), (90, 190, 255), (190, 120, 255)]


def cutp(name, h=None, w=None, flip=False, folder="cut17"):
    im = Image.open(os.path.join(HERE, folder, name + ".png")).convert("RGBA")
    im = im.crop(im.getbbox())
    if h:
        im = im.resize((max(1, int(im.width * h / im.height)), h), Image.LANCZOS)
    elif w:
        im = im.resize((w, max(1, int(im.height * w / im.width))), Image.LANCZOS)
    return im.transpose(Image.FLIP_LEFT_RIGHT) if flip else im


def pop(im, sat=1.25, con=1.08):
    """The saturated toy look: more colour and a little more contrast, alpha kept."""
    a = im.split()[3]
    rgb = ImageEnhance.Contrast(ImageEnhance.Color(im.convert("RGB")).enhance(sat)).enhance(con)
    rgb.putalpha(a)
    return rgb


def burst(size, centre, inner, outer, n=18, colours=None, alpha=120, spin=0.0):
    """A round gradient with wedge rays from `centre` (0..1); `colours` cycles the wedges (a rainbow burst)."""
    W, H = size
    A.W, A.H = W, H
    img = A.bg(inner, outer, centre=centre)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    X, Y = centre[0] * W, centre[1] * H
    R = 3 * max(W, H)
    for i in range(n):
        a0 = 2 * math.pi * i / n + spin
        a1 = a0 + math.pi / n
        c = colours[i % len(colours)] if colours else (255, 255, 255)
        d.polygon([(X, Y), (X + R * math.cos(a0), Y + R * math.sin(a0)), (X + R * math.cos(a1), Y + R * math.sin(a1))],
                  fill=c + (alpha,))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(2)))
    return img


def glow(img, cx, cy, r, rgb, a=200):
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(lay).ellipse([cx - r, cy - r, cx + r, cy + r], fill=rgb + (a,))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(r // 3)))


def vignette(img, strength=90, rgb=(20, 10, 60)):
    W, H = img.size
    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).ellipse([-W * 0.15, -H * 0.15, W * 1.15, H * 1.15], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(max(W, H) // 6)).point(lambda v: int((255 - v) * strength / 255))
    lay = Image.new("RGBA", (W, H), rgb + (0,)); lay.putalpha(m)
    img.alpha_composite(lay)


def shine(img, box, alpha=70):
    """A soft white gloss streak across `box` (x0, y0, x1, y1), for the shiny tile look."""
    lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    x0, y0, x1, y1 = box
    ImageDraw.Draw(lay).polygon([(x0, y1), (x0 + (x1 - x0) * 0.35, y0), (x1, y0), (x1 - (x1 - x0) * 0.35, y1)],
                                fill=(255, 255, 255, alpha))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(30)))


import sys  # noqa: E402
sys.path.insert(0, os.environ.get("TYPE17", "/mnt/project-files/Design-Agent/home-type-2026-11-17"))
import type17 as T  # noqa: E402  Design-Agent's chunky trending-style lettering


def word(img, text, size, cx, cy, style=None, tilt=0):
    """Design's lettering at the sizes these layouts were drawn for (its outline and extrude add about a fifth)."""
    T.word(img, text, int(size * 0.84), cx, cy, style or T.GOLD, tilt)
