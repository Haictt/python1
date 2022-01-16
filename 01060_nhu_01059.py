def sum_digit(a):
    sum = 0
    for i in a:
        sum += int(i)
    return str(sum)
def mul_digit(a):
    res = 1
    for i in a:
        if i != '0':
            res *= int(i)
    return str(res)
t = int(input())
for i in range(t):
    num = input()
    even = num[0::2]
    odd = num[1::2]
    res1 = sum_digit(odd)
    res2 = mul_digit(even)
    if set(even) == {'0'}:
        res2 = '0'
    print(res2,res1)