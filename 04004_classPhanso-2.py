class Phanso:
    def __init__(self,tuso,mauso):
        self.tuso = tuso
        self.mauso = mauso
    def rutGon(self):
        ucln = self.UCLN(self.tuso, self.mauso)
        self.tuso //= ucln
        self.mauso //= ucln
        
    def UCLN(self,a,b):
        while(b != 0):
            a,b = b,a % b
        return a
    def add(a,b):
        c = Phanso(a.tuso * b.mauso + b.tuso*a.mauso , a.mauso*b.mauso)
        c.rutGon()
        print(f"{c.tuso}/{c.mauso}")
if __name__ == "__main__":
    a,b,c,d = [int(x) for x in input().split()]
    x = Phanso(a,b)
    y = Phanso(c,d)
    Phanso.add(x,y)
        