from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt

# ================================
# 1) START TIMER
# ================================
t_debut = time.time()

# ================================
# 2) OUVERTURE DE L’IMAGE
# ================================
img_pil = Image.open("images/Lenna512.png").convert("RGB")
image = np.array(img_pil)

nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]

print(f"Dimensions: {nb_lignes} lignes x {nb_colonnes} colonnes")
print(f"Shape complet: {image.shape}")

# Spremi original za usporedbu
Image.fromarray(image).save("image_entree.png")

# ================================
# 3) TRAITEMENT : CROP (ZONE DU REGARD)
# ================================
# Profesorov primjer:
# lignes 240 -> 289  (jer 290 nije uključeno)
# colonnes 240 -> 359 (jer 360 nije uključeno)

image_sortie = image[240:290, 240:360]

print("\nNouvelle zone découpée:")
print(f"Shape sortie = {image_sortie.shape}")

# Spremi rezultat
Image.fromarray(image_sortie).save("image_sortie.png")

# ================================
# 4) END TIMER
# ================================
t_fin = time.time()
print(f"Temps de traitement: {t_fin - t_debut:.6f} secondes")

# ================================
# 5) AFFICHAGE AVEC MATPLOTLIB
# ================================

img_in = np.array(Image.open("image_entree.png"))
img_out = np.array(Image.open("image_sortie.png"))

plt.figure()
plt.title("Image d'origine (image_entree)")
plt.imshow(img_in)
plt.axis("off")

plt.figure()
plt.title("Zone découpée (image_sortie)")
plt.imshow(img_out)
plt.axis("off")

plt.show()
