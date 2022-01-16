a = [int(x) for x in input().split()]
b =[0,0,0,0]
while a != b:
    cnt = 0
    while a[0] != a[1] or a[0] != a[2] or a[0] != a[3]:
        a[0],a[1],a[2],a[3]=abs(a[0]-a[1]),abs(a[1]-a[2]),abs(a[2]-a[3]),abs(a[3]-a[0])
        cnt+=1
    print(cnt)
    a = [int(x) for x in input().split()]