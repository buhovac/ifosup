import numpy as np

rows = int(input("Rows: "))
cols = int(input("Cols: "))
k = float(input("Scalaire: "))

A = np.random.randint(0, 10, size=(rows, cols))

print("A:\n", A)
print("kA:\n", k * A)
