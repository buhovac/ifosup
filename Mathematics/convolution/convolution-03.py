import numpy as np
from scipy.signal import convolve2d
from PIL import Image

def load_grayscale_512(path):
    img = Image.open(path).convert("L").resize((512, 512))
    return np.array(img, dtype=np.float32)

def blur_convolve2d(image, kernel, boundary="symm"):
    return convolve2d(image, kernel, mode="same", boundary=boundary)

def save_image(arr, out_path):
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    Image.fromarray(arr).save(out_path)

# --- main ---
img = load_grayscale_512("images/Lenna512.png")

kernel_3 = np.ones((3, 3), dtype=np.float32) / 9.0
kernel_10 = np.ones((10, 10), dtype=np.float32) / 100.0

blur3 = blur_convolve2d(img, kernel_3, boundary="symm")
blur10 = blur_convolve2d(img, kernel_10, boundary="symm")

save_image(blur3, "blur_3x3.png")
save_image(blur10, "blur_10x10.png")
print("OK: blur_3x3.png et blur_10x10.png générés")
