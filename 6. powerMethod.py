def power_method(n, A, initialVector, tol, max_iter):

    # Initial vector
    x = initialVector

    eigenvalue_old = 0.0

    for iteration in range(max_iter):

        # y = A * x
        y = [0.0] * n

        for i in range(n):
            for j in range(n):
                y[i] += A[i][j] * x[j]

        # Find the largest absolute value
        max_value = max(abs(value) for value in y)

        # Normalize the vector
        x_new = [value / max_value for value in y]

        # Estimate eigenvalue
        eigenvalue = max_value

        # Check convergence
        if abs(eigenvalue - eigenvalue_old) < tol:
            return eigenvalue, x_new, iteration + 1

        x = x_new
        eigenvalue_old = eigenvalue

    return eigenvalue, x, max_iter

def getInput(n, matrix):
    for i in range(n):
        for j in range(n):
            matrix[i][j]=int(input(f"Enter the value of {i}x{j}: "))
    return matrix

n=int(input("Enter the size of matrix in terms of n: "))
matrix = [[0 for _ in range(n)] for _ in range(n)]
A = getInput(n,matrix)

initial = [1.0]*n
print("Enter initial value")
for i in range(n):
    initial[i]=int(input(f"I:{i}"))

tol = float(input("Enter tolerance value: "))
max_iter = int(input("Enter maximum iterations: "))

eigenvalue, eigenvector, iterations = power_method(n,A,initial,tol,max_iter)

print("Dominant Eigenvalue =", eigenvalue)
print("Corresponding Eigenvector =", eigenvector)
print("Number of Iterations =", iterations)