# given an unsorted array of size n find first element such that it is smaller than right one and graeter than left one
a = int(input("enter size of array:-"))
b = []
for i in range(a):
    c = int(input("enter element of array:-"))
    try:
        b.append(c)
    except:
        break
for j in range(1 ,len(b)):
    if b[j-1] <b[j] <b[j+1]:
        print(b[j])
        break
    else:
        continue
