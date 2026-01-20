'''
Ecrivez un programme qui inverse une matrice par la méthode du pivot de Gauss-Jordan
'''
import random

def create_random_int_matrix(n, min_val=0, max_val=9):
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]

def print_matrix(matrix, title=None):
    if title:
        print(title)
    for row in matrix:
        print(" ".join(f"{v:9.3f}" for v in row))
    print()

def swap_lines(A, i, j):
    if i == j:
        return
    A[i], A[j] = A[j], A[i]

def transvection(A, k, i, alpha):
    #vEx 2.2: Lk = Lk - alpha * Li (in-place).
    for col in range(len(A[k])):
        A[k][col] = A[k][col] - alpha * A[i][col]

def scale_row(A, k, divisor):
    for col in range(len(A[k])):
        A[k][col] = A[k][col] / divisor

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

def gauss_jordan_inverse(A, eps=1e-12, verbose=True):
    """
    Ex 2.4: Inverse matrice methods pivot Gauss-Jordan.
    """
    n = len(A)
    if n == 0 or any(len(row) != n for row in A):
        raise ValueError("La matrice doit être carrée (n x n).")

    aug = augment_with_identity(A)  # [A|I]
    if verbose:
        print_matrix(aug, "Matrice augmentée initiale [A | I]:")

    r = 0

    for j in range(n):
        k = r
        max_val = abs(aug[r][j]) if r < n else 0.0
        for i in range(r + 1, n):
            v = abs(aug[i][j])
            if v > max_val:
                max_val = v
                k = i

        if verbose:
            print(f"--- Colonne {j} ---")
            print(f"Recherche pivot (max |A[i,{j}]|) sur i = {r}..{n-1} -> ligne k = {k}, valeur = {aug[k][j]:.6f}")

        if max_val < eps:
            if verbose:
                print("Pivot ~ 0 dans cette colonne -> on passe à la colonne suivante.\n")
            continue

        if k != r:
            if verbose:
                print(f"Échange des lignes {k} et {r} (placer le pivot sur la diagonale)")
            swap_lines(aug, k, r)
            if verbose:
                print_matrix(aug, "Après échange:")

        pivot = aug[r][j]
        if abs(pivot) < eps:
            if verbose:
                print("Pivot devenu nul après échange -> impossible.\n")
            continue

        if verbose:
            print(f"Normalisation: diviser la ligne {r} par le pivot {pivot:.6f} (pivot -> 1)")
        scale_row(aug, r, pivot)
        if verbose:
            print_matrix(aug, "Après normalisation:")

        for i in range(n):
            if i == r:
                continue
            factor = aug[i][j]
            if abs(factor) > eps:
                if verbose:
                    print(f"Transvection: L{i} = L{i} - ({factor:.6f}) * L{r}  (annuler A[{i},{j}])")
                transvection(aug, i, r, factor)

        if verbose:
            print_matrix(aug, f"Après élimination dans la colonne {j}:")

        r += 1
        if r == n:
            break

    for i in range(n):
        for j in range(n):
            expected = 1.0 if i == j else 0.0
            if abs(aug[i][j] - expected) > 1e-8:
                raise ValueError("Matrice non inversible (la réduction ne donne pas l'identité).")

    return extract_inverse(aug)

def main():
    n = int(input("Saisissez la dimension n de la matrice carrée (n x n): "))

    print("\nChoisissez le mode:")
    print("1) Matrice aléatoire")
    print("2) Saisie manuelle")
    mode = input("Votre choix (1/2): ").strip()

    if mode == "2":
        A = []
        print("\nEntrez la matrice ligne par ligne:")
        for i in range(n):
            row = []
            for j in range(n):
                row.append(float(input(f"A[{i}][{j}] = ").replace(",", ".")))
            A.append(row)
    else:
        A = create_random_int_matrix(n, 0, 5)

    print_matrix([[float(x) for x in row] for row in A], "Matrice A:")

    try:
        invA = gauss_jordan_inverse(A, verbose=True)
        print_matrix(invA, "Matrice inverse A^-1:")
    except ValueError as e:
        print(f"Erreur: {e}")

if __name__ == "__main__":
    main()
