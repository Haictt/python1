t = int(input())
for i in range(1,t+1):
    str1=input()
    str2=input()
    print(f'Test {i}: ',end='')
    if sorted(str1)==sorted(str2):
        print("YES")
    else:
        print("NO")