size = int(input("enter the no of elements to add in library:"))
diction = dict()
for i in range(size):
    key = input("enter the key for the items" " " + str(i+1) +  " " " in dictionary:")

    value =int(input("enter the value for items"  "  "+ str(i+1) + " " "in dictionary:"))
    diction[key] = value
print("the second max value is:", list(sorted(diction.values()))[-2])
