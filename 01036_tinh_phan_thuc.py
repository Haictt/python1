t = int(input())
for i in range(t):
    num = int(input())
    sum = 0
    if num % 2 == 0:
        for i in range(2,num+1,2):
            sum+= 1/i
    else:
        for i in range(1,num+1,2):
            sum+= 1/i
    print('%.6f'%sum)

