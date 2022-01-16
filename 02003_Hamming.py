from math import log
def solve():
    arr = []
    for i in range(0,int(log(10**18,2))+1):
        for j in range(0,int(log(10**18,3))+1):
            for k in range(0,int(log(10**18,5))+1):
                if 2**i * 3**j * 5**k < 10**18:
                    arr.append(2**i * 3**j * 5**k)
    return sorted(arr)
t = int(input())
arr = solve()
for i in range(t):
    num = int(input())
    if num in arr:
        print(arr.index(num)+1)
    else:
        print('Not in sequence')
    