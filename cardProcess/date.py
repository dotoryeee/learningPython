class Date:#날짜 값을 담기 위한 클래스 :VO
    def __init__(self, yy, mm):
        self.yy = yy    #연도
        self.mm = mm    #월

    def printDate(self):
        print('카드유효기간: ', self.mm, '/', self.yy)