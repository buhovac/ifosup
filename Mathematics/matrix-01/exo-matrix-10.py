'''
En Python, créer un programme qui exécute le produit de Hadamard de deux matrices.
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


def hadamard_product(A, B):
    rows = len(A)
    cols = len(A[0])

    C = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] * B[i][j])
        C.append(row)
    return C


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

    C = hadamard_product(A, B)

    print_matrix(A, "A")
    print_matrix(B, "B")
    print_matrix(C, "A B")


if __name__ == "__main__":
    main()
