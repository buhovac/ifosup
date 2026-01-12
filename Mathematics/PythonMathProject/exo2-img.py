import numpy as np
from PIL import Image
import time


image_path = 'images/Lenna512.png'
image = Image.open(image_path)
image_array = np.asarray(image)

# Dohvati dimenzije
height, width = image_array.shape[:2]
channels = image_array.shape[2] if len(image_array.shape) == 3 else 1  # 3 za RGB, 1 za grayscale

print(f"Originalna slika: {height} redova x {width} kolona x {channels} kanala")

# 2. Definiraj područje za cropping (kao u primjeru: redovi 240-290, kolone 240-360)
start_row = 240
end_row = 290
start_col = 240
end_col = 360

# Izračunaj nove dimenzije (visina = end_row - start_row, širina = end_col - start_col)
new_height = end_row - start_row
new_width = end_col - start_col

# Provjeri da li su koordinate validne (da ne izlaze izvan slike)
if start_row < 0 or end_row > height or start_col < 0 or end_col > width:
    raise ValueError("Koordinate su izvan granica slike!")

# 3. Kreiraj novi numpy array za cropirani dio (prazan, iste tipa uint8)
cropped_array = np.zeros((new_height, new_width, channels) if channels > 1 else (new_height, new_width), dtype=np.uint8)

# 4. Ručno kopiraj piksele koristeći for petlje
start_time = time.time()  # Mjeri vrijeme za performanse (kao u dokumentu)

for row in range(new_height):
    for col in range(new_width):
        # Kopiraj piksel iz originala: originalni položaj je start_row + row, start_col + col
        cropped_array[row, col] = image_array[start_row + row, start_col + col]

end_time = time.time()
print(f"Vrijeme ručnog croppinga: {end_time - start_time:.4f} sekundi")

# 5. Pretvori nazad u Pillow Image i spremi
cropped_image = Image.fromarray(cropped_array)
cropped_image.save('images/cropirano_rucno.png')
print("Cropirana slika spremljena kao 'images/cropirano_rucno.png'!")