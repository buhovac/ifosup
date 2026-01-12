'''
En Python, créer un programme qui calcule et affiche la nème puissance
d’une matrice carrée aléatoire de manière économique
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

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value:4d}" for value in row))


def main():
    rows = int(input("Saisissez le nombre de lignes: "))
    cols = int(input("Saisissez le nombre de colonnes: "))

    puissance = int(input("Saisissez un nombre puissance: "))

    A = create_random_matrix(rows, cols)
    B = A
    C = produit_matrices(A, B)

    print("\nMatrice :")
    print_matrix(A)

    print("\nLe produit d’une matrice aléatoire par un puissance :")
    print_matrix(C)

if __name__ == "__main__":
    main()