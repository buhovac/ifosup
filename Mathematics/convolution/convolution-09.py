import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def intensity_profile(image, x0, y0, x1, y1, n=500):
    """
    image : 2D numpy array (grayscale)
    (x0,y0) -> (x1,y1) : linija
    n : broj uzoraka
    """
    xs = np.linspace(x0, x1, n)
    ys = np.linspace(y0, y1, n)

    profile = []
    for x, y in zip(xs, ys):
        xi = int(round(x))
        yi = int(round(y))
        profile.append(image[yi, xi])

    return profile

def main():
    img_path = os.path.join("images", "image.png")
    img = Image.open(img_path).convert("L")
    image = np.array(img, dtype=np.float32)

    # linija (primjer)
    x0, y0 = 50, 100
    x1, y1 = 450, 350

    profile = intensity_profile(image, x0, y0, x1, y1)

    # prikaz slike + linije
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.plot([x0, x1], [y0, y1], 'r')
    plt.title("Image + ligne de mesure")
    plt.axis("off")

    # profil
    plt.subplot(1, 2, 2)
    plt.plot(profile)
    plt.title("Profil d'intensité")
    plt.xlabel("Distance (pixels)")
    plt.ylabel("Intensité")
    plt.grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
