class Student:
    def __init__(self,name,dob,mark1,mark2,mark3):
        self.name = name
        self.dob = dob
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def res(self):
        mark = "%.1f" % (self.mark1+self.mark2+self.mark3)
        print(f"{self.name} {self.dob} {mark}")
if __name__ == "__main__":
    arr = []
    for i in range(5):
        a = input()
        arr.append(a)
    stu = Student(arr[0],arr[1],float(arr[2]),float(arr[3]),float(arr[4]))
    stu.res()
        