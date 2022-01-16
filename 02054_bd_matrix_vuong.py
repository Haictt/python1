n,m = [int(x) for x in input().split()]
matrix = []
for i in range(n):
    num = input().split()
    matrix.append(num)
cnt = abs(n-m)
for i in range(n):
    if n > m:
        if cnt > 0:
            if i % 2 != 0:
                print(' '.join(matrix[i]))
            else:
                cnt-=1
        else:
            print(' '.join(matrix[i]))
    elif n < m:
        cnt = abs(n-m)
        for j in range(m):
            if cnt > 0:
                if j % 2 == 0:
                    print(matrix[i][j],end=' ')
                else:
                    cnt-=1
            else:
                print(matrix[i][j],end=' ')
        print("")
    else:
        print(' '.join(matrix[i]))