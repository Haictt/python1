def multi_digit(n):
    sum = 1
    for i in range(len(n)):
        sum *= int(n[i])
    return sum
t = int(input())
for i in range(t):
    n = int(input())
    Str = input().split()
    Str = sorted(Str,key=int)
    Str2 = sorted(Str,key=multi_digit)
    print(" ".join(Str2))