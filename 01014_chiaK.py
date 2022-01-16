from typing import List


a,K,N = [int(x) for x in input().split()]
check = 0
Str =''
if (a>=N) or K > N:
    print("-1")
else:
    lst = list(range(K,N+1,K))
    for i in lst:
        if i > a:
            Str+=str(i-a)+' '
    if Str == '':
        print("-1")
    else:
        print(Str)
