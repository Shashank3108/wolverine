#check if the sum of fibonacci elements in an array is a fibonacci number or not
MAX = 100005
fibonacci = set()
def createhash():
    global fibonacci
    prev , curr = 0 ,1
    fibonacci.add(prev)
    fibonacci.add(curr)
    while (curr <= MAX):
        temp = curr + prev
        if temp <= MAX:
            fibonacci.add(temp)
        prev = curr
        curr = temp
def checkarray(arr , n):
    sum = 0
    for i in range(n):
        if (arr[i] in fibonacci):
            sum += arr[i]
    if (sum in fibonacci):
        return True


    return False

if __name__ == "__main__":
    arr = [ 1, 2,3 ,4 ,8 ,2]
    n = len(arr)
    createhash()
    if (checkarray(arr , n)):
        print("yes")
    else:
        print("no")
