def UCLN(a,b):
    a=int(a)
    b=int(b)
    if(a<b):
        a,b=b,a
    while(a % b != 0):
        a,b=b,a%b
    return b
a , b = [int(x) for x in input().split()]
j = a+1
for i in range(a,b-1):
    for j in range(i+1,b):
        if UCLN(i,j) == 1:
            for k in range(j+1,b+1):
                if UCLN(i,k) == 1 and UCLN(k,j) == 1:
                    print(f'({i}, {j}, {k})')
