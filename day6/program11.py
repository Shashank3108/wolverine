# for spiral and transpose matrix
a = int(input("enter the number of  rows of matrix:"))
b = int(input("enter the number of coloums of matrix:"))
d =[]
for i in range(a):
    e = []
    for j in range(b):
        c = int(input(f"enter {i+1}th row {j+1}th coloum element:-"))
        e.append(c)
    d.append(e)

def spiral_matrix(m,n,f):
    k = 0
    l = 0
    while k<m and l<n :
        for i in range(l , n):
            print(f[k][i], end = "")
        k+=1
        for i in range(k , m):
            print(f[i][n-1] , end = "")
        n-=1
        if k<m:
            for i in range(n-1 , (l-1) , -1):
                print(f[m-1][i] , end = "")
        m-=1
        if l<n:
            for i in range(m-1 , k-1 ,-1):
                print(f[i][l], end = "")
            l+=1
def print_matrix(z):
    for i in range(len(z)):
        for j in range(len(z)):
            print(z[i][j] , end = "")
        print()


def transpose(c):
    for i in range(len(c)):
        for j in range(i, len(c)):
            c[i][j], c[j][i] = c[j][i], c[i][j]




print("original matrix is:")
print_matrix(d)
print("transposed matrix:")
transpose(d)
print_matrix(d)
print("matrix in spiral form :-")
spiral_matrix(a,b,d)
