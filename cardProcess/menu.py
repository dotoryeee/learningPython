import cardProcess.service as serv

class Menu:#메뉴 돌리는 클래스. 사용자한테 메뉴를 물어보고 그 메뉴에 해당하는 기능을 실행.
    def __init__(self):
        self.service = serv.Service()

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