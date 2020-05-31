def duplicate(list):
    t = []
    for i in list:
        if i not in t:
            t.append(i)
    return t
n = int(input("enter the no of elements you want to add in list:"))
print("enter the elements one by one")
list = []
for x in range(0,n):
    elements = int(input())
    list.append(elements)
print("list after removing duplicates is:",duplicate(list))
