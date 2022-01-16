t=int(input())
for i in range(t):
    num = input()
    res=''
    remember = 0
    j = len(num) - 1
    while j >= 1:
        if int(num[j]) + remember >= 5:
            res = '0' + res
            remember = 1
        else:
            res = '0' + res
            remember = 0
        j-=1
    res = str(int(num[0]) + remember) + res
    print(res)
            