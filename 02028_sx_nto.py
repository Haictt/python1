from math import sqrt
def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
n = int(input())
num = [int(x) for x in input().split()]
pos = []
prime = []
for i in num:
    if isPrime(i):
        pos.append("1")
        prime.append(i)
    else:
        pos.append("0")
prime = sorted(prime)
x = 0
for i in range(len(pos)):
    if pos[i] == "1":
        print(prime[x],end=' ')
        x+=1
    else:
        print(num[i],end=' ')