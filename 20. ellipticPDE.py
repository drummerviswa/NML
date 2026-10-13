# 20. Finite Difference Method for Elliptic PDE (Laplace & Poisson Equations)
# Solves ∇²u = 0 (or ∇²u = f(x, y)) using 5-point stencil & Liebmann's method

print("=== Elliptic PDE Solver: Laplace / Poisson Equation ===")
print("Standard 5-point formula: u(i, j) = 0.25 * [u(i+1, j) + u(i-1, j) + u(i, j+1) + u(i, j-1)]")

nx = int(input("\nEnter number of intervals in x-direction (nx): "))
ny = int(input("Enter number of intervals in y-direction (ny): "))

print("\nEnter Dirichlet Boundary Conditions:")
top = float(input("Top boundary value: "))
bottom = float(input("Bottom boundary value: "))
left = float(input("Left boundary value: "))
right = float(input("Right boundary value: "))

tol = float(input("Enter convergence tolerance (e.g. 1e-4): "))
max_iter = int(input("Enter maximum iterations (e.g. 200): "))

# Initialize grid (ny + 1 rows, nx + 1 columns)
# grid[j][i]: j is y index (0 to ny), i is x index (0 to nx)
grid = [[0.0 for _ in range(nx + 1)] for _ in range(ny + 1)]

# Apply boundary conditions
for i in range(nx + 1):
    grid[0][i] = bottom
    grid[ny][i] = top
for j in range(ny + 1):
    grid[j][0] = left
    grid[j][nx] = right

# Corner averages
grid[0][0] = (bottom + left) / 2.0
grid[0][nx] = (bottom + right) / 2.0
grid[ny][0] = (top + left) / 2.0
grid[ny][nx] = (top + right) / 2.0

# Initialize interior nodes with average of boundaries
avg_val = (top + bottom + left + right) / 4.0
for j in range(1, ny):
    for i in range(1, nx):
        grid[j][i] = avg_val

print("\nStarting Liebmann's (Gauss-Seidel) iterations...")

converged = False
for it in range(1, max_iter + 1):
    max_error = 0.0
    for j in range(ny - 1, 0, -1):  # top-down row order
        for i in range(1, nx):
            old = grid[j][i]
            # Standard 5-point stencil
            grid[j][i] = 0.25 * (grid[j + 1][i] + grid[j - 1][i] + grid[j][i + 1] + grid[j][i - 1])
            err = abs(grid[j][i] - old)
            if err > max_error:
                max_error = err

    if it % 10 == 0 or it == 1:
        print(f"Iteration {it:3d}: Max Error = {max_error:.6f}")

    if max_error < tol:
        print(f"Converged successfully in {it} iterations! (Max Error = {max_error:.6e})")
        converged = True
        break

if not converged:
    print(f"Completed {max_iter} iterations.")

print("\n--- Final Grid Values u[y][x] ---")
print("    " + "".join(f"  x={i:<5d}" for i in range(nx + 1)))
print("    " + "-" * ((nx + 1) * 8))

for j in range(ny, -1, -1):  # print from top (ny) down to bottom (0)
    row_str = "".join(f"{grid[j][i]:8.3f}" for i in range(nx + 1))
    print(f"y={j:<2d}|{row_str}")
