from math import sqrt
def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
t = int(input())
for i in range(t):
    num = input()
    cnt=0
    for i in num:
        if isPrime(i):
            cnt+=1
    if cnt > len(num) - cnt and isPrime(len(num)):
        print("YES")
    else:
        print("NO")