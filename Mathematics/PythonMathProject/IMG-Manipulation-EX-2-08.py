# ex2-8.py — version corrigée (sans overflow)
# Pillow = open/save, numpy = traitement manuel, time = mesure, matplotlib = affichage

from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt

DELTA = 40  # + augmente la luminosité, - diminue

# ================================
# 1) TIMER START
# ================================
t_debut = time.time()

# ================================
# 2) OUVERTURE IMAGE
# ================================
img_src = Image.open("images/Lenna512.png").convert("RGB")
image = np.array(img_src)

nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]

print(f"Dimensions: {nb_lignes} x {nb_colonnes} | Shape: {image.shape}")
print(f"Delta luminosité = {DELTA}")

Image.fromarray(image).save("image_entree.png")

# ================================
# 3) TRAITEMENT : MODIFICATION DE LUMINOSITÉ (SANS OVERFLOW)
# ================================
image_sortie = np.zeros_like(image)

for i in range(nb_lignes):
    for j in range(nb_colonnes):
        r, v, b = image[i, j]

        r2 = min(255, max(0, int(r) + DELTA))
        v2 = min(255, max(0, int(v) + DELTA))
        b2 = min(255, max(0, int(b) + DELTA))

        image_sortie[i, j] = [r2, v2, b2]

Image.fromarray(image_sortie).save("image_sortie.png")

# ================================
# 4) TIMER END
# ================================
t_fin = time.time()
print(f"Temps de traitement: {t_fin - t_debut:.6f} secondes")

# ================================
# 5) AFFICHAGE
# ================================
img_in  = np.array(Image.open("image_entree.png"))
img_out = np.array(Image.open("image_sortie.png"))

plt.figure()
plt.title("Original")
plt.imshow(img_in)
plt.axis("off")

plt.figure()
plt.title(f"Luminosité modifiée (Δ={DELTA})")
plt.imshow(img_out)
plt.axis("off")

plt.show()
