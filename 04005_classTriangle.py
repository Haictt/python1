from math import sqrt
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
            self.chuvi()
    def kc(self,x1,y1,x2,y2):
        return sqrt((x2-x1)**2+(y2-y1)**2)
    def chuvi(self):
        res = self.kc(self.x1,self.y1,self.x2,self.y2) + self.kc(self.x1,self.y1,self.x3,self.y3) + self.kc(self.x2,self.y2,self.x3,self.y3)
        print("%.3f" % res)
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a = input().split()
        tg = Triangle(float(a[0]),float(a[1]),float(a[2]),float(a[3]),float(a[4]),float(a[5]))
        tg.checkTriangle()


