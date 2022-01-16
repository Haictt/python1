from math import sqrt
from decimal import Decimal
class Triangle:
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
    def checkTriangle(self):
        a = (self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2))  
        if a == 0:
            print('INVALID')
        else:
            self.dientich()
    def kc(self,x1,y1,x2,y2):
        return sqrt((x2-x1)**2+(y2-y1)**2)
    def dientich(self):
        a = self.kc(self.x1,self.y1,self.x2,self.y2)  
        b = self.kc(self.x1,self.y1,self.x3,self.y3)  
        c = self.kc(self.x2,self.y2,self.x3,self.y3)
        res = (0.25)* sqrt((a+b+c)*(a+b-c)*(b+c-a)*(c+a-b))
        print("%.2f" % res)
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a = input().split()
        tg = Triangle(Decimal(a[0]),Decimal(a[1]),Decimal(a[2]),Decimal(a[3]),Decimal(a[4]),Decimal(a[5]))
        tg.checkTriangle()