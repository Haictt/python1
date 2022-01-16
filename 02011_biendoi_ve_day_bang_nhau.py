n = int(input())
num = [int(x) for x in input().split()]
Min = sum(num)
key = 0
for i in range(len(num)):
    res = 0
    for j in num:
        res += abs(num[i]-j)
    if Min > res:
        Min = res
        key = i
print(Min,num[key])