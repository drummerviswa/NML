# 21. Finite Difference Method for Parabolic PDE (1D Heat Equation)
# Solves ∂u/∂t = c² ∂²u/∂x² using Bender-Schmidt Explicit Scheme
import math

print("=== Parabolic PDE Solver: 1D Heat Equation (Bender-Schmidt) ===")
print("Formula: u(i, j+1) = λ * u(i-1, j) + (1 - 2λ) * u(i, j) + λ * u(i+1, j)")
print("Stability condition: λ = (c² * k) / h² <= 0.5\n")

length = float(input("Enter length of rod (L): "))
c2 = float(input("Enter thermal diffusivity c² (e.g. 1.0): "))
nx = int(input("Enter number of spatial divisions (nx): "))
nt = int(input("Enter number of time steps (nt): "))
total_time = float(input("Enter total time duration (T): "))

h = length / nx
k = total_time / nt
lam = (c2 * k) / (h ** 2)

print(f"\nGrid spacing: h = {h:.4f}, time step: k = {k:.4f}")
print(f"Mesh ratio λ = {lam:.4f}")

if lam > 0.5 + 1e-9:
    print(f"WARNING: λ = {lam:.4f} > 0.5. The explicit scheme is unstable! Consider increasing nx or nt.")

f_str = input("\nEnter initial condition f(x) for u(x, 0) (press Enter for sin(pi*x/L)): ").strip()
if not f_str:
    f_init = lambda x: math.sin(math.pi * x / length)
else:
    f_init = lambda x: eval(f_str, {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "pi": math.pi, "exp": math.exp})

left_bc = float(input("Enter boundary condition at x = 0 (left): "))
right_bc = float(input("Enter boundary condition at x = L (right): "))

# u[j][i]: row j is time level (0 to nt), column i is spatial node (0 to nx)
u = [[0.0 for _ in range(nx + 1)] for _ in range(nt + 1)]

# Initial condition at t = 0
for i in range(nx + 1):
    u[0][i] = f_init(i * h)

# Boundary conditions for all time steps
for j in range(nt + 1):
    u[j][0] = left_bc
    u[j][nx] = right_bc

# Time marching
for j in range(nt):
    for i in range(1, nx):
        u[j + 1][i] = lam * u[j][i - 1] + (1.0 - 2.0 * lam) * u[j][i] + lam * u[j][i + 1]

print("\n--- Temperature Distribution Table u(x, t) ---")
header = f"{'Time':<10}" + "".join(f"{f'x={i*h:.2f}':<10}" for i in range(nx + 1))
print(header)
print("-" * len(header))

for j in range(nt + 1):
    row_str = f"{j * k:<10.4f}" + "".join(f"{u[j][i]:<10.4f}" for i in range(nx + 1))
    print(row_str)

print("-" * len(header))
print(f"Final temperature distribution at t = {total_time:.4f} reached.")
