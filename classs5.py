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

def main():
    p = [0]*3   #크기가 3인 리스트 정의
    for i in range(0, len(p)):#리스트 p의 길이만큼 반복
        #Product 객체 생성하여 p리스트에 담는다
        name = input('제품명:')
        price = int(input('가격:'))
        a = int(input('수량:'))
        p[i] = Product(i, name, price, a)#Product 객체 생성

    for i in p:
        i.printProductInfo()

main()

#dao, service, menu, main
#제품추가, 제품검색(번호/이름), 수정(번호로 검색해서 수정), 삭제(번호로 검색해서 삭제), 전체출력