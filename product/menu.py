import service as serv

class Menu:
    def __init__(self):
        self.service = serv.Service()

    def run(self):
        while True:
            m = int(input('1.제품추가 2.제품번호로검색 3.제품이름검색 4.수정 5.삭제 6.전체출력 7. 종료'))
            if m == 1:
                self.service.addProduct()
            elif m == 2:
                self.service.getProductByNum()
            elif m == 3:
                self.service.getProductByName()
            elif m == 4:
                self.service.editProduct()
            elif m == 5:
                self.service.delProduct()
            elif m == 6:
                self.service.getAll()
            elif m == 7:
                break