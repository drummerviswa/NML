f = input("Enter f(x, y) (e.g. x + y): ")
x = []
y = []

print("Enter the 4 starting values (x y), one pair per line:")
for _ in range(4):
    a, b = map(float, input().split())
    x.append(a)
    y.append(b)

X_req = float(input("Enter the value of x at which y is required: "))

h = x[1] - x[0]
n = round((X_req - x[3]) / h)

print("\n--- Milne's Predictor-Corrector Results ---")

for i in range(3, 3 + n):

    F = [
        eval(f, {"x": x[j], "y": y[j]})
        for j in range(i - 3, i + 1)
    ]

    X_k = x[i] + h

    # Predictor
    Y_p = y[i - 3] + (4 * h / 3) * (
        2 * F[1] - F[2] + 2 * F[3]
    )

    print(f"\nFor X = {X_k:.6f}")
    print(f"Predicted Y = {Y_p:.6f}")

    iteration = 0

    # Repeated correction
    while True:
        iteration += 1

        Y_c = y[i - 1] + (h / 3) * (
            F[2]
            + 4 * F[3]
            + eval(f, {"x": X_k, "y": Y_p})
        )

        print(f"Correction {iteration}: Y = {Y_c:.6f}")

        if abs(Y_c - Y_p) < 1e-6:
            break

        Y_p = Y_c

    x.append(X_k)
    y.append(Y_c)

    print(f"Converged Y = {Y_c:.6f}")
    print(f"Number of iterations = {iteration}")
