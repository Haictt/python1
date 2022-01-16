t = int(input())
arr = [int(x) for x in input().split()]
cnt = 0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            cnt+=1
print(cnt)