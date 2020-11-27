import date

class Card:#카드 객체의 값을 담기 위한 클래스 :VO. Card 객체 1개에는 카드 몇 개를 담을 수 있어요? 1개
    def __init__(self, com, c_num, pwd, yy, mm):
        self.com = com  #카드사
        self.c_num = c_num  #카드번호
        self.pwd = pwd  #카드 비밀번호
        #포함관계. 다른 클래스 객체를 멤버변수로 갖음
        self.date = date.Date(yy, mm)    #
        #self.yy = yy
        #self.mm = mm

    def printCardInfo(self):
        print('카드사:', self.com)
        print('카드번호:', self.c_num)
        print('카드비밀번호:', self.pwd)
        self.date.printDate() #. 멤버 접근 연산자