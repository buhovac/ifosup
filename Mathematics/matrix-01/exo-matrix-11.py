'''
En Python, créer un programme qui calcule et affiche la transposée d’une matrice aléatoire.
La matrice de départ et sa transposée sont affichées à l’écran.
'''

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


def transpose_matrix(A):
    rows = len(A)
    cols = len(A[0])

    T = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(A[i][j])
        T.append(row)
    return T


def print_matrix(matrix, name="M"):
    print(f"\nMatrice {name}:")
    for row in matrix:
        print(" ".join(f"{value:4d}" for value in row))


def main():
    rows = int(input("Saisissez le nombre de lignes: "))
    cols = int(input("Saisissez le nombre de colonnes: "))

    A = create_random_matrix(rows, cols)

    T = transpose_matrix(A)

    print_matrix(A, "A (original)")
    print_matrix(T, "Aᵀ (transposée)")

if __name__ == "__main__":
    main()
