def gauss_seidal(A,b,x_old,TOL,KMAX):
    n=len(b)
    for k in range(1,KMAX+1):
        x_new = x_old.copy()
        for i in range(n):
            summ=0
            for j in range(i):
                summ+=A[i][j]*x_new[j]
            for j in range(i+1,n):
                summ+=A[i][j]* x_old[j]
            x_new[i]=(b[i]-summ)/A[i][i]
        error = max(abs(x_new[i]-x_old[i]) for i in range(n))
        print(f"Iteration {k}: {x_new}")
        print(f"Error: {error}")
        if error<=TOL:
            break
        x_old=x_new.copy()
    return x_new

n=int(input("Enter no.of equ: "))
A=[]
print("Enter coeff. matrix: ")
for i in range(n):
    row = list(map(float,input(f"Row {i+1}: ").split()))
    A.append(row)
b = list(map(float,input("Enter RHS value: ").split()))
x0=list(map(float,input("Enter inital guess values: ").split()))
TOL=float(input("Enter tolerance value: "))
KMAX=int(input("Enter maximum no. of iteration: "))
ans = gauss_seidal(A,b,x0,TOL,KMAX)
print("\nFinal Answer: ")
for i in range(n):
    print(f"x{i+1} = {ans[i]}")