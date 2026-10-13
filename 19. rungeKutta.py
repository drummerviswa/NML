# 16. Runge-Kutta 4th Order Method for Initial Value Problems
import math

f = input("Enter f(x, y) (e.g. x + y): ").strip()
x = float(input("Enter the initial value of x (x0): "))
y = float(input("Enter the initial value of y (y0): "))
h = float(input("Enter the step size (h): "))
X_req = float(input("Enter the value of x at which y is required: "))

n = round((X_req - x) / h)

safe_dict = {"math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp, "sqrt": math.sqrt}

print(f"\n--- Runge-Kutta 4th Order Results (Steps = {n}) ---")
print(f"{'Step':<6}{'x':<12}{'k1':<12}{'k2':<12}{'k3':<12}{'k4':<12}{'y':<12}")
print("-" * 78)

for step in range(1, n + 1):
    scope = {"x": x, "y": y, **safe_dict}
    k1 = h * eval(f, scope)

    scope["x"] = x + h / 2.0
    scope["y"] = y + k1 / 2.0
    k2 = h * eval(f, scope)

    scope["y"] = y + k2 / 2.0
    k3 = h * eval(f, scope)

    scope["x"] = x + h
    scope["y"] = y + k3
    k4 = h * eval(f, scope)

    y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    x = x + h

    print(f"{step:<6}{x:<12.6f}{k1:<12.6f}{k2:<12.6f}{k3:<12.6f}{k4:<12.6f}{y:<12.6f}")

print("-" * 78)
print(f"Final Solution: at x = {x:.6f}, y = {y:.6f}")
