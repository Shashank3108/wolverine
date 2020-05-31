# given a list and a number k, where k is the smaller than size of lists , find the kth smallest number of list
a = int(input("enter the size of the list:-"))
b = []
for i in range(a):
    c =int(input("enter an integer:-"))
    b.append(c)
b.sort()
k = int(input("enter the number less than {a} to find kth smallest number:-"))
print(f"{k}th smallest number is", b[k-1])
