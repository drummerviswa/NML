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