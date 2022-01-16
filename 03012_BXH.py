t = int(input())
dic = {}
for i in range(t):
    Name = input()
    a,b =[int(x) for x in input().split()]
    dic[str(b)+'/'+Name] = a

for i in sorted(sorted(dic),key=dic.get,reverse=True):
    Name = i.split('/')
    print(f'{Name[1]} {dic[i]} {Name[0]}')

