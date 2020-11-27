import cardProcess.dao as DAO
import cardProcess.card as ca

class Service:#사용자가 사용할 기능 구현 클래스
    def __init__(self):
        self.dao = DAO.Dao()    #저장소 작업할 dao 객체 생성

    #1.카드추가기능=>카드 정보를 키보드로 입력 => Card객체를 생성. Card객체를 저장소에 저장
    def addCard(self):
        com = input('카드사:')
        c_num = input('카드번호:')
        pwd = input('pwd:')
        yy = input('유효연도')
        mm = input('유효월')
        c = ca.Card(com, c_num, pwd, yy, mm)#값이 여러개인 카드 정보를 간편하게 Card 객체에 담는다
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