
N=int(input())
number_array=list(map(int,input().split()))

def findMaxNum(number_array ,t):
    hash = [0] * 10
    for i in range(t):
        hash[number_array[i]] += 1
    for i in range(9 ,-1 ,-1):
        for j in range(hash[i]):
            print(i , end = "")

if __name__ == "__main__":
    t =len(number_array)
    findMaxNum(number_array , t)
