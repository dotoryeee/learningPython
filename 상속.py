class person:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        print('부모 생성')

    def printInfo(self):
        print(f'ID : {self.ID}')
        print(f'name : {self.name}')

class student(person):
    def __init__(self, ID, name, sub):
        super().__init__(ID, name)
        self.sub = sub

    def printSub(self):
        print(f'sub : {self.sub}')

class staff(person):
    def __init__(self, ID, name, job):
        super().__init__(ID, name)
        self.job = job

    def printJob(self):
        print(f'job : {self.job}')

def main():
    stu1 = student(1,'zzz','ggg')
    stu1.printInfo()
    stu1.printSub()

    stf1 = staff(1, 'dasd', 'sad')
    stf1.printInfo()
    stf1.printJob()

main()