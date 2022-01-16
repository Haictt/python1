from math import modf,ceil,floor
class racingBoy:
    def __init__(self,name,loc,time):
        self.name = name
        self.loc = loc
        self.time = time
    def codeNumber(self):
        res = ''
        arr1 = self.loc.split(' ')
        arr2 = self.name.split(' ')
        for i in arr1:
            res += i[0]
        for i in arr2:
            res += i[0]
        return res
    def speed(self):
        time = self.time.split(':')
        hours = time[0]
        mins = time[1]
        return 120/(int(hours) - 6 + int(mins)/60)
    def Round(self):
        time = self.time.split(':')
        hours = time[0]
        mins = time[1]
        num =  modf(120/(int(hours) - 6 + int(mins)/60))
        if num[0] >= 0.5:
            return ceil(120/(int(hours) - 6 + int(mins)/60))
        else:
            return floor(120/(int(hours) - 6 + int(mins)/60))
    def res(self):
        return f'{self.codeNumber()} {self.name} {self.loc} {self.Round()} Km/h'
if __name__ == '__main__':
    t = int(input())
    racers = []
    for i in range(t):
        name = input()
        loc = input()
        time = input()
        racers.append(racingBoy(name,loc,time))
    racers.sort(reverse=True,key=racingBoy.speed)
    for i in racers:
        print(i.res())