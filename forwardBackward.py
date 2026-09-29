import sympy as sp

n = int(input("Enter the number of points: "))

L = []

for i in range(n):
    row = list(map(float, input().split()))
    L.append(row)

x_value = float(input("Enter x value: "))

x = sp.Symbol('x')

addition_count = 0
subtraction_count = 0
multiplication_count = 0
division_count = 0
ac,sc,mc,dc=0,0,0,0

sum = 0
term2 = 0

for i in range(n):

    p = 1
    term1 = L[i][1]

    for j in range(n):

        if j != i:

            # Lagrange basis term
            term1 *= (x - L[j][0]) / (L[i][0] - L[j][0])

            # x - L[j][0]
            subtraction_count += 1

            # L[i][0] - L[j][0]
            subtraction_count += 1

            # Division
            division_count += 1

            # Multiplication with term1
            multiplication_count += 1

            # Numerical interpolation term
            p *= (x_value - L[j][0]) / (L[i][0] - L[j][0])

            # x_value - L[j][0]
            sc += 1

            # L[i][0] - L[j][0]
            sc += 1

            # Division
            dc += 1

            # Multiplication with p
            mc += 1

    # sum += p * L[i][1]
    sum += p * L[i][1]

    mc += 1
    ac += 1

    # term2 += term1 * L[i][1]
    term2 += term1 * L[i][1]

    multiplication_count += 1
    addition_count += 1


# Expand polynomial
poly_form = sp.expand(term2)

# Find degree
degree = sp.degree(poly_form, x)


# Display results
print("\nLagrange Form:", term2)

print("\nPolynomial Form:", poly_form)

print(f"\nInterpolation of {x_value}:", sum)

print("\nDegree of polynomial:", degree)

print("\nNumber of additions:", addition_count)

print("Number of subtractions:", subtraction_count)

print("Number of multiplications:", multiplication_count)

print("Number of divisions:", division_count)

print("\nTotal arithmetic operations:",
      addition_count +
      subtraction_count +
      multiplication_count +
      division_count)

print("\nNumber of operations to interpolate at x:",
      ac+sc+mc+dc)

newton.py
import sympy as sp

n = int(input("Enter number of data points: "))

x_data = []
y_data = []

for i in range(n):
    x_val, y_val = map(float, input(f"Enter x[{i}] and y[{i}]: ").split())
    x_data.append(x_val)
    y_data.append(y_val)

l = int(input("Enter number of interpolated values: "))

x_values = []

for k in range(l):
    x_val = float(input(f"Enter interpolation x[{k}]: "))
    x_values.append(x_val)

d = [[0.0 for j in range(n)] for i in range(n)]

for j in range(n):
    d[0][j] = y_data[j]

for i in range(1, n):
    for j in range(n - i):
        d[i][j] = (
            d[i - 1][j + 1] - d[i - 1][j]
        ) / (
            x_data[j + i] - x_data[j]
        )

print("\nDivided Difference Table")

print(f"{'x':<12}{'f(x)':<18}", end="")

for i in range(1, n):
    print(f"{'DD' + str(i):<18}", end="")

print()

for j in range(n):
    print(f"{x_data[j]:<12.6f}{y_data[j]:<18.6f}", end="")

    for i in range(1, n):
        if j < n - i:
            print(f"{d[i][j]:<18.6f}", end="")
        else:
            print(f"{'':<18}", end="")

    print()

x = sp.Symbol('x')

for k in range(l):
    y_value = d[0][0]
    p = 1

    for i in range(n - 1):
        p = p * (x_values[k] - x_data[i])
        y_value = y_value + p * d[i + 1][0]

    print(f"x = {x_values[k]}, y = {y_value}")

polynomial = d[0][0]
p = 1

for i in range(n - 1):
    p = p * (x - x_data[i])
    polynomial = polynomial + p * d[i + 1][0]

polynomial = sp.expand(polynomial)

print("\nNewton Polynomial:")
print(polynomial)

forward.py
import sympy as sp
import math

