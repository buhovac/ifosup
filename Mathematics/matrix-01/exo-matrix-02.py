"""
En Python, créer un programme qui génère une matrice unité, une matrice diagonale,
une matrice triangulaire, une matrice creuse, une matrice nulle.
La taille de la matrice est entrée au clavier.
"""
def create_zero_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix