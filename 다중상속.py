#파이썬은 다중상속 가능.
#다중상속은 한번에 여러 클래스를 상속받는것
#한번에 여러 클래스를 상속받기 때문에 다양한 기능을 쉽게 첨가 할 수 있다.
class A:#멤버변수 a / Amethod()
    def __init__(self):
        self.a = 'A 클래스'

    def Amethod(self):
        print('A 메서드')


class B:#멤버변수 b / Bmethod()
    def __init__(self):
        self.b = 'B 클래스'

    def Bmethod(self):
        print('B 메서드')

class C(A, B):#다중상속. 한번에 A, B를 상속받음
    def __init__(self):
        A.__init__(self)#부모 A의 생성자
        B.__init__(self)#부모 B의 생성자


    def Cmethod(self):
        print(self.a)
        print(self.b)

def main():
    c1 = C()
    c1.Amethod()
    c1.Bmethod()
    c1.Cmethod()

main()