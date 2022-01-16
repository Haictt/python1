def sum_digit(a):
    sum = 0
    for i in a:
        sum += int(i)
    return str(sum)
def isTN(a):
    return a == a[::-1] and len(a) > 1
t = int(input())
for i in range(t):
    num = input()
    if isTN(sum_digit(num)):
        print("YES")
    else:
        print("NO")