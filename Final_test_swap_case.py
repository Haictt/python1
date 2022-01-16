s = input()
s2=''
for i in s:
    if i.isupper():
        s2+=i.lower()
    elif i.islower():
        s2+=i.upper()
    else:
        s2+=i
print(s2)