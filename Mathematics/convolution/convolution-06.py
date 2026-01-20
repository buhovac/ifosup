from PIL import Image
import numpy as np
import os

def median_filter_manual(image, k=3):
    """
    image: 2D numpy array float
    k: veličina prozora (mora biti neparna: 3,5,7...)
    Rubovi: kopirani (kao u kursu)
    """
    if k % 2 == 0:
        raise ValueError("k doit être impair (3,5,7,...)")

    H, W = image.shape
    pad = k // 2

    out = image.copy().astype(np.float32)

    for y in range(pad, H - pad):
        for x in range(pad, W - pad):
            window = image[y-pad:y+pad+1, x-pad:x+pad+1].flatten()
            out[y, x] = float(np.median(window))

    return out

def main():
    input_path = os.path.join("images", "image.png")  # promijeni ime po potrebi
    img = Image.open(input_path).convert("L").resize((512, 512))
    image = np.array(img, dtype=np.float32)

    filtered = median_filter_manual(image, k=3)

    out_path = os.path.join("images", "median_3x3_manual.png")
    Image.fromarray(np.clip(filtered, 0, 255).astype(np.uint8)).save(out_path)

    print("OK:", input_path, "->", out_path)

if __name__ == "__main__":
    main()
