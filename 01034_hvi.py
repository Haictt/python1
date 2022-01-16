t = int(input())
for i in range(t):
    num = input()
    num = num.lstrip('0')
    i=len(num) - 1
    if num == '':
        print("-1")
    else:
        while (int(num[i]) >= int(num[i-1])) and i > 0:
            i-=1
        if i <= 0:
            print("-1")
        else:
            key = i - 1                 #giá trị cần hoán đổi
            str1 = num[key+1:len(num)]    #xâu bên phải giá trị key
            str2=''
            str3=''
            for j in range(key):
                str2 += num[j]
            for j in range(i,len(num)): #tìm giá trị lớn nhất < key
                if num[j]<num[key]:     #       ''
                    str3 += num[j]      #       ''
            str2 += max(str3)           #thêm giá trị đó vào str2(gọi là x)
            str1=str1.replace(max(str3),num[key],1) #loại bỏ giá trị x khỏi xâu str1
            for j in str1:              #thêm xâu còn lại vào str2
                str2+=j
            if(str2[0]=='0'):
                print("-1")
            else:
                print(str2)
            