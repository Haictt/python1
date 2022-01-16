class Rectangle:
    def __init__(self,a,b,c):
            self.a = a
            self.b = b
            self.c = c
    def perimeter(self):
        return (self.a + self.b) * 2
    def area(self):
        return self.a * self.b
    def color(self):
        return self.c.title()
def int(a):
    if a.isnumeric():
        rtr=0
        for c in a:
            rtr=rtr*10 + ord(c) - ord('0')
        return rtr
    elif a.isalpha():
        return a
    else: #check if a < 0 (-a will return false because a is not numeric)
        return False
arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')
