'''
Écrivez un programme qui calcule le déterminant d’une matrice par la méthode du pivot de Gauss-Jordan
(vous aurez besoin des programmes des exercices 1 et 2 sous forme de fonction)
'''
import random

def create_random_int_matrix(n, min_val=0, max_val=9):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix

def swap_lines(A, i, j):
    print(f"\nÉchange des lignes {i} et {j}")
    A[i], A[j] = A[j], A[i]

def transvection(A, k, i, alpha):
    print(f"Transvection: L{k} = L{k} - {alpha} * L{i}")
    for col in range(len(A[k])):
        A[k][col] = A[k][col] - alpha * A[i][col]

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:8.2f}", end=" ")
        print()

def determinant_gauss_jordan(A):
    n = len(A)
    det = 1.0

    print("\nMatrice originale:")
    print_matrix(A)

    for j in range(n):
        print(f"\n--- Colonne {j} ---")

        pivot_row = j
        while pivot_row < n and A[pivot_row][j] == 0:
            pivot_row += 1

        if pivot_row == n:
            print("Pivot nul → déterminant = 0")
            return 0

        if pivot_row != j:
            swap_lines(A, pivot_row, j)
            det *= -1
            print("Matrice après échange:")
            print_matrix(A)

        pivot = A[j][j]
        print(f"Pivot choisi: A[{j}][{j}] = {pivot}")

        for i in range(j + 1, n):
            alpha = A[i][j] / pivot
            transvection(A, i, j, alpha)

        print("\nMatrice après élimination:")
        print_matrix(A)

    print("\nMatrice triangulaire finale:")
    print_matrix(A)

    for i in range(n):
        det *= A[i][i]

    return det

def main():
    n = int(input("Saisissez la dimension de la matrice carrée (n): "))

    A = create_random_int_matrix(n, 0, 5)

    det = determinant_gauss_jordan(A)

    print(f"\nDéterminant de la matrice = {det}")

if __name__ == "__main__":
    main()
