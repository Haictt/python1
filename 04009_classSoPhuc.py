class soPhuc:
    def __init__(self,phanThuc,phanAo):
        self.phanThuc = phanThuc
        self.phanAo = phanAo
    def total(a,b):
        return soPhuc(a.phanThuc + b.phanThuc, a.phanAo + b.phanAo)
    def multi(a,b):
        return soPhuc(a.phanThuc * b.phanThuc - a.phanAo * b.phanAo,a.phanThuc * b.phanAo + a.phanAo * b.phanThuc)
    def res(self):
        if self.phanAo < 0:
            return f'{self.phanThuc} - {self.phanAo*-1}i'
        else:
            return f'{self.phanThuc} + {self.phanAo}i'
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a,b,c,d=[int(x) for x in input().split()]
        sP1= soPhuc(a,b)
        sP2= soPhuc(c,d)
        C = soPhuc.multi(soPhuc.total(sP1,sP2),sP1)
        D = soPhuc.multi(soPhuc.total(sP1,sP2),soPhuc.total(sP1,sP2))
        print(f'{C.res()}, {D.res()}')
