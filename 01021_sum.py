t=int(input())
for i in range(t):
    str1=input()
    lst1=list(str1)
    sum=0
    str2=''
    for i in range(0,len(lst1)):
        if lst1[i].isdigit():
            sum += int(lst1[i])
        else:
            str2+=lst1[i]
    str2=sorted(str2)
    str2+=str(sum)
    print("".join(str2))