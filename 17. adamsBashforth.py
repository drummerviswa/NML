# 17. Adams-Bashforth-Moulton Predictor-Corrector Method
import math

f = input("Enter f(x, y) (e.g. x + y): ").strip()
x = []
y = []

safe_dict = {"math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp, "sqrt": math.sqrt}

def eval_f(xv, yv):
    return eval(f, {"x": xv, "y": yv, **safe_dict})

print("Enter the 4 starting values (x y), one pair per line:")
for i in range(4):
    a, b = map(float, input(f"Point {i} (x y): ").split())
    x.append(a)
    y.append(b)

X_req = float(input("Enter the value of x at which y is required: "))

h = x[1] - x[0]
n = round((X_req - x[3]) / h)

print("\n--- Adams-Bashforth-Moulton Predictor-Corrector Results ---")

for i in range(3, 3 + n):
    F = [eval_f(x[j], y[j]) for j in range(i - 3, i + 1)]

    X_k = x[i] + h

    # Adams-Bashforth 4-step Predictor
    Y_p = y[i] + (h / 24.0) * (
        55.0 * F[3]
        - 59.0 * F[2]
        + 37.0 * F[1]
        - 9.0 * F[0]
    )

    print(f"\nFor X = {X_k:.6f}")
    print(f"Predicted Y = {Y_p:.6f}")

    iteration = 0

    # Adams-Moulton repeated correction
    while True:
        iteration += 1

        Y_c = y[i] + (h / 24.0) * (
            9.0 * eval_f(X_k, Y_p)
            + 19.0 * F[3]
            - 5.0 * F[2]
            + F[1]
        )

        print(f"  Correction {iteration}: Y = {Y_c:.6f}")

        if abs(Y_c - Y_p) < 1e-6 or iteration >= 50:
            break

        Y_p = Y_c

    x.append(X_k)
    y.append(Y_c)

    print(f"Converged Y = {Y_c:.6f} in {iteration} iterations.")

print("-" * 55)
print(f"Final Solution: at x = {x[-1]:.6f}, y = {y[-1]:.6f}")
