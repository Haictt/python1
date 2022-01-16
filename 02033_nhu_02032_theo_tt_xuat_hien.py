num = input()
res = []
for i in range(0,len(num),2):
    if num[i:i+2] not in res:
        res.append(num[i:i+2])
if len(num) % 2 == 1:
    res.pop(len(res)-1)
print(" ".join(res))