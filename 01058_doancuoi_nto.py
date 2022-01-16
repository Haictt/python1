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
    if isPrime(num[len(num)-4:len(num)]):
        print("YES")
    else:
        print("NO")


