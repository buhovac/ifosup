import numpy as np

rows = int(input("Rows: "))
cols = int(input("Cols: "))

A = np.random.randint(-9, 10, size=(rows, cols))
opposite = -A

print("A:\n", A)
print("-A:\n", opposite)
print("A + (-A):\n", A + opposite)
