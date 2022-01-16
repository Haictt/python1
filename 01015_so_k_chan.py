t=int(input())
for i in range(t):
    num=input()
    cnt = 0
    for j in range(len(num)-1):
        if int(num[j]) > int(num[j+1]):
            cnt = 1
    if cnt == 1:
        print("NO")
    else:
        print("YES")
    