from PIL import Image
import numpy as np

# 1) OPEN (Pillow only for loading)
img_pil = Image.open("images/6x2.png")          # mala slika za debug strukture
image = np.array(img_pil)               # numpy array: [ligne, colonne, canalRGB]

# 2) DIMENSIONS
nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]
print(f"Dimensions: {nb_lignes} lignes x {nb_colonnes} colonnes")
print(f"Shape complet: {image.shape}")  # očekuješ (2, 6, 3) ako je stvarno 6x2 RGB

# 3) PRINT pixel matrix (svaki element je [r, v, b])
print("\nTableau des pixels (triplets r,v,b):")
print(image)

# 4) EXAMPLES: kako čitati piksele (ligne, colonne)
# "Bas à gauche" znači: zadnji red (nb_lignes-1), prva kolona (0)
pixel_bas_gauche = image[nb_lignes - 1, 0]
print(f"\nPixel bas-gauche = image[{nb_lignes - 1}, 0] -> {pixel_bas_gauche}")

# "Haut à droite": prvi red (0), zadnja kolona (nb_colonnes-1)
pixel_haut_droite = image[0, nb_colonnes - 1]
print(f"Pixel haut-droite = image[0, {nb_colonnes - 1}] -> {pixel_haut_droite}")

# 5) SAVE original as image_entree.png (da original BMP/Lenna ostane netaknut)
Image.fromarray(image).save("image_entree.png")

# 6) No transformation in this exercise (just copy)
image_sortie = np.copy(image)
Image.fromarray(image_sortie).save("image_sortie.png")

print("\nOK: saved image_entree.png and image_sortie.png")
