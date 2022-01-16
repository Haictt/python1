num = input()
num = num.replace('688',' ')
num = num.replace('68',' ')
num = num.replace('6',' ')
num = num.replace(' ','')
if num == '':
    print("YES")
else:
    print("NO")