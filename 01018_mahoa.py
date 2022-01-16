P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_." #encode
case = input()
while (case != '0'):
    k,s=case.split(" ")
    str2=''
    for i in s:
        str2 = str2 + P[(P.index(i)+int(k))%28]
    print(str2[::-1])
    case = input()