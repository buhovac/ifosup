"""
En Python, créer un programme qui additionne/soustrait deux matrices
après avoir vérifié que l’addition est possible.
Les matrices sont entrées au clavier élément par élément.
"""

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


def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


def subtract_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] - B[i][j])
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
    if rows1 != rows2 or cols1 != cols2:
        print("\nL'addition/soustraction est impossible : les matrices n'ont pas les mêmes dimensions.")
        return

    A = read_matrix(rows1, cols1, name="A")
    B = read_matrix(rows2, cols2, name="B")

    S = add_matrices(A, B)
    D = subtract_matrices(A, B)

    print_matrix(A, "A")
    print_matrix(B, "B")
    print_matrix(S, "A + B")
    print_matrix(D, "A - B")


if __name__ == "__main__":
    main()
