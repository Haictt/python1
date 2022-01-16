def toPalindrome(x):#x2 số đã ganerate tạo ra binary palindrome numbers
    tmp,a,b = '','',''
    for i in x:
      tmp += str(i)
    a = tmp + '0' +tmp[::-1]
    b = tmp + '1' +tmp[::-1]
    tmp += tmp[::-1]
    lst.extend((a,b,tmp))
def bin_gen(i,n):#generate số nhị phân
   for j in range(1,-1,-1):
        x[i] = j
        if i == n-1:
            toPalindrome(x)
        else:
            bin_gen(i+1,n)
def toDecimal(str):
    decimal = 0
    for digit in str:
        decimal = decimal*2 + int(digit)
    return decimal
lst = ["0","1","11","101","111"]
for i in range(2,11):#11 chữ số 1 ở binary là max tầm 2m ở decimal
    x = i*[0]
    x[0] = 1
    bin_gen(1,i)
lst2 = sorted(list(map(toDecimal,lst)))#list những số TN ở base 2
a,b,M = [int(item) for item in input().split()]
lst = [0, 1, 6643, 1422773]#chỉ có 2 số này palin ở cả base 2 và 3, k có số nào <2m palin ở cả 2,3,4
lst1 = [0, 1] #0,1 auto palin ở all base
#bat dau:
if M >= 4:
    count = 0
    for i in lst1:
        if i >= a and i <= b:
            count += 1
    print(count)
elif M == 3:
    count = 0
    for i in lst:
        if i >= a and i <= b:
            count += 1
    print(count)
else:
    count = 0
    for i in lst2:
        if i>=a and i<=b:
            count += 1
    print(count)
