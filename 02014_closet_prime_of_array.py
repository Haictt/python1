from math import sqrt
def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def closetPrime(n):
    n = int(n)
    a,b,cnt = n-1,n+1,1
    while not isPrime(a) and not isPrime(b):
        a-=1
        b+=1
        cnt+=1
    return cnt
n = int(input())
num = [int(x) for x in input().split()]
res,max = 0,0
for i in num:
    if not isPrime(i):
        res = closetPrime(i)
        if(max < res):
            max = res
print(max)