n = int(input())
arr=[]
pos=[]
even=[]
odd=[]
x,y=0,0 #position of odd[] and even[]
while n > 0:
    num = [int(x) for x in input().split()]
    n -= len(num)
    arr.extend(num)
for i in arr:
    if i % 2 == 0:
        pos.append("1")#position of even numbers
        even.append(i)
    else:
        pos.append("0")#position of odd numbers
        odd.append(i)
even=sorted(even)
odd=sorted(odd,reverse=True)
for i in range(len(pos)):
    if pos[i] == '0':
        print(odd[x],end=' ')
        x+=1
    else:
        print(even[y],end=' ')
        y+=1
        