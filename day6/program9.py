# merge the k  sorted lists and return a one sorted list
a = int(input("enter  number of lists elements :-"))
d = []
for i in range(a):
    x = int(input("enter the number of lists elements is :-"))
    b = []
    for j in range(x):
        c = int(input("enter the list elements :-"))
        b.append(c)
    b.sort()
    d = d +b
d.sort()
print(d)
