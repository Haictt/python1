num = input()
res = []
for i in range(0,len(num),2):
    res.append(num[i:i+2])
if len(num) % 2 == 1:
    res.pop(int(len(num)/2))
print(" ".join(sorted(set(res))))