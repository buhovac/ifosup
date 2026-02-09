# ex2-4.py
# Pillow = open/save, numpy = manual pixel work, time = measurement, matplotlib = display

from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt


# ================================
# 1) START TIMER
# ================================
t_debut = time.time()

# ================================
# 2) OPEN IMAGE
# ================================
img_pil = Image.open("images/Lenna512.png").convert("RGB")
image = np.array(img_pil)

nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]

print(f"Dimensions: {nb_lignes} lignes x {nb_colonnes} colonnes")
print(f"Shape complet: {image.shape}")

# Save original (required naming convention)
Image.fromarray(image).save("image_entree.png")

# ================================
# 3) TRAITEMENT (EX 2.4) : MIROIR HORIZONTAL (LEFT <-> RIGHT)
# ================================
# We create a new array and fill it manually (no numpy shortcuts like flip)
image_sortie = np.zeros_like(image)

for i in range(nb_lignes):
    for j in range(nb_colonnes):
        # mirror horizontally: column j becomes (nb_colonnes - 1 - j)
        image_sortie[i, nb_colonnes - 1 - j] = image[i, j]

# Save result
Image.fromarray(image_sortie).save("image_sortie.png")

# ================================
# 4) END TIMER
# ================================
t_fin = time.time()
print(f"Temps de traitement: {t_fin - t_debut:.6f} secondes")

# ================================
# 5) DISPLAY WITH MATPLOTLIB
# ================================
img_in = np.array(Image.open("image_entree.png").convert("RGB"))
img_out = np.array(Image.open("image_sortie.png").convert("RGB"))

plt.figure()
plt.title("Image d'origine (image_entree)")
plt.imshow(img_in)
plt.axis("off")

plt.figure()
plt.title("Miroir horizontal (image_sortie)")
plt.imshow(img_out)
plt.axis("off")

plt.show()
