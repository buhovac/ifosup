import numpy as np

rowsA = int(input("Rows A: "))
colsA = int(input("Cols A: "))
rowsB = int(input("Rows B: "))
colsB = int(input("Cols B: "))

if colsA != rowsB:
    print("Error!")
else:
    A = np.random.randint(0, 10, size=(rowsA, colsA))
    B = np.random.randint(0, 10, size=(rowsB, colsB))

    print("A:\n", A)
    print("B:\n", B)
    print("A × B =\n", A @ B)
