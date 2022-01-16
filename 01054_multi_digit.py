def mul_digit(a):
    res = 1
    for i in a:
        if i != '0':
            res *= int(i)
    return str(res)
t = int(input())
for i in range(t):
    num = input()
    print(mul_digit(num))