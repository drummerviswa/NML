def gauss_jacobi(A, b, x_old, TOL, KMAX):
    n = len(A)

    print("Initial Guess:")
    for i in range(n):
        print(f"x[{i+1}] = {x_old[i]}")

    for k in range(1, KMAX + 1):
        x_new = [0.0] * n

        # Compute new values
        for i in range(n):
            summ = 0.0
            for j in range(n):
                if j != i:
                    summ += A[i][j] * x_old[j]

            if A[i][i] == 0:
                raise ValueError(f"Zero diagonal element at row {i+1}")

            x_new[i] = (b[i] - summ) / A[i][i]

        # Compute error
        error = max(abs(x_new[i] - x_old[i]) for i in range(n))

        print(f"\nIteration {k}")
        for i in range(n):
            print(f"x[{i+1}] = {x_new[i]:.6f}")
        print(f"Maximum Error = {error:.6e}")

        # Check convergence
        if error <= TOL:
            print("\nConverged Successfully!")
            return x_new

        # Update old values
        x_old = x_new[:]

    print("\nMaximum iterations reached.")
    return x_new

num_resistors = int(input("Enter number of resistors: "))

edges = []

for i in range(num_resistors):
    print(f"\nResistor {i+1}")
    u = int(input("From node: "))
    v = int(input("To node: "))
    r = float(input("Resistance (ohms): "))
    edges.append((u, v, r))

v1 = float(input("\nVoltage at node 1: "))
v6 = float(input("Voltage at node 6: "))

known_voltage = {1: v1, 6: v6}
unknown = [2, 3, 4, 5]

m = len(unknown)

A = [[0.0 for _ in range(m)] for _ in range(m)]
B = [0.0 for _ in range(m)]

# Construct coefficient matrix and RHS vector
for i, node in enumerate(unknown):
    for u, v, r in edges:
        if node == u or node == v:
            other = v if node == u else u
            conductance = 1.0 / r

            A[i][i] += conductance

            if other in unknown:
                j = unknown.index(other)
                A[i][j] -= conductance
            else:
                B[i] += conductance * known_voltage[other]

print("\nCoefficient Matrix (A):")
for row in A:
    print(["{:.4f}".format(x) for x in row])

print("\nRHS Vector (B):")
print(["{:.4f}".format(x) for x in B])

# Initial guess
x0 = [0.0] * m

# Solve using Gauss-Jacobi
solution = gauss_jacobi(A, B, x0, 1e-10, 100)

print("\nSolution (Unknown Node Voltages):")
for i, node in enumerate(unknown):
    print(f"Voltage at node {node} = {solution[i]:.6f} V")