import Dao as Dao
import product as Prod

class Service:
    def __init__(self):
        self.dao = Dao.Dao()

    def addProduct(self):
        print('제품추가')
        p = 0
        while p!=None:
            num = int(input('num:'))
            p = self.dao.selectByNum(num)   #p가 None이면 중복되지 않은 번호이므로 루프를 빠져나감
        name = input('name:')
        price = int(input('price:'))
        q = int(input('qunatity:'))

        self.dao.insert(Prod.Product(num, name, price, q))

    def getProductByNum(self):
        print('제품 번호로 검색')
        num = int(input('num:'))
        p = self.dao.selectByNum(num)
        if p==None:
            print('없는 제품')
        else:
            p.printProductInfo()

    def getProductByName(self):
        print('제품 이름으로 검색')
        name = input('name:')
        l1 = self.dao.selectByName(name)
        if len(l1) == 0:
            print(name, '이름의 제품이 없다')
            return

        for i in l1:
            i.printProductInfo()


    def getAll(self):
        print('제품 전체 검색')
        l1 = self.dao.selectAll()
        for i in l1:
            i.printProductInfo()

    def editProduct(self):
        print('제품 가격 수정')

        num = int(input('num:'))
        price = int(input('price:'))

        self.dao.update(num, price)

    def delProduct(self):
        print('제품 삭제')
        num = int(input('num:'))
        self.dao.delete(num)
