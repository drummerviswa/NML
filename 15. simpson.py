import sympy as sp
x = sp.symbols('x')
poly = input("Enter the polynomial f(x): ")
f = sp.sympify(poly)
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of subintervals n (even): "))
if n % 2 != 0:
    print("Error: n must be even for Simpson's 1/3 Rule.")
    exit()
h = (b - a) / n
simpson_sum = float(f.subs(x, a)) + float(f.subs(x, b))
for i in range(1, n):
    xi = a + i * h
    if i % 2 == 0: simpson_sum += 2 * float(f.subs(x, xi))
    else: simpson_sum += 4 * float(f.subs(x, xi))
simpson_result = (h / 3) * simpson_sum
exact_result = sp.integrate(f, (x, a, b))
exact_result_float = float(exact_result)
absolute_error = abs(exact_result_float - simpson_result)
print("\nFunction:", f)
print("Interval:", a, "to", b)
print("Number of subintervals:", n)
print("\nSimpson's 1/3 Rule =", simpson_result)
print("Exact Integral     =", exact_result_float)
print("Absolute Error     =", absolute_error)