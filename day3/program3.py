def duplicate(str):
    t = set(str)
    t = ""
    for i in str:
        if i  in t:
            pass
        else:
            t=t+i
    print("the string after removing duplicates :",t)
str = input("inter the string:")
duplicate(str)
