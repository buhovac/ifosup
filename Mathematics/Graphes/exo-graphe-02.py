'''
Écrivez un programme qui soustrait d'une ligne k un multiple d'une autre ligne
d'une matrice (transvection: Lk = Lk – alpha.Li )
et qui sera appelé par l'instruction nom-fonction(A,k,i,alpha)
où A est le nom de la matrice et k et i le numéro des lignes à soustraire
et alpha le facteur de multiplication de la ième ligne avant soustraction
'''

import random

def create_random_int_matrix(rows, cols, min_val=0, max_val=9):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = random.randint(min_val, max_val)
            row.append(value)
        matrix.append(row)
    return matrix

def transvection(A, k, i, alpha):
    # Lk = Lk - alpha * Li
    for col in range(len(A[k])):
        A[k][col] = A[k][col] - alpha * A[i][col]
    return A

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:6.2f}", end=" ")
        print()

def main():
    rows = int(input("Saisissez le nombre de lignes: "))
    cols = int(input("Saisissez le nombre de colonnes: "))

    matrix = create_random_int_matrix(rows, cols)

    print("\nMatrice originale:")
    print_matrix(matrix)

    k = int(input(f"\nIndice de la ligne k à modifier (0 à {rows-1}): "))
    i = int(input(f"Indice de la ligne i utilisée (0 à {rows-1}): "))
    alpha = float(input("Valeur de alpha: "))

    matrix_after = transvection(matrix, k, i, alpha)

    print("\nMatrice après transvection (Lk = Lk - alpha * Li):")
    print_matrix(matrix_after)

if __name__ == "__main__":
    main()
