n = int(input())
while n != 0:
    arr = []
    for i in range(n):
        num = input()
        arr.append(num.lstrip('0'))
    arr=sorted(set(arr),key=int)
    if(len(arr)) == 1:
        print("BANG NHAU")
    else:
        print(arr[0],arr[len(arr)-1])
    n = int(input())