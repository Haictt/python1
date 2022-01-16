t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a = sorted(a)
    b = sorted(b)
    cnt = 0
    for i in range(n):
        if a[i] > b[i]:
            cnt = 1
            break
    if cnt == 0:
        print("YES")
    else:
        print("NO")