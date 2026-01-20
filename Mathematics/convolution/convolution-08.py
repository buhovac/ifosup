import os
import numpy as np
from PIL import Image
from scipy.signal import convolve2d

def load_gray_512(path):
    img = Image.open(path).convert("L").resize((512, 512))
    return np.array(img, dtype=np.float32)

def save(arr, path):
    Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).save(path)

def normalize(arr):
    arr = np.abs(arr)
    return arr / (arr.max() + 1e-9) * 255.0

def main():
    input_path = os.path.join("images", "Lenna512.png")
    img = load_gray_512(input_path)

    kernel_v = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float32)

    kernel_h = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ], dtype=np.float32)

    sobel_v = convolve2d(img, kernel_v, mode="same", boundary="symm")
    sobel_h = convolve2d(img, kernel_h, mode="same", boundary="symm")

    save(normalize(sobel_v), os.path.join("images", "sobel_vertical.png"))
    save(normalize(sobel_h), os.path.join("images", "sobel_horizontal.png"))

    magnitude = np.sqrt(sobel_v**2 + sobel_h**2)
    magnitude = normalize(magnitude)

    save(magnitude, os.path.join("images", "sobel_edges.png"))

    sketch = 255 - magnitude
    save(sketch, os.path.join("images", "sobel_pencil.png"))

    print("OK Sobel:")
    print("- sobel_vertical.png")
    print("- sobel_horizontal.png")
    print("- sobel_edges.png")
    print("- sobel_pencil.png")

if __name__ == "__main__":
    main()
