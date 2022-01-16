def isTN(a):
    return a == a[::-1] and len(a) > 1
n,m = [int(x) for x in input().split()]
matrix = []
MAX = 0
res = 0
for i in range(n):
    key = []
    num = input().split()
    matrix.append(num)
    for i in num:
        if isTN(i):
            key.append(i)
    if len(key) != 0:
        res = int(max(key))
    if MAX < res:
        MAX = res
if MAX == 0:
    print("NOT FOUND")
else:
    print(MAX)
    for i in range(n):
        for j in range(m):
            if int(matrix[i][j]) == MAX:
                print(f"Vi tri [{i}][{j}]")
