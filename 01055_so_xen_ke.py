def odd_index(a):
    return len(set(a[::2]))==1
t = int(input())
for i in range(t):
    num = input()
    if len(num) % 2 == 1 and num[0] != num[1] and odd_index(num):
        print("YES")
    else:
        print("NO")