import math

def f(x):
    return x**2

a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
n = int(input("Enter number of subintervals n: "))

h = (b - a) / n

I = 0

for i in range(n):
    xi = a + i * h
    xip1 = xi + h

    midpoint = (xi + xip1) / 2

    d = h / (2 * math.sqrt(3))

    x1 = midpoint - d
    x2 = midpoint + d

    I = I + (h / 2) * (f(x1) + f(x2))

print("Integral =", I)
