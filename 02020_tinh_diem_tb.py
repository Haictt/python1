n = int(input())
mark = [float(x) for x in input().split()]
cnt = 0
Sum = 0
for i in mark:
    if i != max(mark) and i != min(mark):
        Sum += i
        cnt +=1
print('%.2f'% (Sum/cnt))