"""
Exercice 1
En Python, créer un programme qui génère une matrice aléatoire
dont les éléments sont des entiers et une autre où ce sont des réels.

La taille de la matrice est entrée au clavier.
Le résultat est affiché proprement à l’écran.
"""
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


def create_random_float_matrix(rows, cols, min_val=0.0, max_val=10.0):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = random.uniform(min_val, max_val)
            row.append(value)
        matrix.append(row)
    return matrix


def print_matrix(matrix, is_float=False):
    for row in matrix:
        line_parts = []
        for value in row:
            if is_float:
                line_parts.append(f"{value:6.2f}")
            else:
                line_parts.append(f"{value:4d}")
        print(" ".join(line_parts))


def main():
    rows = int(input("Saisissez le nombre de lignes.: "))
    cols = int(input("Saisissez le nombre de colonnes.: "))

    int_matrix = create_random_int_matrix(rows, cols, min_val=0, max_val=9)
    float_matrix = create_random_float_matrix(rows, cols, min_val=0.0, max_val=10.0)

    print("\nMatrice entiers:")
    print_matrix(int_matrix, is_float=False)

    print("\nMatrice réels:")
    print_matrix(float_matrix, is_float=True)


if __name__ == "__main__":
    main()
