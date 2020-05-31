# Find the smallest positive number missing from the list
a = int(input("enter the elements of the list:"))
b = []
for i in range(a):
    c = int(input("enter an integer :"))
    b.append(c)
    print("" ,c)

d = min(b)
e = max(b)
for j in range(d , e+1):
    if j in list(b):
        continue
    else:
        print("smallest missing number is ", j)
        break
