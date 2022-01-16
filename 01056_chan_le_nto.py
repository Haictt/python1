from math import sqrt
def index(a):
    for i in range(len(a)):
        if (i % 2 == 0 and int(a[i]) % 2 != 0) or (i % 2 == 1 and int(a[i]) % 2 != 1):
            return False
    return True
def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def sum_digit(a):
    sum = 0
    for i in a:
        sum += int(i)
    return str(sum)
t = int(input())
for i in range(t):
    num = input()
    if isPrime(sum_digit(num)) and index(num):
        print("YES")
    else:
        print("NO")