num = input()
k = int(input())
res = []
dic = {}
for i in range(0,len(num),2):
    res.append(num[i:i+2])
if len(num) % 2 == 1:
    res.pop(len(res)-1)
for i in res:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
check = 0
for i in sorted(dic):
    if dic[i] >= k:
        print(i,dic[i])
        check = 1
if check == 0:
    print("NOT FOUND")