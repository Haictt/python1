a = input()
b = input()
while len(a) != len(b):
    if len(a) < len(b):
        a='0'+a
    elif len(b) < len(a):
        b='0'+b
re = 0 #bien nho
pos = len(a) - 1
res =''
for i in range(pos,-1,-1):
    num = str(int(a[i]) + int(b[i]) + re)
    res = str(int(num[len(num)-1])) + res
    if len(num) == 2:
        re = 1
    else:
        re = 0
res = str(re) + res
arr = ''.join(set(res))
if arr == '0':
    print(arr)
else:
    print(res.lstrip('0'))
