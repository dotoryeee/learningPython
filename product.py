class product():
    def __init__(self, ID, name, price, quantity):
        self.ID = ID
        self.name = name
        self.price = price
        self.quantity = quantity

    def productInfo(self):
        print(f'제품명 : {self.name}, 제품코드 : {self.ID}, 가격 : {self.price}, 수량 : {self.quantity}')

def main():
    li = [0] * 3
    '''
    li[0] = product(1, '새우강', 1500, 20)
    li[1] = product(2, '감쟈강', 1200, 10)
    li[2] = product(3, '요단강', 1000, 5)
    '''
    for i in range(0, len(li)):
        ID = input(f'{i+1}번 ID : ')
        name = input(f'{i+1}번 이름 : ')
        price = input(f'{i+1}번 가격 : ')
        quantity = input(f'{i+1}번 수량 : ')
        li[i] = product(ID, name, price, quantity)

    for i in li:
        product.productInfo(i)

main()