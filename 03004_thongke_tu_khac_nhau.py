n = int(input())
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
    print(i,dic[i])
## cach 2:
import re
n = int(input())
Str=''
while n > 0:
    array = input()
    n-=1
    Str+=array + ' '
dic={}
arr=re.split(r'[^A-Za-z0-9]+',Str)
arr=list(map(lambda x:x.lower(),arr))
arr.sort()
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
asd=sorted(dic,key=dic.get,reverse=True)
for i in asd:
    if i != '':
        print(i,dic[i])
        