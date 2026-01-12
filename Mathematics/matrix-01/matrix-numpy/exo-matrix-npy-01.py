import numpy as np

rows = int(input("Rows: "))
cols = int(input("Cols: "))

A_int = np.random.randint(0, 10, size=(rows, cols))
A_float = np.random.random(size=(rows, cols))

print("Integer matrix:\n", A_int)
print("Float matrix:\n", A_float)
