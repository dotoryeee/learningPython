# 학생의 이름,번호, 국,영,수, 총, 평을 갖는 클래스를 정의. 객체 3개를 생성. 객체 멤버변수에 각 학생의 이름, 번, 국,영,수만 할당
# 총,평 자동계산. 각 학생의 정보를 출력하라
class Student:  # 클래스는 1인분

    def __init__(self, name, num, kor, eng, math):
        # 생성자 파라메터로 받은 값을 멤버변수에 할당
        self.name = name
        self.num = num
        self.kor = kor
        self.eng = eng
        self.math = math
        # 총합 멤버변수 정의 및 계산
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3

    def printStudentInfo(self):  # 한 학생의 정보 출력
        print('name:', self.name)
        print('num:', self.num)
        print('kor:', self.kor)
        print('eng:', self.eng)
        print('math:', self.math)
        print('total:', self.total)
        print('avg:', self.avg)


def main():
    studs = []  # 요소로 Student 객체를 갖는다

    for i in range(0, 3):
        name = input('name:')
        num = input('num:')
        kor = int(input('kor:'))
        eng = int(input('eng:'))
        math = int(input('math:'))
        s = Student(name, num, kor, eng, math)
        studs.append(s)

    for i in studs:
        i.printStudentInfo()

    # 객체 하나가 학생 1명. 객체 생성하려면 생성자 호출
    '''
    s1 = Student('aaa', 1, 34,56,67)
    s2 = Student('bbb', 2, 87,90,76)
    s3 = Student('ccc', 3, 87,65,45)

    s1.printStudentInfo()
    s2.printStudentInfo()
    s3.printStudentInfo()
 '''


main()