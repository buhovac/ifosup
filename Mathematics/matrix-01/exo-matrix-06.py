'''
En Python, créer un programme qui exécute le produit de deux matrices.
Les matrices sont entrées au clavier élément par élément.
Leur compatibilité est vérifiée avant d’introduire tous les éléments.
Les matrices de départ et le produit sont affichés à l’écran.

'''

def read_matrix(rows, cols, name="A"):
    print(f"\nEntrée matricielle {name}:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Saisissez un élément {name}[{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

def produit_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    cols2 = len(B[0])

    result = []
    for i in range(rows):
        row = []
        for j in range(cols2):
            sum = 0
            for k in range(cols):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        result.append(row)
    return result

def print_matrix(matrix, name="M"):
    print(f"\nMatrice {name}:")
    for row in matrix:
        print(" ".join(f"{value:4d}" for value in row))


def main():
    # Dimensions de la première matrice
    rows1 = int(input("Saisissez le nombre de lignes de la première matrice: "))
    cols1 = int(input("Saisissez le nombre de colonnes de la première matrice: "))

    # Dimensions de la deuxième matrice
    rows2 = int(input("Saisissez le nombre de lignes de la deuxième matrice: "))
    cols2 = int(input("Saisissez le nombre de colonnes de la deuxième matrice: "))

    # Vérification de compatibilité
    if cols1 != rows2:
        print("\nProduit est impossible : numero de colones matrice A doit etre >= a nombre de lignes de B.")
        return

    A = read_matrix(rows1, cols1, name="A")
    B = read_matrix(rows2, cols2, name="B")

    D = produit_matrices(A, B)

    print_matrix(A, "A")
    print_matrix(B, "B")
    print_matrix(D, "A * B")


if __name__ == "__main__":
    main()