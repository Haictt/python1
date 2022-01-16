from math import sqrt
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def first_n(n):
    prime = []
    i = 2
    while(len(prime) != n):
        if isPrime(i):
            prime.append(i)
        i+=1
    return prime
n,x=[int(x) for x in input().split()]
print(x,end=' ')
for i in first_n(n):
    print(x+i,end=' ')
    x += i