t = int(input())
for i in range(t):
    num = int(input())
    print("1",end='')
    i = 2
    while num != 1:
        cnt = 0
        while num % i == 0:
            num /= i
            cnt += 1
        if cnt != 0:
            print(f' * {i}^{cnt}',end='')
        else:
            i+=1
    print("\n")
