def sum_digit(a):
    sum = 0
    for i in a:
        sum += int(i)
    return sum
t = int(input())
for i in range(t):
    num = input()
    if sum_digit(num) % 3 == 0:
        print("YES")
    else:
        print("NO")