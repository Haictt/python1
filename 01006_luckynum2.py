t=int(input())
for j in range(t):
    num=input()
    cnt=0
    for i in range(len(num)):
        if num[i]!='4' and num[i]!='7':
            cnt=1
            break
    if cnt==1:
        print("NO")
    else:
        print("YES")