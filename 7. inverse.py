# Matrix Inverse using Gauss-Jordan Method
def inverse_matrix(A,TOL):
    n = len(A)

    # Create augmented matrix [A | I]
    augmented = []

    for i in range(n):
        row = A[i][:] + [1 if i == j else 0 for j in range(n)]
        augmented.append(row)

    # Gauss-Jordan elimination
    for i in range(n):
        # Find a suitable pivot
        pivot = i
        for j in range(i + 1, n):
            if abs(augmented[j][i]) > abs(augmented[pivot][i]):
                pivot = j

        # Check for singular matrix
        if abs(augmented[pivot][i]) < TOL:
            return None

        # Swap rows
        augmented[i], augmented[pivot] = augmented[pivot], augmented[i]

        # Make pivot equal to 1
        pivot_value = augmented[i][i]
        for j in range(2 * n):
            augmented[i][j] /= pivot_value

        # Make all other elements in pivot column zero
        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]
        for row in augmented:
                print(" ".join(f"{x:.4f}" for x in row))

    # Extract inverse matrix
    inverse = []
    for i in range(n):
        inverse.append(augmented[i][n:])

    return inverse
    

# Input matrix
n = int(input("Enter the order of matrix: "))

A = []
print("Enter the matrix elements:")

for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)

TOL = float(input("Enter the tolerance limit: "))

# Find inverse
result = inverse_matrix(A,TOL)

if result is None:
    print("Inverse does not exist (singular matrix).")
else:
    print("\nInverse of the matrix is:")
    for row in result:
        print(" ".join(f"{x:.4f}" for x in row))
