def get_minor(matrix, row, col):
    return [r[:col] + r[col+1:] for i, r in enumerate(matrix) if i != row]

def determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(n):
        det += ((-1) ** c) * matrix[0][c] * determinant(get_minor(matrix, 0, c))
    return det

def adjoint(matrix):
    n = len(matrix)

    if n == 1:
        return [[1]]

    adj = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            minor = get_minor(matrix, i, j)
            cofactor = ((-1) ** (i + j)) * determinant(minor)
            adj[j][i] = cofactor   # Transpose while storing

    return adj

def inverse(matrix):
    det = determinant(matrix)

    if det == 0:
        return "Matrix is not invertible"

    adj = adjoint(matrix)

    inv = []
    for row in adj:
        inv.append([x / det for x in row])

    return inv

# Example
A = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]

inv = inverse(A)

print("Inverse:")
for row in inv:
    print(row)