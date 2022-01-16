#a + (a + 1) + (a + 2) + ... + (a + b)
#= (b + 1) * a + (1 + 2 + ... + b)
#= (b + 1) * a + b * (b + 1) / 2
#= (b + 1) * (a + b/2)
# => a = [(2*N) - b*(b+1)]/2*(b+1)
#Cho 1 vòng for chạy b, nếu a nguyên dương thì in ra a -> a+1 ->.....-> a + b
#limit của b:ví dụ a = 0,tổng từ 1 tới b là b(b+1) / 2 = N nên lim b = (-1 + sqrt(1+8N))/2  (giải pt bậc 2)
#Ví dụ, với n = 9 thì có 2 trường hợp:
#a = 2, b = 2
#hoặc
#a = 4, b = 1
from math import sqrt
t = int(input())
for i in range(t):
    num = int(input())
    cnt = 0
    for i in range(1,int((sqrt(num*8+1)-1)/2 + 1)):
        a = (((2*num) - i*(i+1)) / (2*(i+1)))
        check = (((2*num) - i*(i+1)) % (2*(i+1)))
        if a > 0 and check == 0:
            cnt+=1
    print(cnt)

