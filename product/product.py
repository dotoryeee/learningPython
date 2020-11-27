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