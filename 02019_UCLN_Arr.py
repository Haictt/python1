def UCLN(a,b):
    if(a<b):
        a,b=b,a
    while(a % b != 0):
        a,b=b,a%b
    return b
n = int(input())
Str = [int(x) for x in input().split()]
Str = sorted(Str)
lst = []
x = -1
for i in range(len(Str)-1):
    for j in range(i+1,len(Str)):
        if UCLN(Str[i],Str[j]) == 1:
            x+=1
            lst.append([])
            lst[x].append(str(Str[i]))
            lst[x].append(str(Str[j]))
for i in lst:
    print(" ".join(i))
