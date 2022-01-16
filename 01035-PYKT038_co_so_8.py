def to_10(a):
    cnt=0
    for i in range(len(a)):
        if a[i]=='1':
            if i == 0:
                cnt+=4
            if i == 1:
                cnt+=2
            if i == 2:
                cnt+=1
    return str(cnt)
a = input()
if len(a)%3 != 0:
    a = '0' * (3-len(a)%3) + a 
x = int(len(a)/3)
Str=''
for i in range (1,x+1):
    Str+= to_10(a[3*i-3:3*i])
print(Str)
