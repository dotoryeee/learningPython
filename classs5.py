class product:
    def __init__(self, ID, name, price, quantity):
        self.ID = ID  #제품번호
        self.name = name    #제품명
        self.price = price  #가격
        self.quantity = quantity    #수량

    def printProductInfo(self):
        print('제품번호:', self.ID)
        print('제 품 명:', self.name)
        print('가    격:', self.price)
        print('수    량:', self.quantity)

class DAO:
    def __init__(self):
        self.datas = []

    def add(self, data):
        self.datas.append(data)

    def select(self, ID):
        for i in self.datas:
            if i.ID == ID:
                return i

    def selectWithName(self, name):
        for i in self.datas:
            if name == i.name:
                return i

    def update(self, data):
        pass

    def delete(self, ID):



#제품추가, 제품검색(번호/이름), 수정(번호로 검색해서 수정), 삭제(번호로 검색해서 삭제), 전체출력

class service:
        def __init__(self):
            self.dao = DAO()

        def packingData(self):
            ID = input('제품번호 : ')
            name = input('이\t 름 : ')
            price = int(input('가\t 격 : '))
            quantity = int(input('수\t 량 : '))
            print()
            return product(ID, name, price, quantity)

        def addItem(self):
            print('-'*20 ,'제품 정보 입력','-'*20)
            add = self.packingData()
            self.dao.add(add)

        def selectItem(self):
            way = input('찾을 방법 - 1.제품번호 2.제품명 : ')
            if way == '1':
                search = self.dao.select(input('찾을 제품번호 : '))
                if search == None:
                    print('not found')
                else:
                    search.printProductInfo()
            elif way == '2':
                search = self.dao.selectWithName(input('찾을 제품명 : '))
                if search == None:
                    print('not found')
                else:
                    search.printProductInfo()

        def printAll(self):
            print('-' * 50)
            for i in self.dao.datas:
                i.printProductInfo()
                print('-'*50)

        def updateItem(self):
            pass

        def deleteItem(self):
            pass


class menu():
    def __init__(self):
        self.service = service()

    def run(self):
        while True:
            menu = input('1.제품추가 2.제품검색 3.수정 4.삭제 5.전체보기 6.종료 : ')
            if menu == '1':
                self.service.addItem()
            elif menu == '2':
                self.service.selectItem()
            elif menu == '3':
                self.service.updateItem()
            elif menu == '4':
                self.service.deleteItem()
            elif menu == '5':
                self.service.printAll()
            elif menu == '6':
                break

def main():
    m = menu()
    m.run()

main()