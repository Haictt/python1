n,m = [int(x) for x in input().split()]
matrix = []
MAX = 0
MIN = 100000
check = 0
for i in range(n):
    num = [int(x) for x in input().split()]
    matrix.append(num)
    a = max(num)
    b = min(num)
    if MAX < a:
        MAX = a
    if MIN > b:
        MIN = b
key = MAX - MIN
for i in range(n):
    for j in range(m):
        if matrix[i][j] == key:
            check = 1
            break
    if check == 1:
        break
if check == 1:
    print(key)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == key:
                print(f"Vi tri [{i}][{j}]")
else:
    print("NOT FOUND")
    
