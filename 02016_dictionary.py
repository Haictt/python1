t = int(input()) #dictionary : dic{}
for i in range(t):
    n = int(input())
    str1 = input().split()
    str1 = sorted(str1)
    str2 = set(sorted(str1))
    dic={}#khoi tao dictionary
    for i in str1:#them phan tu vao dic
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    key = max(dic.values())
    if key <= int(n/2):
        print("NO")
    else:
        for i in str2:
            if dic[i] == key:
                print(i)
                break

