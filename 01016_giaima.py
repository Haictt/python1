t=int(input())
for i in range(t):
    n=input()
    str2=''
    for j in range(0,len(n)):
        if n[j].isdigit():
            str2 += n[j-1]*int(n[j])
    print(str2)
