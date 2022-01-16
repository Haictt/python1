t=int(input())
for i in range(t):
    num = input()
    a=len(num)
    if (num[0]+num[1]==num[a-2]+num[a-1]):
        print("YES")
    else:
        print("NO")
