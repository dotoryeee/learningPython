class Dao:#저장소 작업 담당. 리스트에 카드 객체를 담거나 검색하거나 수정, 삭제 등의 작업
    def __init__(self):
        self.cards = [] #객체를 담을 리스트를 생성

    def insertCard(self, c):#카드객체 1개(c)를 인자로 받아 리스트에 추가
        self.cards.append(c)

    def selectAll(self):    #리스트 전체 반환
        return self.cards

    def select(self, c_num):#검색할 카드 번호를 받아서 저장소(리스트)에서 동일한 번호를 갖는 카드 객체를 찾아서 반환
        for i in self.cards:
            if i.c_num == c_num:
                return i

    def update(self, c_num, pwd):
        c = self.select(c_num)
        if c==None:
            print('없다')
        else:
            c.pwd = pwd

    def delete(self, c_num):
        c = self.select(c_num)
        if c == None:
            print('없다')
        else:
            self.cards.remove(c)