from math import sqrt
def check(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
def total(a):
    sum = 0
    for i in range(2,int(sqrt(a))+1):
        if check(i):
            while(a%i == 0):
                sum+=i
                a/=i
    if check(a):
        sum+=a
    return sum
t = int(input())
sum = 0
for i in range(t):
    num = int(input())
    sum+=total(num)
print(int(sum))
