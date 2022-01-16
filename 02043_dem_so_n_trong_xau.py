t = int(input())
for i in range(t):
    s = input()
    n = input()
    cnt = 0
    s=s.replace(n,'x')
    for i in s:
        if i == 'x':
            cnt+=1
    print(cnt)