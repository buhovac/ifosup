import numpy as np
from PIL import Image
import time  # Za mjerenje vremena, kao u dokumentu

# Učitaj sliku i pretvori u numpy array
image_path = 'images/6x2.png'  # Zamijeni sa putanjom do tvoje slike
image = Image.open(image_path)
image_array = np.asarray(image)  # Sada je matrica (height, width, 3) za RGB

# Dohvati dimenzije (kao u vježbi 2.0 i 2.2)
height, width, channels = image_array.shape
print(f"Slika ima dimenzije: {height} redova x {width} kolona x {channels} kanala (RGB)")

# Spremi kopiju (bez promjena, za test)
output_image = Image.fromarray(image_array)
output_image.save('images/6x2-kopija.png')