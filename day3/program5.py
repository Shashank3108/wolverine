# how to get an intersection of two python lists
def intersection(list1 ,list2):
    return list(set(list1) & set(list2))


n1 = int(input("enter the no of elements in list1 :"))
print("enter the elements in list1 one by one:")
list1 = []
for i in range(0,n1):
    list1.append(input())
n2 = int(input("enter the no of the  elements of list2:"))
print("enter the elements in the list2 one by one: ")
list2 = []
for i in  range(0,n2):
    list2.append(input())
print("the intersection of two given lists list1 and list2 are:",intersection(list1 , list2))
