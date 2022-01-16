from math import sqrt
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
    if isPrime(sum_digit(num)):
        print("YES")
    else:
        print("NO")