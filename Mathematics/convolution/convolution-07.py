import os
import numpy as np
from PIL import Image
from scipy.signal import convolve2d

def load_gray_512(path):
    img = Image.open(path).convert("L").resize((512, 512))
    return np.array(img, dtype=np.float32)

def save_gray(arr, path):
    Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).save(path)

def main():
    input_path = os.path.join("images", "Lenna512.png")
    img = load_gray_512(input_path)

    kernel_enhance = np.array([
        [0.0, -0.5, 0.0],
        [-0.5, 3.0, -0.5],
        [0.0, -0.5, 0.0],
    ], dtype=np.float32)

    enhanced = convolve2d(img, kernel_enhance, mode="same", boundary="symm")
    out1 = os.path.join("images", "edges_enhanced.png")
    save_gray(enhanced, out1)

    kernel_edges = np.array([
        [0.0, -0.5, 0.0],
        [-0.5, 2.0, -0.5],
        [0.0, -0.5, 0.0],
    ], dtype=np.float32)

    edges = convolve2d(img, kernel_edges, mode="same", boundary="symm")

    edges_vis = np.abs(edges)
    edges_vis = edges_vis / (edges_vis.max() + 1e-9) * 255.0

    out2 = os.path.join("images", "edges_only.png")
    save_gray(edges_vis, out2)

    sketch = 255.0 - edges_vis
    out3 = os.path.join("images", "pencil_sketch.png")
    save_gray(sketch, out3)

    print("OK:")
    print(" -", out1)
    print(" -", out2)
    print(" -", out3)

if __name__ == "__main__":
    main()
