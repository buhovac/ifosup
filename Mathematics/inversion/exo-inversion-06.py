def swap_lines(A, i, j):
    if i == j:
        return
    A[i], A[j] = A[j], A[i]

def transvection(A, k, i, alpha):
    for col in range(len(A[k])):
        A[k][col] = A[k][col] - alpha * A[i][col]

def scale_row(A, k, divisor):
    for col in range(len(A[k])):
        A[k][col] = A[k][col] / divisor

def print_matrix(matrix, title=None):
    if title:
        print(title)
    for row in matrix:
        print(" ".join(f"{v:10.4f}" for v in row))
    print()

def augment_with_identity(A):
    n = len(A)
    aug = []
    for i in range(n):
        left = [float(x) for x in A[i]]
        right = [0.0] * n
        right[i] = 1.0
        aug.append(left + right)
    return aug

def extract_inverse(aug):
    n = len(aug)
    return [row[n:] for row in aug]

def gauss_jordan_inverse(A, eps=1e-12, verbose=False):
    n = len(A)
    if n == 0 or any(len(row) != n for row in A):
        raise ValueError("La matrice doit être carrée (n x n).")

    aug = augment_with_identity(A)
    if verbose:
        print_matrix(aug, "Matrice augmentée initiale [A | I]:")

    r = 0
    for j in range(n):
        # pivot partiel: max(|A[i,j]|) sur i = r..n-1
        k = r
        max_val = abs(aug[r][j]) if r < n else 0.0
        for i in range(r + 1, n):
            v = abs(aug[i][j])
            if v > max_val:
                max_val = v
                k = i

        if max_val < eps:
            continue

        if k != r:
            swap_lines(aug, k, r)
            if verbose:
                print_matrix(aug, f"Après échange L{k} <-> L{r}:")

        pivot = aug[r][j]
        if abs(pivot) < eps:
            continue

        scale_row(aug, r, pivot)
        if verbose:
            print_matrix(aug, f"Après normalisation (pivot -> 1) ligne {r}:")

        for i in range(n):
            if i == r:
                continue
            factor = aug[i][j]
            if abs(factor) > eps:
                transvection(aug, i, r, factor)

        if verbose:
            print_matrix(aug, f"Après élimination colonne {j}:")

        r += 1
        if r == n:
            break

    # provjera lijevo = I
    for i in range(n):
        for j in range(n):
            expected = 1.0 if i == j else 0.0
            if abs(aug[i][j] - expected) > 1e-8:
                raise ValueError("Matrice non inversible (det = 0).")

    return extract_inverse(aug)

def matmul(A, B):
    p, q = len(A), len(A[0])
    if len(B) != q:
        raise ValueError("Dimensions incompatibles pour multiplication.")
    r = len(B[0])
    C = [[0.0 for _ in range(r)] for _ in range(p)]
    for i in range(p):
        for k in range(q):
            aik = A[i][k]
            for j in range(r):
                C[i][j] += aik * B[k][j]
    return C

def main():
    # Ordre des inconnues: [m, q, v, h, n]
    A = [
        [1, 2, 1, 0, 0],
        [2, 1, 1, 1, 0],
        [1, 0, 2, 2, 1],
        [2, 2, 1, 1, 3],
        [1, 0, 0, 2, 2],
    ]
    b = [
        [55.0],
        [65.5],
        [80.0],
        [117.5],
        [63.5],
    ]

    print_matrix(A, "Matrice A (coefficients):")
    print_matrix(b, "Vecteur b (totaux):")

    show_steps = input("Afficher les étapes Gauss-Jordan ? (o/n): ").strip().lower() == "o"

    A_inv = gauss_jordan_inverse(A, verbose=show_steps)
    X = matmul(A_inv, b)

    names = ["Margherita (m)", "Quatre-saisons (q)", "Végétarienne (v)", "Hawaïenne (h)", "Napolitaine (n)"]

    print_matrix(A_inv, "Matrice inverse A^-1:")
    print_matrix(X, "Solution X:")

    print("=== Prix des pizzas ===")
    for name, val in zip(names, [X[i][0] for i in range(5)]):
        # mali cleanup
        if abs(val) < 1e-10:
            val = 0.0
        print(f"{name:20s} = {val:.2f} €")

    print("\nVérification rapide (ex: ami 1): m + 2q + v = 55")
    m, q, v, h, n = [X[i][0] for i in range(5)]
    check1 = m + 2*q + v
    print(f"{m:.2f} + 2*{q:.2f} + {v:.2f} = {check1:.2f}")

if __name__ == "__main__":
    main()
