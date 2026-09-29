def divided_difference(x, y):
    n = len(x)

    table = [[0.0 for j in range(n)] for i in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (
                table[i + 1][j - 1] - table[i][j - 1]
            ) / (x[i + j] - x[i])
    return table
def newton_interpolation(x, y, value):

    table = divided_difference(x, y)
    n = len(x)
    result = table[0][0]
    term = 1
    for i in range(1, n):
        term = term * (value - x[i - 1])
        result = result + term * table[0][i]

    return result, table
n = int(input("Enter the number of data points: "))
x = []
print("\nEnter the x values:")

for i in range(n):
    x.append(float(input(f"x[{i}] = ")))
if len(set(x)) != len(x):
    print("\nError: x values must be distinct.")
    exit()
y = []
print("\nEnter the corresponding y values:")
for i in range(n):
    y.append(float(input(f"y[{i}] = ")))
value = float(input("\nEnter the value of x to find f(x): "))
result, table = newton_interpolation(x, y, value)
print("\nDivided Difference Values:")
for j in range(1, n):
    notation = "f(" + ",".join(f"x{k}" for k in range(j + 1)) + ")"

    print(f"\n{notation}")

    print(
        f"= ({table[1][j - 1]:.4f} - "
        f"{table[0][j - 1]:.4f}) / "
        f"({x[j]:.4f} - {x[0]:.4f})"
    )

    print(f"= {table[0][j]:.4f}")

print(f"\nFinal f({value}) = {result:.4f}")