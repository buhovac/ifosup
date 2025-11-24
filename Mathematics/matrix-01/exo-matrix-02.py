"""
En Python, créer un programme qui génère une matrice unité, une matrice diagonale,
une matrice triangulaire, une matrice creuse, une matrice nulle.
La taille de la matrice est entrée au clavier.
"""
import random

def create_zero_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)
    return matrix


def create_identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(1 if i == j else 0)
        matrix.append(row)
    return matrix


def create_diagonal_matrix(n, min_val=1, max_val=9):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(random.randint(min_val, max_val))
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def create_upper_triangular_matrix(rows, cols, min_val=1, max_val=9):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if i <= j:
                row.append(random.randint(min_val, max_val))
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def create_sparse_matrix(rows, cols, density=0.2):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if random.random() < density:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value:4d}" for value in row))


def main():
    rows = int(input("Saisissez le nombre de lignes: "))
    cols = int(input("Saisissez le nombre de colonnes: "))

    print("\nMatrice nulle:")
    print_matrix(create_zero_matrix(rows, cols))

    if rows == cols:
        print("\nMatrice unité:")
        print_matrix(create_identity_matrix(rows))
    else:
        print("\nUne matrice unité ne peut être créée que lorsque la matrice est carrée.!")

    if rows == cols:
        print("\nMatrice diagonale:")
        print_matrix(create_diagonal_matrix(rows))
    else:
        print("\nLes matrices diagonales ne peuvent être construites que lorsque la matrice est carrée.!")

    print("\nMatrice triangulaire:")
    print_matrix(create_upper_triangular_matrix(rows, cols))

    sparse_matrix = create_sparse_matrix(rows, cols, density=0.2)
    print("\nMatrice creuse:")
    print_matrix(sparse_matrix)


if __name__ == "__main__":
    main()
