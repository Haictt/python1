n , m = [int(x) for x in input().split()]
num = [int(x) for x in input().split()]
dic = {}
for i in num:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
key = max(dic.values())
check = 0
lst = sorted(dic,key=dic.get,reverse=True)
res = []
for i in lst:
    if dic[i] < key:
        key = dic[i]
        check = 1
        break
for i in lst:
    if dic[i] == key:
        res.append(i)
res = sorted(res)
if check == 0:
    print("NONE")
else:
    print(res[0])