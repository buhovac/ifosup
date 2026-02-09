# ex2-6.py
# Exercice 2.6 — Isoler les composantes R, V, B + exemple de modification colorimétrique
#
# Contraintes respectées:
# - Pillow = uniquement open/save
# - numpy = manipulation manuelle des pixels (boucles)
# - time = mesure du temps
# - matplotlib = affichage
#
# Sorties produites:
# - image_entree.png           (original)
# - image_sortie_rouge.png
# - image_sortie_vert.png
# - image_sortie_bleu.png
# - image_sortie_colorimetrie.png   (exemple (0.8, 1, 0.95))

from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt

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

# sauvegarde de référence
Image.fromarray(image).save("image_entree.png")

# ================================
# 3) ALLOCATION DES SORTIES
# ================================
img_rouge = np.zeros_like(image)
img_vert  = np.zeros_like(image)
img_bleu  = np.zeros_like(image)

# coefficients pour modification colorimétrique (exemple du cours)
coef = np.array([0.8, 1.0, 0.95], dtype=float)
img_color = np.zeros_like(image, dtype=float)  # temporaire en float

# ================================
# 4) TRAITEMENTS PIXEL PAR PIXEL
# ================================
for i in range(nb_lignes):
    for j in range(nb_colonnes):
        r, v, b = image[i, j]

        # --- isolation des couleurs ---
        img_rouge[i, j] = [r, 0, 0]
        img_vert[i, j]  = [0, v, 0]
        img_bleu[i, j]  = [0, 0, b]

        # --- modification colorimétrique (multiplication par réel) ---
        img_color[i, j] = [r*coef[0], v*coef[1], b*coef[2]]

# conversion float -> int 0..255 (obligatoire)
img_color = np.clip(img_color, 0, 255).astype(np.uint8)

# ================================
# 5) SAUVEGARDES
# ================================
Image.fromarray(img_rouge).save("image_sortie_rouge.png")
Image.fromarray(img_vert).save("image_sortie_vert.png")
Image.fromarray(img_bleu).save("image_sortie_bleu.png")
Image.fromarray(img_color).save("image_sortie_colorimetrie.png")

# ================================
# 6) TIMER END
# ================================
t_fin = time.time()
print(f"Temps total: {t_fin - t_debut:.6f} secondes")

# ================================
# 7) AFFICHAGE (MATPLOTLIB)
# ================================
img_in  = np.array(Image.open("image_entree.png"))
img_r   = np.array(Image.open("image_sortie_rouge.png"))
img_v   = np.array(Image.open("image_sortie_vert.png"))
img_b   = np.array(Image.open("image_sortie_bleu.png"))
img_col = np.array(Image.open("image_sortie_colorimetrie.png"))

plt.figure(); plt.title("Original"); plt.imshow(img_in); plt.axis("off")
plt.figure(); plt.title("Composante ROUGE"); plt.imshow(img_r); plt.axis("off")
plt.figure(); plt.title("Composante VERTE"); plt.imshow(img_v); plt.axis("off")
plt.figure(); plt.title("Composante BLEUE"); plt.imshow(img_b); plt.axis("off")
plt.figure(); plt.title("Colorimétrie (0.8,1,0.95)"); plt.imshow(img_col); plt.axis("off")

plt.show()
