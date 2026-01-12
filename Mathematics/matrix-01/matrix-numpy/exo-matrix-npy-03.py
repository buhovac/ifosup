import numpy as np

rows = int(input("Rows: "))
cols = int(input("Cols: "))

print("Matrice A:")
A = np.array([[int(input(f"A[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)])

print("Matrice B:")
B = np.array([[int(input(f"B[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)])

print("A + B =\n", A + B)
print("A - B =\n", A - B)
