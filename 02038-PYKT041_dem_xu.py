def res(n):
    return int(n*(n-1)/2)
n = int(input())
arr=[]
dic={}
sum = 0
for i in range(n):
    arr.append([])
    a = input("")
    for j in range(len(a)):
        arr[i].append(a[j])
        if arr[i][j] == 'C':
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1
for i in dic.values():
    sum += res(i)
for i in range(len(arr)):
    sum += res(arr[i].count('C'))
print(sum)