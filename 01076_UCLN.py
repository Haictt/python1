def UCLN(a,b):
    if(a<b):
        a,b=b,a
    while(a % b != 0):
        a,b=b,a%b
    return b
t = int(input())
for i in range(t):
    a=int(input())
    b=int(input())
    print(UCLN(a,b))