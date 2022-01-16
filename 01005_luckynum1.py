num=input()
cnt=0
for i in range(len(num)):
    if num[i]=='4' or num[i]=='7':
        cnt+=1
if cnt==7 or cnt==4:
    print("YES")
else:
    print("NO")