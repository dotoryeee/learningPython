#상속
#1. 코드 재사용성을 높이기 위해
#2. 다형성 구현

#부모클래스, 상위클래스, base class: 상속을 해주는 클래스
class Person:
    def __init__(self, num, name):
        self.num = num
        self.name = name
        print('부모 생성자')

    def printInfo(self):
        print('num:', self.num)
        print('name:', self.name)

#자식클래스, 하위클래스, 파생클래스: 상속을 받는 클래스
class Student(Person):#학생
    def __init__(self, num, name, sub):
        super().__init__(num, name)
        self.sub = sub
        print('자식(학생) 생성자')

    def printInfo(self):
        print('num:', self.num)
        print('name:', self.name)
        print('수강과목:', self.sub)

class Staff(Person):#교직원
    def __init__(self, num, name, job):
        super().__init__(num, name)
        self.job = job
        print('자식(교직원) 생성자')

    def printInfo(self):
        super().printInfo()
        print('직무:', self.job)

def main():
    array = [Person(1, '부모'), Student(2, '학생', '컴퓨터'), Staff(3, '교직원', 'hr')]

   for i in array:
       i.printInfo()

main()