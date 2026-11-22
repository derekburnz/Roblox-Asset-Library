import sys
from PIL import Image, ImageDraw, ImageFont
S = sys.argv[1]
CATS = [
    ("Binbag", "Garbage Bag Cat (Rare): a shiny black bin bag over its back, tied on top, ragged hem"),
    ("Taxi", "Taxi Cat (Epic): a taxi roof light with a paw print, checkered flanks"),
    ("Neon", "Jazz Cat (Mythical): fedora, and a glowing saxophone on its back"),
    ("Birdwatch", "Birdwatcher Cat (Rare): green prism field binoculars"),
    ("Duckling", "Duckling Cat (Epic): a duckling riding on its head"),
    ("Balloon", "Balloon Cat (Mythical): three glowing balloons tied on its back"),
    ("Builder", "Construction Cat (Rare): hard hat with a pencil tucked in"),
    ("Gardener", "Gardener Cat (Epic): straw sun hat with a daisy, and a watering can"),
    ("Gnome", "Gnome Cat (Legendary): drooping gnome hat and a fluffy beard"),
    ("Plumber", "Plumber Cat (Rare): work cap, and a wrench on its back"),
]
F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 34)
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
W = 1800
for k, group in enumerate((CATS[:5], CATS[5:]), start=1):
    blocks = []
    for name, title in group:
        close = Image.open(f"{S}/f78c/_c_{name}_f.png"), Image.open(f"{S}/f78c/_c_{name}_b.png")
        front, back = Image.open(f"{S}/f78/{name}_front.png"), Image.open(f"{S}/f78/{name}_back.png")
        h = 60 + 600 + 34 + 400 + 34 + 400 + 20
        im = Image.new("RGB", (W, h), (255, 255, 255))
        d = ImageDraw.Draw(im)
        d.text((20, 12), title, font=F, fill=(40, 30, 30))
        y = 60
        im.paste(close[0].convert("RGB"), (0, y))
        im.paste(close[1].convert("RGB"), (900, y))
        d.text((20, y + 8), "walking and sitting, front", font=f, fill=(90, 70, 60))
        d.text((920, y + 8), "and from behind", font=f, fill=(90, 70, 60))
        y += 600
        d.text((20, y + 4), "at work, front: walking, gold, sitting, then barista, waiter, greeter, entertainer, "
               "and a plain Tabby for scale", font=f, fill=(90, 70, 60))
        y += 34
        im.paste(front.convert("RGB"), (0, y))
        y += 400
        d.text((20, y + 4), "at work, from behind (the same row seen from the other side)", font=f, fill=(90, 70, 60))
        y += 34
        im.paste(back.convert("RGB"), (0, y))
        blocks.append(im)
    sheet = Image.new("RGB", (W, sum(b.height for b in blocks)), (255, 255, 255))
    y = 0
    for b in blocks:
        sheet.paste(b, (0, y))
        y += b.height
    sheet = sheet.resize((int(W * 0.8), int(sheet.height * 0.8)), Image.LANCZOS)
    sheet.save(f"{S}/f78-themed-cats-{k}.png", optimize=True)
    print(sheet.size)
