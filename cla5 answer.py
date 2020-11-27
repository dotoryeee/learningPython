#vo
class Product:
    def __init__(self, num, name, price, quantity):
        self.num = num  #제품번호
        self.name = name    #제품명
        self.price = price  #가격
        self.quantity = quantity    #수량

    def printProductInfo(self):
        print('제품번호:', self.num)
        print('제품명:', self.name)
        print('가격:', self.price)
        print('수량:', self.quantity)

#dao
class Dao:
    def __init__(self):
        self.prods = []

    def insert(self, p):
        self.prods.append(p)

    def selectByNum(self, num):#검색된 결과가 없으면 None 반환
        for i in self.prods:
            if i.num == num:
                return i

    def selectByName(self, name):#검색결과가 있건 없건, 2,5개건 무조건 리스트 반환. 리스트길이가 0이면 검색안됨.
        res = []
        for i in self.prods:
            if i.name == name:
                res.append(i)
        return res

    def update(self, num, price):
        p = self.selectByNum(num)
        if p==None:
            print('없는 제품')
        else:
            p.price = price

    def delete(self, num):
        p = self.selectByNum(num)
        if p == None:
            print('없는 제품')
        else:
            self.prods.remove(p)

    def selectAll(self):
        return self.prods

class Service:
    def __init__(self):
        self.dao = Dao()

    def addProduct(self):
        print('제품추가')
        p = 0
        while p!=None:
            num = int(input('num:'))
            p = self.dao.selectByNum(num)   #p가 None이면 중복되지 않은 번호이므로 루프를 빠져나감
        name = input('name:')
        price = int(input('price:'))
        q = int(input('qunatity:'))

        self.dao.insert(Product(num, name, price, q))

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

class Menu:
    def __init__(self):
        self.service = Service()

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

def main():
   me = Menu()
   me.run()

main()