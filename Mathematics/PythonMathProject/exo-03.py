import numpy as np
from PIL import Image
import time


def manual_convolve(image, kernel):
    # Flip kernel (kao u dokumentu: renversé)
    kernel = np.flipud(np.fliplr(kernel))  # Dozvoljeno, jer je osnovno; alternativno ručno sa petljama

    # Dimenzije
    img_h, img_w = image.shape
    ker_h, ker_w = kernel.shape
    pad_h = ker_h // 2
    pad_w = ker_w // 2

    # Padded image sa nulama (za rubove)
    padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

    # Nova matrica za rezultat
    result = np.zeros_like(image)

    # Ručna konvolucija sa petljama
    for i in range(img_h):
        for j in range(img_w):
            # Izreži regiju i pomnoži/sumiraj
            region = padded[i:i + ker_h, j:j + ker_w]
            result[i, j] = np.sum(region * kernel)

    return result


# Test na malom primjeru (adaptirano iz 1D primjera dokumenta)
test_image = np.array([[1, 0, 3], [5, 1, 2]])  # Mali 2D ulaz
test_kernel = np.array([[1, 2], [3, 4]])  # Maska
print("Test ulaz:\n", test_image)
print("Test kernel:\n", test_kernel)
result_test = manual_convolve(test_image, test_kernel)
print("Rezultat konvolucije:\n", result_test)

# Primjena na sliku
image_path = 'images/Lenna512.png'  # Grayscale Lenna
image = Image.open(image_path).convert('L')  # U sivo
image_array = np.asarray(image)

start_time = time.time()
convolved = manual_convolve(image_array, test_kernel)  # Koristi istu masku za test
end_time = time.time()
print(f"Vrijeme: {end_time - start_time:.4f} sekundi")

# Spremi
output_image = Image.fromarray(convolved.astype(np.uint8))
output_image.save('convolved_manual.png')
print("Spremljeno kao 'convolved_manual.png'")