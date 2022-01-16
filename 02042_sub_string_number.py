a = input()
b = input()
negative = 0
while len(a) != len(b):
    if len(a) < len(b):
        a='0'+a
    elif len(b) < len(a):
        b='0'+b
for i in range(len(a)):         #check so lon hon
    if int(a[i]) < int(b[i]):
        a,b=b,a
        negative = 1
        break
    elif int(a[i]) > int(b[i]):
        break
re = 0 #bien nho
pos = len(a) - 1
res =''
for i in range(pos,-1,-1):
    if int(a[i]) < int(b[i]) + re:
        num = 10 + int(a[i])
    else:
        num = int(a[i])
    res = str(num-int(b[i])-re) + res
    if len(str(num)) == 2:
        re = 1
    else:
        re = 0
arr = ''.join(set(res))
if arr == '0':
    print(arr)
else:
    if negative == 1:
        print('-'+res.lstrip('0'))
    else:
        print(res.lstrip('0'))
