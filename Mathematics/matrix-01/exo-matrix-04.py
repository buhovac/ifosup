"""
En Python, créer un programme qui crée une matrice aléatoire,
qui calcule ensuite son opposée,
affiche les deux matrices et qui vérifie que leur somme fait bien une Matrice nulle.
"""

import random

def create_random_matrix(rows, cols, min_val=0, max_val=9):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = random.randint(min_val, max_val)
            row.append(value)
        matrix.append(row)
    return matrix

def opposite_matrix(A):
    rows = len(A)
    cols = len(A[0])

    opposite = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(-A[i][j])
        opposite.append(row)
    return opposite

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


def print_matrix(matrix, name="M"):
    print(f"\nMatrice {name}:")
    for row in matrix:
        print(" ".join(f"{value:4d}" for value in row))


def is_zero_matrix(M):
    for row in M:
        for value in row:
            if value != 0:
                return False
    return True

def main():

    rows = 3
    cols = 4

    A = create_random_matrix(rows, cols)

    A_opposite = opposite_matrix(A)

    print_matrix(A, "A")
    print_matrix(A_opposite, "-A")

    S = add_matrices(A, A_opposite)
    print_matrix(S, "A + (-A)")

    if is_zero_matrix(S):
        print("\nVérification réussie : A + (-A) est bien une matrice nulle.")
    else:
        print("\nErreur : le résultat n'est pas une matrice nulle !")


if __name__ == "__main__":
    main()