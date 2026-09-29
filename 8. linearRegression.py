import matplotlib.pyplot as plt

t = [
    2.5, 3.0, 3.2, 4.0, 4.5, 4.8, 5.0, 5.2, 5.5, 6.0,
    6.2, 6.5, 7.0, 7.1, 7.5, 8.0, 8.3, 8.5, 9.0, 9.2,
    9.5, 10.0, 10.2, 10.5, 11.0,
    2.8, 3.5, 3.8, 4.2, 4.7, 5.1, 5.3, 5.8, 6.1, 6.4,
    6.8, 7.2, 7.4, 7.8, 8.1, 8.4, 8.8, 9.1, 9.4, 9.8,
    10.1, 10.4, 10.8, 11.2, 11.5
]

y = [
    53, 56, 58, 62, 61, 65, 68, 67, 72, 70,
    75, 73, 78, 82, 79, 83, 81, 86, 88, 85,
    92, 90, 94, 93, 97,
    54, 60, 59, 64, 63, 69, 71, 68, 74, 76,
    75, 80, 83, 81, 85, 84, 89, 87, 91, 93,
    96, 95, 98, 99, 100
]

def design_matrix(t, degree):

    A = []

    for value in t:

        if degree == 1:
            A.append([value, 1])

        elif degree == 2:
            A.append([value ** 2, value, 1])

        elif degree == 3:
            A.append([
                value ** 3,
                value ** 2,
                value,
                1
            ])

    return A

def transpose(A):

    result = []

    for j in range(len(A[0])):

        row = []

        for i in range(len(A)):
            row.append(A[i][j])

        result.append(row)

    return result

def matrix_multiply(A, B):

    result = []

    for i in range(len(A)):

        row = []

        for j in range(len(B[0])):

            total = 0

            for k in range(len(B)):
                total += A[i][k] * B[k][j]

            row.append(total)

        result.append(row)

    return result

def gauss_seidel(A, b, tol=1e-10, max_iter=1000):

    n = len(b)

    x = [0.0] * n

    for iteration in range(max_iter):

        old_x = x[:]

        for i in range(n):

            total = 0

            # Values already updated
            for j in range(i):
                total += A[i][j] * x[j]

            # Values not yet updated
            for j in range(i + 1, n):
                total += A[i][j] * old_x[j]

            x[i] = (b[i] - total) / A[i][i]

        # Check convergence
        error = 0

        for i in range(n):

            difference = abs(x[i] - old_x[i])

            if difference > error:
                error = difference

        if error < tol:
            print("Iterations:", iteration + 1)
            return x

    print("Maximum iterations reached")

    return x

degrees = [1, 2, 3]

titles = [
    "Linear Fit",
    "Quadratic Fit",
    "Cubic Fit"
]


for degree, title in zip(degrees, titles):

    # Create design matrix
    A = design_matrix(t, degree)

    # Transpose
    AT = transpose(A)

    # Calculate A^T A
    ATA = matrix_multiply(AT, A)

    # Convert y into column matrix
    Y = []

    for value in y:
        Y.append([value])

    # Calculate A^T y
    ATy_matrix = matrix_multiply(AT, Y)

    # Convert to normal list
    ATy = []

    for row in ATy_matrix:
        ATy.append(row[0])
    
    coefficients = gauss_seidel(
        ATA,
        ATy
    )

    print(title)

    print("Coefficients:")

    for value in coefficients:
        print(value)


    xx = []

    minimum = min(t)
    maximum = max(t)

    for i in range(300):

        value = minimum + (maximum - minimum) * i / 299

        xx.append(value)


    yy = []

    for value in xx:

        if degree == 1:

            result = (
                coefficients[0] * value +
                coefficients[1]
            )

        elif degree == 2:

            result = (
                coefficients[0] * value ** 2 +
                coefficients[1] * value +
                coefficients[2]
            )

        else:

            result = (
                coefficients[0] * value ** 3 +
                coefficients[1] * value ** 2 +
                coefficients[2] * value +
                coefficients[3]
            )

        yy.append(result)


    plt.figure(figsize=(7, 5))

    plt.scatter(
        t,
        y,
        color="red",
        label="Data"
    )

    plt.plot(
        xx,
        yy,
        linewidth=2,
        label=title
    )

    plt.title(title)
    plt.xlabel("Study Hours")
    plt.ylabel("Exam Score")
    plt.grid(True)
    plt.legend()

    plt.show()