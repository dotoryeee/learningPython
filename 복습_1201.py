'''
#함수정의
def 함수명(파라메터 리스트):
    실행문

#함수호출
함수명(인자)
'''
#리스트를 인자로 받아 리스트 요소를 출력하는 함수
def printList(l1):#l1은 리스트를 받을꺼다
    for i in l1: #in 뒤에 (리스트나 문자열 등 목록)이름 왔다. i:요소
        print(i)

def sumList(l1):
    s=0
    m=l1[0]
    for i in range(0, len(l1)):#in 뒤에 ragne(). i는 방번호
        s+=l1[i]
        if m < l1[i]:
            m = l1[i]
    return s, m

#클래스. 멤버변수를 메서드 안에서 어디서나 정의해도 상관없음. 하지만
class MyList: #멤버변수로 리스트를 갖는다. 클래스는 거푸집. 알맹이 없다. 객체를 만들어야 멤버변수와 메서드 사용가능.
    cnt=0   #static변수(클래스변수): 객체를 만들지 않아도 사용 가능. MyList.cnt=10. 모든 객체가 공용으로 사용
    def __init__(self):
        self.l1 = []

    def addList(self, x):
        self.l1.append(x)

    def printList(self):
        for i in self.l1:
            print(i)

    @staticmethod #static 메서드임을 알림. static 메서드는 self 파라메터가 없다. MyList.staticTest(). 멤버변수사용불가
    def staticTest():
        print('test')

def main():
    l = [1,2,3,4,5]
    printList(l)#점프
    s = sumList(l)#s:튜플
    print('l 요소의 총합:', s[0])
    print('l 요소의 최대값:', s[1])

    m1 = MyList()
    for i in range(1, 6):
        m1.addList(i)
    m1.printList()

    m2 = MyList()
    for i in range(6, 9):
        m2.addList(i)
    m2.printList()

    print(m1)
main()