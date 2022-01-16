def is_TN(a):
    str2=a[::-1]
    if str2 == a:
        return True
    else:
        return False
def is_even_digit(a):
    for i in a:
        if int(i) % 2 != 0:
            return False
    return True
t=int(input())
for i in range(t):
    num=input()
    for j in range(22,int(num)):
        Str=str(j)
        if (is_TN(Str) and is_even_digit(Str) and len(Str)%2==0):
            print(j, end=" ")
    print("\n")