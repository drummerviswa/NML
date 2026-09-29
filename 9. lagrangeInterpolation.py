import sympy as sp

x = sp.symbols('x')

X = [2, 4, 3, 8]
F = [1, 3, 5, 9]
n = len(X)

# (a) LAGRANGE FORM
P = 0
for i in range(n):
    L = 1
    for j in range(n):
        if i != j:
            L *= (x - X[j]) / (X[i] - X[j])
    P += L * F[i]
print("(a) Lagrange Form:")
print(sp.factor(P))

# (b) CUBIC FORM
C = sp.expand(P)
print("\n(b) Cubic Form:")
print(C)

# (c) LAGRANGE AT x = 6.5 + OPERATION COUNT
xv = 6.5
value = 0
add = sub = mul = div = 0
for i in range(n):
    product = 1
    for j in range(n):
        if i != j:
            product *= (xv - X[j]) / (X[i] - X[j])
            sub += 2
            mul += 1
            div += 1
    product *= F[i]
    mul += 1
    if i > 0:
        value += product
        add += 1
    else:
        value = product
print("\n(c) Lagrange at x =", xv)
print("Value =", value)
print("Add =", add, "Sub =", sub,
      "Mul =", mul, "Div =", div)
print("Total =", add + sub + mul + div)

# (d) CONVERSION TO CUBIC
print("\n(d) Cubic Conversion:")
print(C)
poly = sp.Poly(C, x)
a, b, c, d = poly.all_coeffs()
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)

# (e) CUBIC AT x = 6.5
result = C.subs(x, xv)
print("\n(e) Cubic at x =", xv)
print("Value =", result)

# Operation count for a*x^3+b*x^2+c*x+d
mul_e = 5
add_e = 3
print("Multiplication =", mul_e)
print("Addition =", add_e)
print("Total =", mul_e + add_e)

# (f) BREAK-EVEN POINT
conversion_cost = 0   
lagrange_cost = add + sub + mul + div
cubic_cost = mul_e + add_e
print("\n(f) Break-even:")
for k in range(1, 20):
    Lcost = k * lagrange_cost
    Ccost = conversion_cost + k * cubic_cost

    if Ccost < Lcost:
        print("Break-even point =", k)
        break