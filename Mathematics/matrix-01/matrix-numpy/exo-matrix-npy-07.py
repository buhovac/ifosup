import numpy as np

rows = int(input("Rows: "))
cols = int(input("Cols: "))

A = np.random.randint(0, 10, size=(rows, cols))

sums1 = A.sum(axis=1)

U = np.ones((cols, 1))
sums2 = (A @ U).flatten()

print("A:\n", A)
print("Sum row (sum axis=1):", sums1)
print("Sum row (A×U):", sums2)
