# ex2-7.py
# Exercice 2.7 — Mise en nuance de gris (luminance pondérée)
#
# Contraintes respectées:
# - Pillow = uniquement open/save
# - numpy = manipulation manuelle des pixels (boucles)
# - time = mesure du temps
# - matplotlib = affichage
#
# Entrée :  images/Lenna512.png
# Sorties :
# - image_entree.png
# - image_sortie.png

from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt

# Coefficients officiels (Wikipedia)
A = 0.2126
B = 0.7152
C = 0.0722

# ================================
# 1) TIMER START
# ================================
t_debut = time.time()

# ================================
# 2) OUVERTURE IMAGE (RGB)
# ================================
img_src = Image.open("images/Lenna512.png").convert("RGB")
image = np.array(img_src)

nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]
print(f"Dimensions: {nb_lignes} x {nb_colonnes} | Shape: {image.shape}")

Image.fromarray(image).save("image_entree.png")

# ================================
# 3) TRAITEMENT : NIVEAUX DE GRIS (LUMINANCE)
# ================================
image_sortie = np.zeros_like(image)

for i in range(nb_lignes):
    for j in range(nb_colonnes):
        r, v, b = image[i, j]

        # calcul de la luminance (float)
        luminance = A * r + B * v + C * b

        # normalisation 0..255 + conversion en entier
        lum = int(np.clip(luminance, 0, 255))

        # même valeur sur R, V et B
        image_sortie[i, j] = [lum, lum, lum]

Image.fromarray(image_sortie).save("image_sortie.png")

# ================================
# 4) TIMER END
# ================================
t_fin = time.time()
print(f"Temps de traitement: {t_fin - t_debut:.6f} secondes")

# ================================
# 5) AFFICHAGE (MATPLOTLIB)
# ================================
img_in  = np.array(Image.open("image_entree.png"))
img_out = np.array(Image.open("image_sortie.png"))

plt.figure()
plt.title("Original")
plt.imshow(img_in)
plt.axis("off")

plt.figure()
plt.title("Nuance de gris (luminance)")
plt.imshow(img_out, cmap="gray")
plt.axis("off")

plt.show()
