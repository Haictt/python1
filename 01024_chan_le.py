def sum_digit_10(a):
    sum=0
    for i in a:
        sum+=int(i)
    if sum % 10 == 0:
        return True
    return False
def digit_diff_2(a):
    for i in range(1,len(a)):
        if abs(int(a[i])-int(a[i-1])) != 2:
            return False
    return True
t = int(input())
for i in range(t):
    num = input()
    if sum_digit_10(num) and digit_diff_2(num):
        print("YES")
    else:
        print("NO")