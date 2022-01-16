t = input()
arr = [int(x) for x in input().split()]
a =[]
b =[]
cnt = 0
for i in range(len(arr)-1):
    if arr[i] * arr[i+1] > 0:
        cnt += 1
        a.append(arr[i])
        b.append(arr[i+1])
if cnt > 0:
    print(cnt,a[cnt-1],b[cnt-1])
else:
    print(0)
