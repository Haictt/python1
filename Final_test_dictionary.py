t = int(input())
dic = {}
arr2 = []
sum = 0
for i in range(t):
    Str = input()
    arr = Str.split(' ')
    sum += len(arr)
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1
for i in sorted(sorted(dic), key=dic.get, reverse=True):
    print(i, "{:.2f}".format(dic[i]/sum))
