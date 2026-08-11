# ==========================================================
# Polynomial Least Squares Regression Using Matrix Method
# Normal Equation: (A^T A)X = A^T y
# Solver: Gaussian Elimination
# Visualization: Matplotlib
# ==========================================================

import matplotlib.pyplot as plt


# ----------------------------------------------------------
# Print Matrix
# ----------------------------------------------------------

def printMatrix(A):
    for row in A:
        print("[", end="")
        for elem in row:
            print(f"{elem:12.6f}", end=" ")
        print("]")
    print()


# ----------------------------------------------------------
# Gaussian Elimination
# ----------------------------------------------------------

def gauss_elimination(n, A, b):

    TOL = 1e-10

    # Forward elimination
    for k in range(n - 1):

        # Pivoting
        if abs(A[k][k]) <= TOL:

            max_row = k
            max_value = abs(A[k][k])

            for p in range(k + 1, n):

                if abs(A[p][k]) > max_value:
                    max_value = abs(A[p][k])
                    max_row = p

            if max_value <= TOL:
                raise ValueError(
                    "No unique solution exists"
                )

            A[k], A[max_row] = A[max_row], A[k]
            b[k], b[max_row] = b[max_row], b[k]


        # Elimination
        for i in range(k + 1, n):

            factor = A[i][k] / A[k][k]

            for j in range(k + 1, n):

                A[i][j] = (
                    A[i][j]
                    - factor * A[k][j]
                )

            A[i][k] = 0

            b[i] = (
                b[i]
                - factor * b[k]
            )


    # Back substitution

    x = [0] * n

    x[n-1] = b[n-1] / A[n-1][n-1]


    for k in range(n-2, -1, -1):

        summation = 0

        for j in range(k+1, n):

            summation += A[k][j] * x[j]


        x[k] = (
            b[k] - summation
        ) / A[k][k]


    return x



# ----------------------------------------------------------
# Construct Polynomial Matrix A
#
# Degree m polynomial:
#
# y = c0 + c1*x + c2*x^2 + ... + cm*x^m
#
# ----------------------------------------------------------

def create_matrix_A(x, degree):

    A = []

    for value in x:

        row = []

        for power in range(degree + 1):

            row.append(value ** power)

        A.append(row)


    return A



# ----------------------------------------------------------
# Calculate A^T A
# ----------------------------------------------------------

def transpose_multiply(A):

    rows = len(A)
    cols = len(A[0])


    result = [
        [0 for j in range(cols)]
        for i in range(cols)
    ]


    for i in range(cols):

        for j in range(cols):

            total = 0

            for k in range(rows):

                total += (
                    A[k][i]
                    *
                    A[k][j]
                )

            result[i][j] = total


    return result



# ----------------------------------------------------------
# Calculate A^T y
# ----------------------------------------------------------

def transpose_y(A, y):

    rows = len(A)
    cols = len(A[0])


    result = [0 for i in range(cols)]


    for i in range(cols):

        total = 0

        for k in range(rows):

            total += (
                A[k][i]
                *
                y[k]
            )

        result[i] = total


    return result

# ----------------------------------------------------------
# Evaluate Polynomial
# ----------------------------------------------------------

def evaluate_polynomial(coeff, x):

    value = 0

    for i in range(len(coeff)):

        value += (
            coeff[i]
            *
            (x ** i)
        )

    return value



# ----------------------------------------------------------
# Display Polynomial Equation
# ----------------------------------------------------------

def display_polynomial(coeff):

    equation = "y = "

    for i, c in enumerate(coeff):

        if i == 0:

            equation += f"{c:.6f}"

        elif i == 1:

            if c >= 0:
                equation += f" + {c:.6f}x"
            else:
                equation += f" - {abs(c):.6f}x"

        else:

            if c >= 0:
                equation += (
                    f" + {c:.6f}x^{i}"
                )
            else:
                equation += (
                    f" - {abs(c):.6f}x^{i}"
                )


    print("\nBest Fit Polynomial")
    print("-------------------")
    print(equation)



# ==========================================================
# MAIN PROGRAM
# ==========================================================

print("Polynomial Least Squares Regression")
print("-----------------------------------")


n = int(
    input("Enter number of data points: ")
)


degree = int(
    input("Enter polynomial degree: ")
)


if degree >= n:

    print(
        "Degree must be smaller than number of points"
    )

    exit()



x = []
y = []


print("\nEnter data points")

for i in range(n):

    xi = float(
        input(f"x[{i+1}] = ")
    )

    yi = float(
        input(f"y[{i+1}] = ")
    )


    x.append(xi)
    y.append(yi)



# ----------------------------------------------------------
# Create Matrix A
# ----------------------------------------------------------

A = create_matrix_A(
    x,
    degree
)


print("\nMatrix A")
printMatrix(A)



# ----------------------------------------------------------
# Normal Equation
#
# (A^T A)X = A^T y
#
# ----------------------------------------------------------

ATA = transpose_multiply(A)


print("Matrix A^T A")
printMatrix(ATA)



ATy = transpose_y(
    A,
    y
)


print("Vector A^T y")

for value in ATy:

    print(
        f"{value:.6f}"
    )



# ----------------------------------------------------------
# Solve system
# ----------------------------------------------------------

coefficients = gauss_elimination(
    degree + 1,
    ATA,
    ATy
)



# ----------------------------------------------------------
# Display coefficients
# ----------------------------------------------------------

print("\nPolynomial Coefficients")
print("-----------------------")


for i,c in enumerate(coefficients):

    print(
        f"c{i} = {c:.8f}"
    )



display_polynomial(
    coefficients
)



# ----------------------------------------------------------
# Calculate Predictions and SSE
# ----------------------------------------------------------

print("\nPredictions")
print("-----------------------------")
print("x\tActual\tPredicted")


SSE = 0


for i in range(n):

    predicted = evaluate_polynomial(
        coefficients,
        x[i]
    )


    error = (
        y[i]
        -
        predicted
    )


    SSE += error ** 2


    print(
        f"{x[i]:.3f}\t"
        f"{y[i]:.3f}\t"
        f"{predicted:.6f}"
    )



print(
    "\nSum of Squared Error (SSE) =",
    SSE
)



# ==========================================================
# Visualization
# ==========================================================

# Generate smooth curve points

x_curve = []

y_curve = []


xmin = min(x)
xmax = max(x)


points = 200


step = (
    xmax - xmin
) / (points - 1)



for i in range(points):

    value = (
        xmin
        +
        i * step
    )

    x_curve.append(value)


    y_curve.append(
        evaluate_polynomial(
            coefficients,
            value
        )
    )



# Plot

plt.figure(
    figsize=(8,6)
)


# Scatter points

plt.scatter(
    x,
    y,
    color="red",
    s=60,
    label="Data Points"
)



# Fitted curve

plt.plot(
    x_curve,
    y_curve,
    color="blue",
    linewidth=2,
    label=f"Degree {degree} Polynomial"
)



plt.title(
    "Least Squares Polynomial Curve Fitting"
)


plt.xlabel(
    "x"
)


plt.ylabel(
    "y"
)


plt.grid(True)

plt.legend()


plt.show()