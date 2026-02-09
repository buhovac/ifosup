from PIL import Image
import os

BASE_PATH = "image_base.png"
CACHE_PATH = "image_cache.png"
OUT_PATH = "images/image_cryptee.png"

def encode_pixel_channel(base_val: int, cache_val: int) -> int:
    base_high = base_val & 0xF0
    cache_high_to_low = (cache_val & 0xF0) >> 4
    return base_high | cache_high_to_low

def main():
    if not os.path.exists(BASE_PATH):
        raise FileNotFoundError(f"Missing file: {BASE_PATH}")
    if not os.path.exists(CACHE_PATH):
        raise FileNotFoundError(f"Missing file: {CACHE_PATH}")

    base_img = Image.open(BASE_PATH).convert("RGB")
    cache_img = Image.open(CACHE_PATH).convert("RGB")

    if base_img.size != cache_img.size:
        raise ValueError(f"Images must have the same size. base={base_img.size}, cache={cache_img.size}")

    w, h = base_img.size
    out_img = Image.new("RGB", (w, h))

    base_px = base_img.load()
    cache_px = cache_img.load()
    out_px = out_img.load()

    for y in range(h):
        for x in range(w):
            br, bg, bb = base_px[x, y]
            cr, cg, cb = cache_px[x, y]

            r = encode_pixel_channel(br, cr)
            g = encode_pixel_channel(bg, cg)
            b = encode_pixel_channel(bb, cb)

            out_px[x, y] = (r, g, b)

    out_img.save(OUT_PATH)
    print(f"Done: {OUT_PATH} created ({w}x{h})")

if __name__ == "__main__":
    main()
