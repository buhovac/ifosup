import numpy as np

n = int(input("Dimension n×n: "))
p = int(input("Puissance p: "))

A = np.random.randint(0, 5, size=(n, n))

print("A:\n", A)
print(f"A^{p} :\n", np.linalg.matrix_power(A, p))
