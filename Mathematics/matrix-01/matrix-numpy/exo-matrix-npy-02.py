import numpy as np

n = int(input("Dimenzija matrice: "))

identity = np.eye(n)
diagonal = np.diag(np.random.randint(1, 10, size=n))
upper_triangular = np.triu(np.random.randint(0, 10, size=(n, n)))
sparse = np.random.choice([0, 1], size=(n, n), p=[0.8, 0.2])
zero = np.zeros((n, n))

print("unité:\n", identity)
print("diagonale:\n", diagonal)
print("triangulaire:\n", upper_triangular)
print("creuse:\n", sparse)
print("nulle:\n", zero)
