str1=input()
str2=input()
p=int(input())
str3 = str1[0:p-1] + str2 + str1[p-1:]
print(str3)