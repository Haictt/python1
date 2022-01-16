def UCLN(a,b):
    a=int(a)
    b=int(b)
    if(a<b):
        a,b=b,a
    while(a % b != 0):
        a,b=b,a%b
    return b
t = int(input())
for i in range(t):
    num = input()
    if UCLN(num,num[::-1]) == 1:
        print("YES")
    else:
        print("NO")