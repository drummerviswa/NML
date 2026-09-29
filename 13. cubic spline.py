import sympy as sp
import matplotlib.pyplot as plt
import numpy as np


def calculate_M(x, y):
    n = len(x)
    unknowns = sp.symbols(f'M1:{n-1}')
    equations = []

    for i in range(1, n - 1):
        h_left = x[i] - x[i - 1]
        h_right = x[i + 1] - x[i]

        equation = (
            h_left * (0 if i - 1 == 0 else unknowns[i - 2])
            + 2 * (h_left + h_right) * unknowns[i - 1]
            + h_right * (0 if i + 1 == n - 1 else unknowns[i])
            - 6 * (
                (y[i + 1] - y[i]) / h_right
                - (y[i] - y[i - 1]) / h_left
            )
        )

        equations.append(equation)

    solution = sp.solve(equations, unknowns)

    M = [0]

    for variable in unknowns:
        M.append(solution[variable])

    M.append(0)

    return M


def cubic_spline(x, y, M):
    X = sp.symbols('x')
    splines = []

    n = len(x)

    for i in range(1, n):
        h = x[i] - x[i - 1]

        f = (
            ((x[i] - X) ** 3 / (6 * h)) * M[i - 1]
            + ((X - x[i - 1]) ** 3 / (6 * h)) * M[i]
            + ((x[i] - X) / h)
            * (y[i - 1] - (h ** 2 / 6) * M[i - 1])
            + ((X - x[i - 1]) / h)
            * (y[i] - (h ** 2 / 6) * M[i])
        )

        splines.append(sp.expand(f))

    return splines


print("NATURAL CUBIC SPLINE")
print("-" * 40)

n = int(input("Enter number of data points: "))

x = []

print("\nEnter x values:")
for i in range(n):
    x.append(float(input(f"x[{i}] = ")))

y = []

print("\nEnter y values:")
for i in range(n):
    y.append(float(input(f"y[{i}] = ")))

M = calculate_M(x, y)

print("\nCalculated M values:")
for i in range(n):
    print(f"M[{i}] = {sp.N(M[i])}")

splines = cubic_spline(x, y, M)

print("\nCUBIC SPLINE POLYNOMIALS")
print("-" * 40)

for i in range(n - 1):
    print(f"\nInterval [{x[i]}, {x[i + 1]}]")
    print(f"S{i + 1}(x) = {splines[i]}")

value = float(input("\nEnter x value for interpolation: "))

X = sp.symbols('x')

for i in range(n - 1):
    if x[i] <= value <= x[i + 1]:
        result = splines[i].subs(X, value)

        print(f"\nUsing interval [{x[i]}, {x[i + 1]}]")
        print(f"S(x) = {splines[i]}")
        print(f"S({value}) = {sp.N(result)}")
        break
else:
    print("\nError: x value is outside the given range.")

plt.figure(figsize=(8, 5))

for i in range(n - 1):
    points = np.linspace(x[i], x[i + 1], 100)
    values = [
        float(splines[i].subs(X, point))
        for point in points
    ]
    plt.plot(points, values, color="blue")

plt.scatter(x, y, color="red", label="Data points")

if x[0] <= value <= x[-1]:
    plt.scatter(
        value,
        float(result),
        color="green",
        s=80,
        label="Interpolated value"
    )

plt.xlabel("x")
plt.ylabel("y")
plt.title("Natural Cubic Spline")
plt.grid(True)
plt.legend()
plt.show()
