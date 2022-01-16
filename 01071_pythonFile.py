import re
arr = input().lower()
res = re.search(r"\.(?=py$)",arr)
if res:
    print('yes')
else:
    print('no')