def is_Prime(n):
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
    if count == 1:
        return True
    return False
x,y = [int(x) for x in input().split()]
matrix = []
for i in range(x):
    matrix.append([])
    ele = [int(x) for x in input().split()]
    for j in range(y):
        if is_Prime(ele[j]):
            matrix[i].append('1')
        else:
            matrix[i].append('0')
for k in matrix:
    print(' '.join(k))


