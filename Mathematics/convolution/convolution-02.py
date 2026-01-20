import numpy as np
from scipy.signal import convolve2d

image = np.array([
    [2, 1, 3, 0],
    [1, 1, 0, 5],
    [3, 3, 1, 0],
    [2, 0, 0, 2]
], dtype=float)

kernel = np.array([
    [1, 0, 2],
    [2, 1, 0],
    [1, 0, 3]
], dtype=float)

res = convolve2d(image, kernel, mode="same", boundary="fill", fillvalue=0)
print(res)
