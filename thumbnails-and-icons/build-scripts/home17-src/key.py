import sys
import numpy as np
from PIL import Image, ImageFilter
src, out = sys.argv[1], sys.argv[2]
flip = len(sys.argv) > 3 and sys.argv[3] == "flip"
a = np.asarray(Image.open(src).convert("RGB")).astype(np.float32)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
m = np.minimum(r, b) - g                      # how magenta
alpha = np.clip(1.0 - (m - 40) / 150.0, 0, 1)
spill = np.clip(m, 0, None) * (alpha > 0)     # pull the pink out of soft edges
r2 = r - spill * 0.9; b2 = b - spill * 0.9
rgba = np.dstack([np.clip(r2, 0, 255), g, np.clip(b2, 0, 255), alpha * 255]).astype(np.uint8)
img = Image.fromarray(rgba, "RGBA")
al = img.split()[3].filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.6))
img.putalpha(al)
img = img.crop(img.getbbox())
if flip:
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
img = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)
img.save(out); print(out, img.size)
