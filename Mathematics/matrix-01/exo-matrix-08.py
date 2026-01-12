'''
En Python, créer un programme qui calcule et affiche la somme des colonnes
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


def somme_des_colonnes(A):
    rows = len(A)
    cols = len(A[0])

    sums = []
    for j in range(cols):
        total = 0
        for i in range(rows):
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
            s = 0
            for k in range(cols):
                s += A[i][k] * B[k][j]
            row.append(s)
        result.append(row)
    return result


def create_row_of_ones(m):
    return [[1 for _ in range(m)]]


def somme_des_colonnes_par_produit(A):
    rows = len(A)
    V = create_row_of_ones(rows)
    S = produit_matrices(V, A)
    return S[0]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value:4d}" for value in row))


def main():
    rows = int(input("Saisissez le nombre de lignes: "))
    cols = int(input("Saisissez le nombre de colonnes: "))

    A = create_random_matrix(rows, cols)

    sums1 = somme_des_colonnes(A)

    sums2 = somme_des_colonnes_par_produit(A)

    print("\nMatrice A :")
    print_matrix(A)

    print("\nSomme des colonnes (méthode 1 - boucles):")
    print(sums1)

    print("\nSomme des colonnes (méthode 2 - produit matriciel V × A):")
    print(sums2)


if __name__ == "__main__":
    main()
