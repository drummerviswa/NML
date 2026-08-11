class EquationSolving:
    def gauss_elimination(self,n, A, b):
        TOL = 1e-10
    
        # Forward Elimination
        for k in range(n - 1):
    
            # Check for zero pivot
            if abs(A[k][k]) <= TOL:
                print("The first row first column in 0")
                # Find the row with the largest pivot element
                max_row = k
                max_value = abs(A[k][k])
    
                for p in range(k + 1, n):
                    if abs(A[p][k]) > max_value:
                        max_value = abs(A[p][k])
                        max_row = p
    
                # If no suitable pivot exists
                if max_value <= TOL:
                    raise ValueError("No unique solution exists.")
    
                # Swap rows in A
                A[k], A[max_row] = A[max_row], A[k]
    
                # Swap corresponding elements in b
                b[k], b[max_row] = b[max_row], b[k]
            print(f"After {k} swap")
            # Elimination
            for i in range(k + 1, n):
                factor = A[i][k] / A[k][k]
                # print("What is the factor: ",factor)
    
                for j in range(k + 1, n):
                    A[i][j] = A[i][j] - factor * A[k][j]
                A[i][k] = 0
                b[i] = b[i] - factor * b[k]
                print(f"    -- Row operation in row: {i+1}")
    
        # Back Substitution
        x = [0] * n
    
        x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    
        for k in range(n - 2, -1, -1):
    
            sum_ax = 0
    
            for j in range(k + 1, n):
                sum_ax += A[k][j] * x[j]
    
            x[k] = (b[k] - sum_ax) / A[k][k]
    
        return x
    def gauss_jacobi(self,A,b,x_old,TOL,KMAX):
        n=len(A)
        for i in range(n):
            print(f"Old x[{i}] = {x_old[i]}")
        TAG = True
        for k in range(1,KMAX+1):
            if TAG==False:
                break
            x_new = [0]*n
            for i in range(n):
                summ=0
                for j in range(n):
                    if j!=i:
                        summ+=A[i][j]*x_old[j]
                    x_new[i]=(b[i]-summ)/A[i][i]
                    print(f"x_new[{i}] = {x_new[i]}")
                error = max(abs(x_new[i]-x_old[i]) for i in range(n))
                print(f"Iteration {k}: {x_new}")
                print(f"Error: {error}")
            if error<=TOL:
                TAG=False
            else:
                for i in range(n):
                    x_old[i]=x_new[i]
        return x_new

    def gauss_seidal(self,A, b, x, n, tol, max_iter):
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
