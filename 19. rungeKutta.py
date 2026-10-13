f = input("Enter f(x, y) (e.g. x + y): ")
x = float(input("Enter the initial value of x (x0): "))
y = float(input("Enter the initial value of y (y0): "))
h = float(input("Enter the step size (h): "))
X_req = float(input("Enter the value of x at which y is required: "))

n = round((X_req - x) / h)

print("\n--- Runge-Kutta 4th Order Results ---")
for _ in range(n):
    k1 = h * eval(f, {"x": x, "y": y})
    k2 = h * eval(f, {"x": x + h / 2, "y": y + k1 / 2})
    k3 = h * eval(f, {"x": x + h / 2, "y": y + k2 / 2})
    k4 = h * eval(f, {"x": x + h, "y": y + k3})
    y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    x = x + h
    print(f"X = {x:.6f}, Y = {y:.6f}")
