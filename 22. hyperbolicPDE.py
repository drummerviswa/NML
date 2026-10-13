# 22. Finite Difference Method for Hyperbolic PDE (1D Wave Equation)
# Solves ∂²u/∂t² = c² ∂²u/∂x² using Explicit Finite Difference Scheme
import math

print("=== Hyperbolic PDE Solver: 1D Wave Equation (Vibrating String) ===")
print("Formula: u(i, j+1) = 2(1 - λ²) u(i, j) + λ² [u(i+1, j) + u(i-1, j)] - u(i, j-1)")
print("CFL stability condition: λ = (c * k) / h <= 1.0\n")

length = float(input("Enter length of string (L): "))
c = float(input("Enter wave speed (c): "))
nx = int(input("Enter number of spatial divisions (nx): "))
nt = int(input("Enter number of time steps (nt): "))
total_time = float(input("Enter total time duration (T): "))

h = length / nx
k = total_time / nt
lam = (c * k) / h
lam2 = lam ** 2

print(f"\nGrid spacing: h = {h:.4f}, time step: k = {k:.4f}")
print(f"Courant number λ = {lam:.4f}")

if lam > 1.0 + 1e-9:
    print(f"WARNING: λ = {lam:.4f} > 1.0. CFL stability condition violated! Numerical instability will occur.")

f_str = input("\nEnter initial displacement f(x) for u(x, 0) (press Enter for sin(pi*x/L)): ").strip()
if not f_str:
    f_disp = lambda x: math.sin(math.pi * x / length)
else:
    f_disp = lambda x: eval(f_str, {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "pi": math.pi, "exp": math.exp})

g_str = input("Enter initial velocity g(x) = ∂u/∂t(x, 0) (press Enter for 0): ").strip()
if not g_str:
    g_vel = lambda x: 0.0
else:
    g_vel = lambda x: eval(g_str, {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "pi": math.pi})

left_bc = float(input("Enter left boundary condition at x = 0: "))
right_bc = float(input("Enter right boundary condition at x = L: "))

# u[j][i]: row j is time level (0 to nt), column i is spatial node (0 to nx)
u = [[0.0 for _ in range(nx + 1)] for _ in range(nt + 1)]

# Initial displacement at t = 0
for i in range(nx + 1):
    u[0][i] = f_disp(i * h)

# Boundary conditions for all time levels
for j in range(nt + 1):
    u[j][0] = left_bc
    u[j][nx] = right_bc

# First time step j = 1 using initial velocity condition:
# u(i, 1) = (1 - λ²) u(i, 0) + 0.5 λ² [u(i+1, 0) + u(i-1, 0)] + k * g(x_i)
for i in range(1, nx):
    xi = i * h
    u[1][i] = (1.0 - lam2) * u[0][i] + 0.5 * lam2 * (u[0][i + 1] + u[0][i - 1]) + k * g_vel(xi)

# Subsequent time steps j >= 1
for j in range(1, nt):
    for i in range(1, nx):
        u[j + 1][i] = 2.0 * (1.0 - lam2) * u[j][i] + lam2 * (u[j][i + 1] + u[j][i - 1]) - u[j - 1][i]

print("\n--- Wave Displacement Table u(x, t) ---")
header = f"{'Time':<10}" + "".join(f"{f'x={i*h:.2f}':<10}" for i in range(nx + 1))
print(header)
print("-" * len(header))

for j in range(nt + 1):
    row_str = f"{j * k:<10.4f}" + "".join(f"{u[j][i]:<10.4f}" for i in range(nx + 1))
    print(row_str)

print("-" * len(header))
print(f"Wave simulation completed up to t = {total_time:.4f}.")