n = int(input("Enter number of data points: "))

x_data = []
y_data = []

for i in range(n):
    x_val, y_val = map(float, input(f"Enter x[{i}] and y[{i}]: ").split())
    x_data.append(x_val)
    y_data.append(y_val)

l = int(input("Enter number of interpolated values: "))

x_values = []

for k in range(l):
    x_val = float(input(f"Enter interpolation x[{k}]: "))
    x_values.append(x_val)

d = [[0.0 for j in range(n)] for i in range(n)]

for j in range(n):
    d[0][j] = y_data[j]

for i in range(1, n):
    for j in range(n - i):
        d[i][j] = d[i - 1][j + 1] - d[i - 1][j]

print("\nForward Difference Table")

print(f"{'x':<12}{'f(x)':<18}", end="")

for i in range(1, n):
    print(f"{'DD' + str(i):<18}", end="")

print()

for j in range(n):
    print(f"{x_data[j]:<12.6f}{y_data[j]:<18.6f}", end="")

    for i in range(1, n):
        if j < n - i:
            print(f"{d[i][j]:<18.6f}", end="")
        else:
            print(f"{'':<18}", end="")

    print()

x = sp.Symbol('x')

h = x_data[1] - x_data[0]

for k in range(l):
    u = (x_values[k] - x_data[0]) / h
    y_value = d[0][0]
    term = 1

    for i in range(1, n):
        term = term * (u - (i - 1))
        y_value = y_value + (term / math.factorial(i)) * d[i][0]

    print(f"x = {x_values[k]}, y = {y_value}")

u = (x - x_data[0]) / h

polynomial = d[0][0]
term = 1

for i in range(1, n):
    term = term * (u - (i - 1))
    polynomial = polynomial + (term / math.factorial(i)) * d[i][0]

polynomial = sp.expand(polynomial)

print("\nNewton Forward Polynomial:")
print(polynomial)

backward.py
import sympy as sp
import math

n = int(input("Enter number of data points: "))

x_data = []
y_data = []

for i in range(n):
    x_val, y_val = map(float, input(f"Enter x[{i}] and y[{i}]: ").split())
    x_data.append(x_val)
    y_data.append(y_val)

h = x_data[1] - x_data[0]

l = int(input("Enter number of interpolated values: "))

x_values = []

for k in range(l):
    x_val = float(input(f"Enter interpolation x[{k}]: "))
    x_values.append(x_val)

d = [[0.0 for j in range(n)] for i in range(n)]

for j in range(n):
    d[0][j] = y_data[j]

for i in range(1, n):
    for j in range(i, n):
        d[i][j] = d[i - 1][j] - d[i - 1][j - 1]

print("\nNewton Backward Difference Table\n")

print(f"{'x':<12}{'f(x)':<18}", end="")

for i in range(1, n):
    print(f"{'DD' + str(i):<18}", end="")
print()


for j in range(n):
    print(f"{x_data[j]:<12.6f}{y_data[j]:<18.6f}", end="")
    for i in range(1, n):
        if j >= i:
            print(f"{d[i][j]:<18.6f}", end="")
        else:
            print(f"{'':<18}", end="")

    print()

for k in range(l):
    x_val = x_values[k]
    x_last = x_data[n - 1]
    print(x_last)
    u = (x_val - x_last) / h

    y_value = d[0][n - 1]
    print(y_value)    
    term = 1

    for i in range(1, n):
        term = term * (u + (i - 1))
        print(d[i][n-1])
        y_value = y_value + (term / math.factorial(i)) * d[i][n - 1]
        print(y_value)
    print(f"x = {x_val}, y = {y_value}")

x = sp.Symbol('x')
u = (x - x_data[n - 1]) / h
polynomial = d[0][n - 1]
term = 1

for i in range(1, n):
    term = term * (u + (i - 1))
    polynomial = polynomial + (term / math.factorial(i)) * d[i][n - 1]

polynomial = sp.expand(polynomial)

print("\nNewton Backward Polynomial:")
print(polynomial)