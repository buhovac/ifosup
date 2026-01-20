from PIL import Image
import numpy as np

def convolution(image, kernel):
    h = len(image)
    w = len(image[0])

    kh = len(kernel)
    kw = len(kernel[0])

    pad_h = kh // 2
    pad_w = kw // 2

    # kopija radi “rubovi se kopiraju”
    result = [row[:] for row in image]

    for i in range(pad_h, h - pad_h):
        for j in range(pad_w, w - pad_w):
            s = 0.0
            for ki in range(kh):
                for kj in range(kw):
                    s += kernel[ki][kj] * image[i - pad_h + ki][j - pad_w + kj]
            result[i][j] = s

    return result

def main():
    # 1) ucitaj i pripremi 512x512 grayscale
    img = Image.open("images/4-2-03-BW.png").convert("L").resize((512, 512))
    image = np.array(img, dtype=float).tolist()

    # 2) gauss kernel 3x3
    kernel_gauss = [
        [1/16, 2/16, 1/16],
        [2/16, 4/16, 2/16],
        [1/16, 2/16, 1/16]
    ]

    # 3) primijeni filter
    blurred = convolution(image, kernel_gauss)

    # 4) spremi rezultat
    out = np.clip(np.array(blurred), 0, 255).astype("uint8")
    Image.fromarray(out).save("blur_gauss_3x3.png")

    print("OK: image.png -> blur_gauss_3x3.png (512x512)")

if __name__ == "__main__":
    main()
