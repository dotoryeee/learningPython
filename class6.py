'''
클래스: 캡슐화(정보)/ 객체:프로그램으로 모델링하는 부분을 구성요소. 사람 or 사물 or 개념(수강) => 타입으로 정의

기능정의
기능명세화
출금:카드꼽는다->비밀->금액->계좌
'''


# 클래스 정의는 사용자 타입을 정의. 메모리 필요한가? 아니다. 메모리는 클래스로 변수를 만들때 할당된다
# 객체: 프로그램 설계시 추출된 샘플. 클래스로 만든 변수
class Test:  # 생성자를 정의하지 않은 클래스. 그래도 기본 생성자. 파라메터도 없고 아무 동작도 안함
    def __init__(self, x, y):  # 멤버 함수. 메서드
        self.x = x  # 멤버변수 x를 정의
        self.y = y  # 멤버변수 y를 정의
        k = 5  # 지역변수. 이 함수 안에서만 사용가능



def printData(self):
    print('x:', self.x)
    print('y:', self.y)
    # print('k:', k)



class Date:
    def __init__(self, yy, mm):
        self.yy = yy  # 연도
        self.mm = mm  # 월



def printDate(self):
    print('카드유효기간: ', self.mm, '/', self.yy)


class Card:
    def __init__(self, com, c_num, pwd, yy, mm):
        self.com = com  # 카드사
        self.c_num = c_num  # 카드번호
        self.pwd = pwd  # 카드 비밀번호
        # 포함관계. 다른 클래스 객체를 멤버변수로 갖음
        self.date = Date(yy, mm)  #



def printCardInfo(self):
    print('카드사:', self.com)
    print('카드번호:', self.c_num)
    print('카드비밀번호:', self.pwd)
    self.date.printDate()  # . 멤버 접근 연산자


def main():  # 전역함수
    cards = []  # 빈 리스트 생성

cards.append(Card('현대카드', '111-2222-111', '1234', '23', '07'))
cards.append(Card('삼성카드', '333-2222-444', '1234', '24', '12'))
cards.append(Card('롯데카드', '888-2222-4561', '5678', '21', '11'))

for i in range(0, len(cards)):  # i: 인덱스. 방번호
    cards[i].date.yy = '00'
    cards[i].pwd = 'qwerqwer'
    cards[i].printCardInfo()


for i in cards:  # i는 요소. cards 리스트의 요소는 Card 객체. i는 Card 객체
    i.yy = '00'
    i.pwd = '가가가'
    i.printCardInfo()

'''
t1 = Test(1,2)#Test클래스의 변수를 만든다. t1을 객체 또는 참조변수. 파이썬의 모든 변수 참조변수
t1.printData()

t2 = Test(3,4)
t2.printData()

t3 = t1 #얕은 복사. t1의 참조값만 복사. 100번지 메모리는 하나. 이름이 t1, t3 2개.
t3.x=40
t3.y=50
t1.printData()
'''
main()
