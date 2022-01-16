class Phanso:
    def __init__(self,tuso,mauso):
        self.tuso = tuso
        self.mauso = mauso
    def rutGon(self):
        ucln = self.UCLN(self.tuso, self.mauso)
        self.tuso //= ucln
        self.mauso //= ucln
        return f"{self.tuso}/{self.mauso}"
    def UCLN(self,a,b):
        while(b != 0):
            a,b = b,a % b
        return a
if __name__ == "__main__":
    a,b = [int(x) for x in input().split()]
    p = Phanso(a,b)
    print(p.rutGon())