import re
def chuanHoa(a):
    res=''
    arr = re.sub(r'[\s]+',' ',a)
    arr = arr.replace(' ,',', ')
    arr = arr.replace('  ',' ')
    return arr.strip().capitalize()
text = ''
while True: 
    try: 
        str = input()
        
        text += str + " " 
    except EOFError: 
        break

arr = re.split(r'[\.!\?]',text)
for i in arr:
    print(chuanHoa(i))