t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    count = {}
    for i in range(n):
        num = int(input())
        arr.append(num)
    str2 = sorted(set(arr))
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    key = max(count.values())
    for i in str2:
        if count[i] == key:
            print(i)
            break
        
