t = int(input())
for i in range(t):
    n = int(input())
    str1 = [int(x) for x in input().split()]
    count ={}
    str2 = set(str1)
    for i in str1:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in str2:
        if count[i] % 2 != 0:
            print(i)
            break