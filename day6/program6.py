# program to find a triple (a,b,c) such that 1<a+b+c<2 from a given array
import itertools
a = int(input("enter size of array:-"))
b = []
for i in range(a):
    c = float(input("elements of the array :-"))
    try:
        b.append(c)
    except:
        break
d = itertools.permutations(b , 3)
for j in list(d):
    c = list(j)
    for k in range(3):
        if 1 < c[0] + c[1] + c[2] < 2:
            print(c)
        else:
            continue
