n = int(input())
res=[]
for i in range(n):
    num = input()
    Str=''
    for i in range(len(num)):
        if num[i].isdigit():
            Str+=num[i]
            if i == len(num)-1:
                if Str.lstrip('0')=='':
                    res.append('0')
                else:
                    res.append(Str.lstrip('0'))
        else:
            if Str!='':
                if Str.lstrip('0')=='':
                    res.append('0')
                else:
                    res.append(Str.lstrip('0'))
            Str=''
res = sorted(res,key=int)
for i in res:
    print(i)