def convolution(image, kernel):
    nb_lignes = len(image)
    nb_colonnes = len(image[0])

    result = [[0 for _ in range(nb_colonnes)] for _ in range(nb_lignes)]

    for ligne in range(1, nb_lignes - 1):
        for col in range(1, nb_colonnes - 1):

            somme = 0
            for i in range(3):
                for j in range(3):
                    somme += kernel[i][j] * image[ligne - 1 + i][col - 1 + j]

            result[ligne][col] = somme

    for i in range(nb_lignes):
        result[i][0] = image[i][0]
        result[i][nb_colonnes - 1] = image[i][nb_colonnes - 1]

    for j in range(nb_colonnes):
        result[0][j] = image[0][j]
        result[nb_lignes - 1][j] = image[nb_lignes - 1][j]

    return result


def print_matrix(matrix, title=""):
    if title:
        print(title)
    for row in matrix:
        for value in row:
            print(f"{value:6.2f}", end=" ")
        print()
    print()


def main():
    image = [
        [2, 1, 3, 0],
        [1, 1, 0, 5],
        [3, 3, 1, 0],
        [2, 0, 0, 2]
    ]

    kernel = [
        [1, 0, 2],
        [2, 1, 0],
        [1, 0, 3]
    ]

    print_matrix(image, "Image originale:")
    print_matrix(kernel, "Masque (kernel):")

    result = convolution(image, kernel)

    print_matrix(result, "Image après convolution:")


if __name__ == "__main__":
    main()
