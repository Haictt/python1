from math import sqrt
def solve(a):
    sum = 0
    for i in range(2,int(sqrt(a)+1)):
        if a % i == 0:
            if i == int(a/i):
                sum += i
            else:
                sum = sum + i + a/i
    return int(sum-a)

t = int(input())
for i in range(t):
    cnt = 0
    a,b=[int(x) for x in input().split()]
    for i in range(a,b+1):
        j = solve(i)
        if solve(j) == i and i != j:
            cnt+=1
    print(cnt/2)