n = 10
arr=[]
while n > 0:
    num = [int(x) for x in input().split()]
    n -= len(num)
    arr.extend(num)
arr = sorted(arr)
b=list(set(map(lambda x:x%42,arr)))
print(len(b))
