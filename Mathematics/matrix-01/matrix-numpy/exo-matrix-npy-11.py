import numpy as np

rows = int(input("Rows: "))
cols = int(input("Cols: "))

A = np.random.randint(0, 10, size=(rows, cols))

print("A:\n", A)
print("A^T:\n", A.T)
