t=int(input())
for i in range(t):
    str=input()
    str2=str[::-1]
    cnt=0
    for j in range(1,len(str)):
        if abs(ord(str[j])-ord(str[j-1])) != abs(ord(str2[j])-ord(str2[j-1])):
            cnt = 1
    if cnt == 1:
        print("NO")
    else:
        print("YES")