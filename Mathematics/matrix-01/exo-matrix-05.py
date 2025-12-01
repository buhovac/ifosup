'''
En Python, créer un programme qui exécute le produit d’une matrice aléatoire par un scalaire entré au clavier.
La matrice de départ, le scalaire et le produit sont affichés à l’écran.
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

def produit_scalaire(A, scalaire):
    rows = len(A)
    cols = len(A[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] * scalaire)
        result.append(row)
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value:4d}" for value in row))


def main():
    rows = int(input("Saisissez le nombre de lignes: "))
    cols = int(input("Saisissez le nombre de colonnes: "))

    scalaire = int(input("Saisissez un nombre scalaire: "))

    A = create_random_matrix(rows, cols)
    B = produit_scalaire(A, scalaire)

    print("\nMatrice :")
    print_matrix(A)

    print("\nLe produit d’une matrice aléatoire par un scalaire :")
    print_matrix(B)

if __name__ == "__main__":
    main()