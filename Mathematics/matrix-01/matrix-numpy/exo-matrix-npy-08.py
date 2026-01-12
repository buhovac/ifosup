import numpy as np

rows = int(input("Rows: "))
cols = int(input("Cols: "))

A = np.random.randint(0, 10, size=(rows, cols))

sums1 = A.sum(axis=0)

V = np.ones((1, rows))
sums2 = (V @ A).flatten()

print("A:\n", A)
print("Sum col (sum axis=0):", sums1)
print("Sum col (V×A):", sums2)
