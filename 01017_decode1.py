t = int(input())
for i in range(t):
    str1=input()
    str2=''
    l = len(str1)
    x=0
    while(len(str1)!= 0):
        str3=str1.lstrip(str1[0])
        x = l-len(str3)
        str2+=str(str1.count(str1[0],0,x))+str1[0]
        str1=str1.lstrip(str1[0])
        l = len(str1)
    print(str2)