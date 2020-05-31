#rpogram to find the highrst product possible using triplets  of elements of given array
import itertools
a = int(input("enter the number of elements of list"))
b = []
for i in range(a):
    c = int(input("enter an integer:"))
    try:
        b.append(c)
    except:
        break
z = []
d = itertools.permutations(b , 3)
for j in list(d):
    k = list(j)
    for n in list(k):
        p = k[0]*k[1]*k[2]
        z.append(p)
z.sort()
print(z)
print("highest product possible is :",z[len(z) - 1])
