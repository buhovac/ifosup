from PIL import Image
import numpy as np
import os

def convolve_manual(image, kernel):
    H, W = image.shape
    kh, kw = kernel.shape

    pad_h = kh // 2
    pad_w = kw // 2

    out = image.copy().astype(np.float32)

    for y in range(pad_h, H - pad_h):
        for x in range(pad_w, W - pad_w):
            s = 0.0
            for i in range(kh):
                for j in range(kw):
                    s += kernel[i, j] * image[y - pad_h + i, x - pad_w + j]
            out[y, x] = s

    return out

def main():
    input_path = os.path.join("images", "Lenna512.png")

    img = Image.open(input_path).convert("L").resize((512, 512))
    image = np.array(img, dtype=np.float32)

    kernel = np.ones((1, 9), dtype=np.float32) / 9.0

    blurred = convolve_manual(image, kernel)

    out_path = os.path.join("images", "blur_directionnel_LR_1x9.png")
    Image.fromarray(np.clip(blurred, 0, 255).astype(np.uint8)).save(out_path)

    print("OK:", input_path, "->", out_path)

if __name__ == "__main__":
    main()
