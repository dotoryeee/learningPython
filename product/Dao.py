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