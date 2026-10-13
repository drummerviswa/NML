# 15. Composite Gauss-Legendre 2-Point Quadrature Rule
import math

expr = input("Enter f(x) (press Enter for default x**2): ").strip()
if expr:
    f = lambda x: eval(expr, {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp, "sqrt": math.sqrt})
else:
    f = lambda x: x**2

a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of subintervals n: "))

h = (b - a) / n

I = 0.0

print(f"\nSubintervals = {n}, Step size h = {h:.6f}")
print("-" * 55)
print(f"{'Interval':<10}{'x_mid':<12}{'x1':<12}{'x2':<12}{'Sub-Integral':<12}")
print("-" * 55)

for i in range(n):
    xi = a + i * h
    xip1 = xi + h

    midpoint = (xi + xip1) / 2.0
    d = h / (2.0 * math.sqrt(3))

    x1 = midpoint - d
    x2 = midpoint + d

    sub_I = (h / 2.0) * (f(x1) + f(x2))
    I += sub_I

    print(f"[{xi:.3f}, {xip1:.3f}] {midpoint:<12.6f}{x1:<12.6f}{x2:<12.6f}{sub_I:<12.6f}")

print("-" * 55)
print(f"Integral = {I:.8f}")
