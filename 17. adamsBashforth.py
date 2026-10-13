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

print("\n--- Adams-Bashforth-Moulton Predictor-Corrector Results ---")

for i in range(3, 3 + n):

    F = [
        eval(f, {"x": x[j], "y": y[j]})
        for j in range(i - 3, i + 1)
    ]

    X_k = x[i] + h

    # Adams-Bashforth Predictor
    Y_p = y[i] + (h / 24) * (
        55 * F[3]
        - 59 * F[2]
        + 37 * F[1]
        - 9 * F[0]
    )

    print(f"\nFor X = {X_k:.6f}")
    print(f"Predicted Y = {Y_p:.6f}")

    iteration = 0

    # Adams-Moulton repeated correction
    while True:
        iteration += 1

        Y_c = y[i] + (h / 24) * (
            9 * eval(f, {"x": X_k, "y": Y_p})
            + 19 * F[3]
            - 5 * F[2]
            + F[1]
        )

        print(f"Correction {iteration}: Y = {Y_c:.6f}")

        if abs(Y_c - Y_p) < 1e-6:
            break

        Y_p = Y_c

    x.append(X_k)
    y.append(Y_c)

    print(f"Converged Y = {Y_c:.6f}")
    print(f"Number of iterations = {iteration}")
