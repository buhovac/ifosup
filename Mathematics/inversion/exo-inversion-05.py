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
        # Chercher max(|A[i,j]|) sur i = r..n-1
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
            print_matrix(aug, f"Après normalisation (pivot -> 1) sur ligne {r}:")

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

    # Vérifier que la partie gauche est I
    for i in range(n):
        for j in range(n):
            expected = 1.0 if i == j else 0.0
            if abs(aug[i][j] - expected) > 1e-8:
                raise ValueError("Matrice non inversible (det = 0).")

    return extract_inverse(aug)

def matmul(A, B):
    # A: p×q, B: q×r
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

def read_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v <= 0:
                print("Veuillez entrer un entier positif.")
                continue
            return v
        except ValueError:
            print("Entrée invalide. Veuillez entrer un entier.")

def read_float(prompt):
    while True:
        s = input(prompt).strip().replace(",", ".")
        try:
            return float(s)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

def solve_linear_system_interactive():
    print("=== Résolution d’un système AX = b (via inversion Gauss-Jordan) ===")

    # 1) Demander nb variables / équations + boucle si différent
    while True:
        n_vars = read_int("Combien de variables ? ")
        n_eqs = read_int("Combien d'équations ? ")
        if n_vars != n_eqs:
            print("Erreur : le nombre d’équations doit être égal au nombre de variables "
                  "(matrice carrée requise pour l’inversion). Recommencez.\n")
            continue
        n = n_vars
        break

    # 2) Saisie de A et b
    A = [[0.0 for _ in range(n)] for _ in range(n)]
    b = [[0.0] for _ in range(n)]

    print("\nEntrez les coefficients équation par équation.")
    for i in range(n):
        print(f"\n--- Équation {i+1} ---")
        for j in range(n):
            A[i][j] = read_float(f"Coefficient de x{j+1} : ")
        b[i][0] = read_float("Terme indépendant b : ")

    print_matrix(A, "\nMatrice A:")
    print_matrix(b, "Vecteur b:")

    # 3) Résolution: X = A^-1 b
    try:
        show_steps = input("Afficher les étapes de l'inversion ? (o/n): ").strip().lower() == "o"
        A_inv = gauss_jordan_inverse(A, verbose=show_steps)
        X = matmul(A_inv, b)
    except ValueError as e:
        print(f"\nImpossible de résoudre par inversion: {e}")
        return

    # 4) Affichage du résultat
    print_matrix(A_inv, "Matrice inverse A^-1:")
    print_matrix(X, "Solution X:")

    print("=== Valeurs des variables ===")
    for i in range(n):
        val = X[i][0]
        if abs(val) < 1e-10:
            val = 0.0
        print(f"x{i+1} = {val}")

if __name__ == "__main__":
    solve_linear_system_interactive()
