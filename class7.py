#VO:value object
#프로그램으로 모델링할때 추출되는 객체의 값을 저장하기 위해 사용하는 클래스
class Date:#날짜 값을 담기 위한 클래스 :VO
    def __init__(self, yy, mm):
        self.yy = yy    #연도
        self.mm = mm    #월

    def printDate(self):
        print('카드유효기간: ', self.mm, '/', self.yy)

class Card:#카드 객체의 값을 담기 위한 클래스 :VO. Card 객체 1개에는 카드 몇 개를 담을 수 있어요? 1개
    def __init__(self, com, c_num, pwd, yy, mm):
        self.com = com  #카드사
        self.c_num = c_num  #카드번호
        self.pwd = pwd  #카드 비밀번호
        #포함관계. 다른 클래스 객체를 멤버변수로 갖음
        self.date = Date(yy, mm)    #
        #self.yy = yy
        #self.mm = mm

    def printCardInfo(self):
        print('카드사:', self.com)
        print('카드번호:', self.c_num)
        print('카드비밀번호:', self.pwd)
        self.date.printDate() #. 멤버 접근 연산자

class Dao:#저장소 작업 담당. 리스트에 카드 객체를 담거나 검색하거나 수정, 삭제 등의 작업
    def __init__(self):
        self.cards = [] #객체를 담을 리스트를 생성

    def insertCard(self, c):#카드객체 1개(c)를 인자로 받아 리스트에 추가
        self.cards.append(c)

    def selectAll(self):    #리스트 전체 반환
        return self.cards

    def select(self, c_num):#검색할 카드 번호를 받아서 저장소(리스트)에서 동일한 번호를 갖는 카드 객체를 찾아서 반환
        for i in self.cards:
            if i.c_num == c_num:
                return i

    def update(self, c_num, pwd):
        c = self.select(c_num)
        if c==None:
            print('없다')
        else:
            c.pwd = pwd

    def delete(self, c_num):
        c = self.select(c_num)
        if c == None:
            print('없다')
        else:
            self.cards.remove(c)

class Service:#사용자가 사용할 기능 구현 클래스
    def __init__(self):
        self.dao = Dao()    #저장소 작업할 dao 객체 생성

    #1.카드추가기능=>카드 정보를 키보드로 입력 => Card객체를 생성. Card객체를 저장소에 저장
    def addCard(self):
        com = input('카드사:')
        c_num = input('카드번호:')
        pwd = input('pwd:')
        yy = input('유효연도')
        mm = input('유효월')
        c = Card(com, c_num, pwd, yy, mm)#값이 여러개인 카드 정보를 간편하게 Card 객체에 담는다
        self.dao.insertCard(c)

    #전체 카드 출력
    def printAll(self):#저장소에 있는 모든 카드를 가져와야 함.
        l1 = self.dao.selectAll()
        for i in l1:#i: 요소(Card 객체)
            i.printCardInfo()#현재 객체(카드)의 정보만 하나 출력함

    def getCard(self):
        c_num = input('카드번호:')
        c = self.dao.select(c_num)#c: 검색된 Card 객체
        if c==None:
            print('없음')
        else:
            c.printCardInfo()

    def editCard(self):
        c_num = input('카드번호:')
        pwd = input('new pwd:')
        self.dao.update(c_num, pwd)

    def delCard(self):
        c_num = input('카드번호:')
        self.dao.delete(c_num)

class Menu:#메뉴 돌리는 클래스. 사용자한테 메뉴를 물어보고 그 메뉴에 해당하는 기능을 실행.
    def __init__(self):
        self.service = Service()

    def run(self):
        while True:
            m = int(input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.종료'))
            if m == 1:
                self.service.addCard()
            elif m == 2:
                self.service.getCard()
            elif m == 3:
                self.service.editCard()
            elif m == 4:
                self.service.delCard()
            elif m == 5:
                self.service.printAll()
            elif m == 6:
                break
def main():
   me = Menu()
   me.run()

main()