# Ilustrasi ASCII bergaya Sentra pengganti stock foto: medan glyph tipis (seperti hero beranda) di atas navy,
# dengan satu ikon Lucide (ISC) besar tersusun dari glyph terang + cahaya lembut di sekitarnya.
# usage: python3 art.py <icon.svg> <dst> W H seed
import sys, subprocess, io, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
svg, dst, W, H, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
rnd = random.Random(seed)
CELL = max(8, round(W / 78))
cols, rows = W // CELL, H // CELL
ox, oy = (W - cols * CELL) // 2, (H - rows * CELL) // 2

# ikon: stroke putih, dirasterkan lalu diturunkan ke resolusi grid
src = open(svg).read().replace('stroke="currentColor"', 'stroke="#fff"').replace('stroke-width="2"', 'stroke-width="1.9"')
side = round(rows * .62) * 4
png = subprocess.run(["rsvg-convert", "-w", str(side), "-h", str(side)], input=src.encode(), capture_output=True, check=True).stdout
ic = Image.open(io.BytesIO(png)).getchannel("A")
mask = Image.new("L", (cols * 4, rows * 4))
cx = cols * 4 // 2
mask.paste(ic, (cx - side // 2, rows * 4 // 2 - side // 2))
m = mask.resize((cols, rows), Image.BOX)
glow = mask.filter(ImageFilter.GaussianBlur(side / 14)).resize((cols, rows), Image.BOX)

# medan latar: noise halus dari grid acak kecil yang diperbesar bikubik
def blob(n):
    g = Image.new("L", (n + 2, round((n + 2) * rows / cols) + 2))
    g.putdata([rnd.randint(0, 255) for _ in range(g.width * g.height)])
    return g.resize((cols, rows), Image.BICUBIC)
f1, f2 = blob(6), blob(13)

RAMP = " .:-=+*#%@"
def mix(a, b, t): t = max(0, min(1, t)); return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))
BG1, BG2 = (19, 48, 107), (8, 21, 48)
C1, C2, HI = (62, 111, 204), (169, 198, 245), (236, 244, 255)
out = Image.new("RGB", (W, H)); d = ImageDraw.Draw(out)
for y in range(H): d.line([(0, y), (W, y)], fill=mix(BG1, BG2, y / H))
font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", round(CELL * 1.0), index=1)
for r in range(rows):
    for c in range(cols):
        x, y = ox + c * CELL, oy + r * CELL
        bg = mix(BG1, BG2, (y + CELL / 2) / H)
        a = m.getpixel((c, r)) / 255; gl = glow.getpixel((c, r)) / 255
        v = (f1.getpixel((c, r)) * .7 + f2.getpixel((c, r)) * .3) / 255
        if a > .12:                                   # ikon
            d.rectangle([x, y, x + CELL - 1, y + CELL - 1], fill=mix(bg, C1, .18 + .25 * a))
            ch, col = RAMP[5 + min(4, int(a * 5))], mix(C2, HI, a)
        elif gl > .06:                                # cahaya di sekitar ikon
            k = min(4, 1 + int(gl * 9)); ch, col = RAMP[k], mix(bg, C1, .45 + gl * 1.5)
        else:                                         # medan latar tipis
            k = (v - .5) / .5
            if k <= 0: continue
            ch, col = RAMP[min(6, 1 + int(k * 7))], mix(bg, C1, .25 + k * .6)
        d.text((x + CELL / 2, y + CELL / 2), ch, font=font, anchor="mm", fill=col)
if dst.endswith(".jpg"): out.save(dst, quality=84, optimize=True, progressive=True)
else: out.save(dst, "WEBP", quality=82, method=6)
