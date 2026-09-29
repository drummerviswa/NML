import sympy as sp
x = sp.symbols('x')
poly = input("Enter the polynomial f(x): ")
f = sp.sympify(poly)
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of subintervals n: "))
h = (b - a) / n
trapezoidal_sum = float(f.subs(x, a)) + float(f.subs(x, b))
for i in range(1, n):
    xi = a + i * h
    trapezoidal_sum += 2 * float(f.subs(x, xi))
trapezoidal_result = (h / 2) * trapezoidal_sum
exact_result = sp.integrate(f, (x, a, b))
exact_result_float = float(exact_result)
absolute_error = abs(exact_result_float - trapezoidal_result)
print("\nFunction:", f)
print("Interval:", a, "to", b)
print("Number of subintervals:", n)
print("\nTrapezoidal Rule =", trapezoidal_result)
print("Exact Integral   =", exact_result_float)
print("Absolute Error   =", absolute_error)
