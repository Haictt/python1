n =int(input())
sum = 0
for i in range(n):
    num = [int(x) for x in input().split()]
    for j in range(n-i-1):
        sum += num[j]
    for k in range(n-i,n):
        sum -= num[k]
x = int(input())
if (abs(sum) <= x):
    print("YES")
else:
    print("NO")
print(abs(sum))