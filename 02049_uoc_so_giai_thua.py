t = int(input())
for i in range(t):
    n,p = [int(x) for x in input().split()]
    cnt = 0
    for j in range(n+1):
        k = j
        while k % p == 0 and k != 0:
            cnt+=1
            k/=p
    print(cnt)