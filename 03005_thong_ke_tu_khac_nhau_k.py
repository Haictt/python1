n,k = [int(x) for x in input().split()]
Str=''
while n > 0:
    array = input()
    n-=1
    Str+=array + ' '
lst,dic =[], {}
start,end,i = 0,0,0 #vi tri bat dau va end cua 1 tu
while i < len(Str):
    if not Str[i].isalnum():
        end = i
        lst.append(Str[start:end].lower())
        start = end
        while start < len(Str):
            if not Str[start].isalnum():
                start+=1
            else:
                break
        i = start
    else:
        i+=1
lst = sorted(lst)
for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in sorted(dic,key=dic.get,reverse=True):
    if (dic[i] >= k):
        print(i,dic[i])