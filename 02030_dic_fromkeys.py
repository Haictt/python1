from math import sqrt
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
n = int(input())
num = [int(x) for x in input().split()]
num = list(dict.fromkeys(num))#set without sorting the list(from py3.7)
check = 0
for i in range(len(num)):
    if isPrime(sum(num[0:i+1])) and isPrime(sum(num[i+1:len(num)])):
        print(i)
        check = 1
        break
if check == 0:
    print("NOT FOUND")