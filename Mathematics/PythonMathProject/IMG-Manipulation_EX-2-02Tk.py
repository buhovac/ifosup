from PIL import Image
import numpy as np
import time
import matplotlib.pyplot as plt

# ================================
# 1) START TIMER
# ================================
t_debut = time.time()

# ================================
# 2) OPEN
# ================================
img_pil = Image.open("images/6x2.png").convert("RGB")
image = np.array(img_pil)

nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]
print(f"Dimensions: {nb_lignes} lignes x {nb_colonnes} colonnes")
print(f"Shape complet: {image.shape}")

# Save original
Image.fromarray(image).save("image_entree.png")

# ================================
# 3) TRAITEMENT (ici: copie)
# ================================
image_sortie = np.copy(image)

# Save result
Image.fromarray(image_sortie).save("image_sortie.png")

# ================================
# 4) END TIMER
# ================================
t_fin = time.time()
print(f"Temps de traitement: {t_fin - t_debut:.6f} secondes")

# ================================
# 5) DISPLAY (matplotlib)
# ================================
img_in = np.array(Image.open("image_entree.png").convert("RGB"))
img_out = np.array(Image.open("image_sortie.png").convert("RGB"))

plt.figure()
plt.title("image_entree.png")
plt.imshow(img_in)
plt.axis("off")

plt.figure()
plt.title("image_sortie.png")
plt.imshow(img_out)
plt.axis("off")

plt.show()
