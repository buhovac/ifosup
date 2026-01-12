import numpy as np

rows = int(input("Rows: "))
cols = int(input("Cols: "))

A = np.array([[int(input(f"A[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)])
B = np.array([[int(input(f"B[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)])

C = A * B

print("A:\n", A)
print("B:\n", B)
print("Hadamard A ⊙ B:\n", C)
