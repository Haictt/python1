n = int(input())
arr =[]
Sum = 0
for i in range(n):
    num = [int(x) for x in input().split()]
    arr.append(num)
    Sum += sum(num)
if n == 2:
    print(f"1 {int(Sum/2-1)}")
else:
    pos = 0
    Sum = int(Sum/(2*(n-1)))
    for i in arr:
        print(int((sum(i)-Sum)/(n-2)),end=' ') 