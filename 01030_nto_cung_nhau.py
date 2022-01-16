def UCLN(a,b):
    a=int(a)
    b=int(b)
    if(a<b):
        a,b=b,a
    while(a % b != 0):
        a,b=b,a%b
    return b
n,k = [int(x) for x in input().split()]
cnt = 0
for i in range (10**(k-1),10**k - 1):
    if cnt == 10:
        print("")
        cnt = 0
    if UCLN(i,n) == 1:
        print(i,end=' ')
        cnt+=1