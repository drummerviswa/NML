def gauss_jacobi(A,b,x_old,TOL,KMAX):
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
n = int(input("Enter no. of equ: "))
A=[]
print("Enter the coeff. matrix: ")
for i in range(n):
    row = list(map(float,input(f"Row {i+1}: ").split()))
    A.append(row)
b = list(map(float,input("Enter RHS value: ").split()))
x0=list(map(float,input("Enter inital guess values: ").split()))
TOL=float(input("Enter tolerance value: "))
KMAX=int(input("Etner maximum no. of iteration: "))
ans = gauss_jacobi(A,b,x0,TOL,KMAX)
print("\nFinal Answer: ")
for i in range(n):
    print(f"x{i+1} = {ans[i]}")