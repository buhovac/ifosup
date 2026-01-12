'''
Écrivez un programme qui inverse deux lignes d'une matrice
 et qui sera appelé par l'instruction nom-fonction(A,i,j)
 où A est le nom de la matrice et i et j le numéro des lignes à échanger
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

def swap_lines(A, i, j):
    # Zamjena dvaju redaka (Python way)
    A[i], A[j] = A[j], A[i]
    return A

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:4d}", end=" ")
        print()

def main():
    rows = int(input("Saisissez le nombre de lignes: "))
    cols = int(input("Saisissez le nombre de colonnes: "))

    int_matrix = create_random_int_matrix(rows, cols, 0, 9)

    print("\nMatrice originale:")
    print_matrix(int_matrix)

    # Tražimo koje linije zamijeniti
    i = int(input(f"\nIndice de la première ligne à échanger (0 à {rows-1}) : "))
    j = int(input(f"Indice de la deuxième ligne à échanger (0 à {rows-1}) : "))

    matrix_swap = swap_lines(int_matrix, i, j)

    print("\nMatrice après échange:")
    print_matrix(matrix_swap)

if __name__ == "__main__":
    main()
