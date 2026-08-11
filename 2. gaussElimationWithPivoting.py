from fractions import Fraction
def printMatrix(A):
    for row in A:
        print("[",end="")
        for elem in row:
            print(round(Fraction(elem),5)," ",end="")
        print("]",end="")
        print()

def gauss_elimination(n, A, b):
    TOL = 1e-10
 
    # Forward Elimination
    for k in range(n - 1):
 
        # Check for zero pivot
        if abs(A[k][k]) <= TOL:
            print("The first row first column in 0")
            # Find the row with the largest pivot element
            max_row = k
            max_value = abs(A[k][k])
 
            for p in range(k + 1, n):
                if abs(A[p][k]) > max_value:
                    max_value = abs(A[p][k])
                    max_row = p
 
            # If no suitable pivot exists
            if max_value <= TOL:
                raise ValueError("No unique solution exists.")
 
            # Swap rows in A
            A[k], A[max_row] = A[max_row], A[k]
 
            # Swap corresponding elements in b
            b[k], b[max_row] = b[max_row], b[k]
        print(f"After {k} swap")
        # Elimination
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            # print("What is the factor: ",factor)
 
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - factor * A[k][j]
            A[i][k] = 0
            b[i] = b[i] - factor * b[k]
            print(f"    -- Row operation in row: {i+1}")
            printMatrix(A)
 
    # Back Substitution
    x = [0] * n
 
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
 
    for k in range(n - 2, -1, -1):
 
        sum_ax = 0
 
        for j in range(k + 1, n):
            sum_ax += A[k][j] * x[j]
 
        x[k] = (b[k] - sum_ax) / A[k][k]
 
    return x
 
 
# Main Program
 
n = int(input("Enter the size of the system: "))
 
print("Enter the coefficient matrix A:")
A = []
 
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)
 
print("Enter the RHS vector b:")
b = list(map(float, input().split()))
 
solution = gauss_elimination(n, A, b)
 
print("\nSolution Vector:")
for i in range(n):
    print(f"x{i+1} = {solution[i]:.2f}")