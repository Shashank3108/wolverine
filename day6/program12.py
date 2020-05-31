# [rogram for longest prefix
arr = ["mint" , "mini","mineral"]
if not arr:
    print("longest common prefix:" , "")
elif len(arr) == 1:
    print("longest coommon prefix :" , arr[0])
else:
    arr.sort()
    result = ""
    for i in range(len(arr[0])):
        if arr[0][i] == arr[-1][i]:
            result += arr[0][i]
        else:
            break
    print("longest common prefix:", result)
