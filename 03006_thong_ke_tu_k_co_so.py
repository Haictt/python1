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
        word=''
        for i in Str[start:end]:
            if i.isalpha():
                word+=i
        if word != '':
            lst.append(word.lower())
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