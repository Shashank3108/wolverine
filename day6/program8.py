# rptate a matrix by 90 degrees clockwise
import numpy as np
a = int(input("enter index of matrix"))
b =[]
print("enter the matrix element rowwise:-")
for i in range(a):
    c = []
    for j in range(a):
        c.append(int(input(f"enter the{i +1}row{j+1}coloum entry:- ")))
    b.append(c)
def print_matrix(z):
    for i in range(len(z)):
        for j in range(len(z)):
            print(z[i][j], end= "")
        print()
print("original matrix is :-")
print_matrix(b)
degrees = {"90": 1, "180":2 ,"270":3}
c = np.rot90(b , 4-degrees["90"])
print("matrixafter rotation (clockwise):-")
print_matrix(c)
