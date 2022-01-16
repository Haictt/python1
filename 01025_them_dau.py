num=input()
remain=len(num)%3
gr3=len(num)
str2=''
if remain != 0:
    for i in range(remain):
        str2 += num[i]
for i in range(remain,gr3):
    if (i-remain) % 3 == 0 and i != 0:
        str2 += ','+num[i]
    else:
        str2 += num[i]
print(str2)