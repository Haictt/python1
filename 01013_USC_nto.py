def UCLN(a,b):
    if(a<b):
        a,b=b,a
    while(a % b != 0):
        a,b=b,a%b
    return b
def is_Prime(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
    if count == 1:
        return True
    return False
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
t=int(input())
for i in range(t):
    x,y = [int(x) for x in input().split()]
    num = UCLN(x,y)
    if is_Prime(sum_digits(num)):
        print("YES")
    else:
        print("NO")
