from math import sqrt
def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def index_prime(a):
    for i in range(len(a)):
        if (isPrime(i) and (a[i] != '2' and a[i] !='3' and a[i] !='5' and a[i] !='7')) or ((not isPrime(i)) and (a[i] == '2' or a[i] =='3' or a[i] =='5' or a[i] =='7')) :
            return False
    return True
t = int(input())
for i in range(t):
    num = input()
    if index_prime(num):
        print("YES")
    else:
        print("NO")