from equSolving import EquationSolving

def gauss_seidal(A, b, x, n, tol, max_iter):
    for k in range(max_iter):
        old = x.copy()

        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s += A[i][j] * x[j]
            x[i] = (b[i] - s) / A[i][i]

        error = 0
        for i in range(n):
            error = max(error, abs(x[i] - old[i]))

        if error < tol:
            print("Converged in", k + 1, "iterations")
            return x

    return x

known = {}
print("Known Voltages:")
known[1] = float(input("V1 = "))
known[6] = float(input("V6 = "))

unknown = [2, 3, 4, 5]
index = {2: 0, 3: 1, 4: 2, 5: 3}

m = int(input("Enter no. of resistors: "))
edges = []

print("Enter Node1 Node2 Resistance:")
for i in range(m):
    u, v, r = input().split()
    edges.append((int(u), int(v), float(r)))

n = len(unknown)

A = [[0 for _ in range(n)] for _ in range(n)]
b = [0 for _ in range(n)]

for node in unknown:
    row = index[node]
    for u, v, R in edges:
        if node == u:
            other = v
        elif node == v:
            other = u
        else:
            continue

        g = 1 / R
        A[row][row] += g

        if other in index:
            A[row][index[other]] -= g
        else:
            b[row] += g * known[other]

print("\nCoefficient Matrix:")
for row in A:
    print(row)

print("\nRHS Vector:")
print(b)

initial = list(map(float, input("Enter initial values (4 values): ").split()))

tol = float(input("Tolerance: "))
max_iter = int(input("Maximum iterations: "))

helpers = EquationSolving()

# voltages = gauss_elimination(n,A,b)
voltages = gauss_seidal(A, b, initial, n, tol, max_iter)

known[2] = voltages[0]
known[3] = voltages[1]
known[4] = voltages[2]
known[5] = voltages[3]

print("\nNode Voltages:")
for i in range(1, 7):
    print("V{} = {:.6f} V".format(i, known[i]))

print("\nBranch Currents:")
for u, v, R in edges:
    cur = (known[u] - known[v]) / R
    print("I({}->{}) = {:.6f} A".format(u, v, cur))