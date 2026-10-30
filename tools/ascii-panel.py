# Latar panel tim: medan glyph tipis (gaya hero beranda), statis, untuk dipasang di belakang kartu.
# usage: python3 ascii-panel.py <dst> W H <bg-hex> <glyph-hex> seed
import sys, math, random
from PIL import Image, ImageDraw, ImageFont
dst, W, H, bg, fg, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5], int(sys.argv[6])
rnd = random.Random(seed)
CELL = 12
cols, rows = W // CELL, H // CELL
hx = lambda s: tuple(int(s.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
B, F = hx(bg), hx(fg)
font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 11, index=1)
ph = [rnd.uniform(0, 6.28) for _ in range(4)]
img = Image.new("RGB", (cols * CELL, rows * CELL), B)
d = ImageDraw.Draw(img)
GL = " .·:+x*"
for r in range(rows):
    for c in range(cols):
        x, y = c / cols, r / rows
        v = (math.sin(x * 5.1 + ph[0]) + math.sin(y * 4.3 + ph[1]) + math.sin((x + y) * 6.2 + ph[2]) + math.sin(math.hypot(x - .5, y - .5) * 9 + ph[3])) / 4
        v = (v + 1) / 2
        v = max(0, min(1, (v - .35) * 1.7))
        i = int(v * (len(GL) - 1))
        if i == 0: continue
        a = .25 + .55 * v
        col = tuple(round(B[k] + (F[k] - B[k]) * a) for k in range(3))
        d.text((c * CELL + 2, r * CELL), GL[i], font=font, fill=col)
img.save(dst, quality=82)
