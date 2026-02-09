# ex2-5.py
# Exercice 2.5 — Négatif sur:
#  - une image couleur (RGB)
#  - une image en niveaux de gris (L)
#
# Rules respected:
# - Pillow only for open/save
# - Manual pixel manipulation with loops (no numpy shortcuts)
# - time to measure processing time
# - matplotlib for display
#
# Outputs (as requested: 2 result images):
# - image_sortie_couleur.png
# - image_sortie_gris.png
# Plus the original saved once:
# - image_entree.png

from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt


# ================================
# 1) START TIMER
# ================================
t_debut = time.time()

# ================================
# 2) OPEN ORIGINAL (keep for reference)
# ================================
img_src = Image.open("images/Lenna512.png")
img_src.save("image_entree.png")  # keep the original always available

# ================================
# 3) NEGATIF COULEUR (RGB)
# ================================
img_rgb = img_src.convert("RGB")
image_rgb = np.array(img_rgb)

nb_lignes_rgb = image_rgb.shape[0]
nb_colonnes_rgb = image_rgb.shape[1]
print(f"[RGB] Dimensions: {nb_lignes_rgb} x {nb_colonnes_rgb} | Shape: {image_rgb.shape}")

image_sortie_rgb = np.zeros_like(image_rgb)

for i in range(nb_lignes_rgb):
    for j in range(nb_colonnes_rgb):
        r, v, b = image_rgb[i, j]
        image_sortie_rgb[i, j] = [255 - r, 255 - v, 255 - b]

Image.fromarray(image_sortie_rgb).save("image_sortie_couleur.png")

# ================================
# 4) NEGATIF GRIS (L)
# ================================
img_gray = img_src.convert("L")
image_gray = np.array(img_gray)

nb_lignes_g = image_gray.shape[0]
nb_colonnes_g = image_gray.shape[1]
print(f"[GRIS] Dimensions: {nb_lignes_g} x {nb_colonnes_g} | Shape: {image_gray.shape}")

image_sortie_gray = np.zeros_like(image_gray)

for i in range(nb_lignes_g):
    for j in range(nb_colonnes_g):
        v = image_gray[i, j]
        image_sortie_gray[i, j] = 255 - v

Image.fromarray(image_sortie_gray).save("image_sortie_gris.png")

# ================================
# 5) END TIMER
# ================================
t_fin = time.time()
print(f"Temps total de traitement: {t_fin - t_debut:.6f} secondes")

# ================================
# 6) DISPLAY (matplotlib)
# ================================
img_in = np.array(Image.open("image_entree.png").convert("RGB"))
img_out_rgb = np.array(Image.open("image_sortie_couleur.png").convert("RGB"))
img_out_gray = np.array(Image.open("image_sortie_gris.png").convert("L"))

plt.figure()
plt.title("Original (image_entree)")
plt.imshow(img_in)
plt.axis("off")

plt.figure()
plt.title("Negatif couleur (image_sortie_couleur)")
plt.imshow(img_out_rgb)
plt.axis("off")

plt.figure()
plt.title("Negatif gris (image_sortie_gris)")
plt.imshow(img_out_gray, cmap="gray")
plt.axis("off")

plt.show()
