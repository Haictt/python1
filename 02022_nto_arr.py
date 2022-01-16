from math import sqrt
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
n = int(input())
str = [int(x) for x in input().split()]
arr = {}
for i in str:
    if isPrime(i):
        if i in arr :
            arr[i] += 1
        else:
            arr[i] = 1
for i in arr:
    print(i,arr[i])