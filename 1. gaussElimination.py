def getMatrix(size):
    matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            matrix[i][j] = float(input(f"Enter element [{i}][{j}]: "))

    return matrix


def GaussElimination(n, A, b):
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - factor * A[k][j]
            #Forward elimination
            b[i] = b[i] - factor * b[k]

    # Back Substitution
    x = [0] * n
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        total = b[i]
        for j in range(i + 1, n):
            total -= A[i][j] * x[j]
        x[i] = total / A[i][i]
    return x


# Main Program
N = int(input("Enter the size of the matrix: "))
print("Enter the matrix A: ")
matrix = []
for i in range(N):
    row = list(map(float,input().split()))
    matrix.append(row)
print("Enter the answer vector b: ")
b = list(map(float, input().split()))
ans = GaussElimination(N, matrix, b)
for _ in ans:
    print(_)