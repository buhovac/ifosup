'''
En Python, créer un programme qui calcule et affiche la somme des lignes
d’une matrice aléatoire de deux manières différentes.
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

def somme_des_lignes(A):
    rows = len(A)
    cols = len(A[0])

    sums = []
    for i in range(rows):
        total = 0
        for j in range(cols):
            total += A[i][j]
        sums.append(total)
    return sums

def somme_des_lignes_deuxieme(A):
    rows = len(A)
    cols = len(A[0])

    sums = []
    for i in range(rows):
        total = 0
        for j in range(cols):
            total += A[i][j]
        sums.append(total)
    return sums

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


def create_column_of_ones(n):
    return [[1] for _ in range(n)]


def main():
    rows = int(input("Saisissez le nombre de lignes: "))
    cols = int(input("Saisissez le nombre de colonnes: "))


    A = create_random_matrix(rows, cols)
    B = somme_des_lignes(A)

    U = create_column_of_ones(cols)
    C = produit_matrices(A, U)


    print("\nMatrice :")
    print_matrix(A)

    print("\nMatrice :")
    print_matrix(C)

    print("\nLa somme des lignes :", B)

if __name__ == "__main__":
    main()