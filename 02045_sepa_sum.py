def sum_ab(a,b):
    return str(int(a) + int(b))
num = input()
while (len(num) > 1):
    a = num[0:int(len(num)/2)]
    b = num[int(len(num)/2):len(num)]
    num = sum_ab(a,b)
    print(num)