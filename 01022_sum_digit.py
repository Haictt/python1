#bullshit
num=input()
sum,cnt = 0,0
if(len(num)==1):
    print("1")
else:
    while len(num)!=1:
        for i in range(len(num)):
            if num[i]=='-':
                sum += ord('-') - ord('0')
            else:
                sum += int(num[i])
        num = str(sum)
        sum = 0
        cnt+=1
    print(cnt)