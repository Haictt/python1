def convert_number(a,b): #a:số hệ 10 , b:hệ cơ số cần chuyển
    Str=''
    remain = a
    m = 0               #m:số dư
    while remain > 0:
        m = remain % b  
        if b > 10:
            if m >= 10:
                Str += str(chr(m + 55))
            else:
                Str += str(m)
        else:
            Str += str(m)
        remain = int(remain/b)
    return "".join(reversed(Str))   #đảo lại
t = int(input())
for i in range(t):
    a,b = [int(x) for x in input().split()]
    print(convert_number(a,b))
