# ex2-6b.py
# Exercice 2.6b — Isoler une couleur à partir d’un seuil (seuil sur la composante ROUGE)
#
# Input:  images/4-2-03.png
# Objectif: mettre en NOIR les pixels dont R < seuil
#           conserver (ou forcer à 255) les pixels dont R >= seuil
# Ici: on FORCE le rouge à 255 (et V,B à 0) pour visualiser clairement la zone.
#
# Sorties:
# - image_entree.png
# - image_sortie.png

from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt

SEUIL_ROUGE = 220  # demandé

# ================================
# 1) START TIMER
# ================================
t_debut = time.time()

# ================================
# 2) OPEN IMAGE (RGB)
# ================================
img_src = Image.open("images/4-2-03.png").convert("RGB")
image = np.array(img_src)

nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]
print(f"Dimensions: {nb_lignes} x {nb_colonnes} | Shape: {image.shape}")
print(f"Seuil rouge = {SEUIL_ROUGE}")

# Save original (per conventions)
Image.fromarray(image).save("image_entree.png")

# ================================
# 3) TRAITEMENT : SEUIL SUR ROUGE
# ================================
image_sortie = np.zeros_like(image)

# Variante choisie:
# - si R < seuil => noir [0,0,0]
# - si R >= seuil => rouge forcé [255,0,0] (met en évidence la zone)
for i in range(nb_lignes):
    for j in range(nb_colonnes):
        r, v, b = image[i, j]
        if r < SEUIL_ROUGE:
            image_sortie[i, j] = [0, 0, 0]
        else:
            image_sortie[i, j] = [255, 0, 0]

# Save result
Image.fromarray(image_sortie).save("image_sortie.png")

# ================================
# 4) END TIMER
# ================================
t_fin = time.time()
print(f"Temps de traitement: {t_fin - t_debut:.6f} secondes")

# ================================
# 5) DISPLAY (MATPLOTLIB)
# ================================
img_in = np.array(Image.open("image_entree.png").convert("RGB"))
img_out = np.array(Image.open("image_sortie.png").convert("RGB"))

plt.figure()
plt.title("Original (image_entree)")
plt.imshow(img_in)
plt.axis("off")

plt.figure()
plt.title(f"Seuil rouge >= {SEUIL_ROUGE} (image_sortie)")
plt.imshow(img_out)
plt.axis("off")

plt.show()
