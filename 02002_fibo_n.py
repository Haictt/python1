def fibo(a,b):
    arr = ['1','1']
    while(len(arr) != b):
        arr.append(str(int(arr[len(arr)-1]) + int(arr[len(arr)-2])))
    return arr[a-1:b]
t = int(input())
for i in range(t):
    a,b=[int(x) for x in input().split()]
    print(" ".join(fibo(a,b)))