from math import sqrt
def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
n,m = [int(x) for x in input().split()]
matrix = []
MAX = 0
res = 0
for i in range(n):
    key = []
    num = [int(x) for x in input().split()]
    matrix.append(num)
    for i in num:
        if isPrime(i):
            key.append(i)
    if len(key) != 0:
        res = max(key)
    if MAX < res:
        MAX = res
if MAX == 0:
    print("NOT FOUND")
else:
    print(MAX)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == MAX:
                print(f"Vi tri [{i}][{j}]")

