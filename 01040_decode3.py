D = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #dictionary
def rotate(a,b):
    Str=''
    for i in a:
        Str += D[(ord(i)-65+b) % 26]
    return Str
t=int(input())
for i in range(t):
    num = input()
    r1,r2=0,0
    res=''
    str1=num[0:int(len(num)/2)]
    str2=num[int(len(num)/2):len(num)]
    for i in str1:
        r1 += ord(i) - 65
    for i in str2:
        r2 += ord(i) - 65
    str3=rotate(str1,r1)
    str4=rotate(str2,r2)
    for i in range(len(str1)):
        res += rotate(str3[i],ord(str4[i])-65)
    print(res)