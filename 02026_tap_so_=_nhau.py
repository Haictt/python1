x,y = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a = sorted(set(a))
b = sorted(set(b))
if a == b:
    print("YES")
else:
    print("NO")
