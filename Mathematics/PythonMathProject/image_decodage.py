from PIL import Image
import math
IN_PATH = "images/image_cryptee.png"
OUT_PATH = "images/image_decrypted.png"

img = Image.open(IN_PATH).convert("RGB")
w, h = img.size

out = Image.new("RGB", (w, h))
px = img.load()
out_px = out.load()

for y in range(h):
    for x in range(w):
        r, g, b = px[x, y]

        r2 = (r % 16) * 16
        g2 = (g % 16) * 16
        b2 = (b % 16) * 16

        out_px[x, y] = (r2, g2, b2)

out.save(OUT_PATH)
out.show()

print(f"Saved secret image to {OUT_PATH}")
