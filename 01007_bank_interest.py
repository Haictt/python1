t=int(input())
for i in range(t):
    a,b,c=(float(i) for i in input().split())
    years=0
    while (a-c<0):
        a+=a*b/100
        years+=1
    print(years)