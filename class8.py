#mvc 패턴:m(model-vo,dao,service), v(view-뷰단), c(controller:프로그램의 흐름 제어: menu)
#검색: 검색할 좌표(x,y)를 입력받아 동일한 좌표 출력. 없으면 없다출력
#수정: 수정할 좌표(x,y)를 입력받아 info를 수정
#삭제: 삭제할 좌표(x,y)를 입력받아 있으면 dao의 리스트에서 좌표 삭제

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.info = ''  #좌표 설명

    def printPoint(self):
        print('[',self.x,',',self.y,']: ', self.info)

#기능: 1. 좌표추가 2. 좌표전체 출력
class Dao:
    # 생성자:point여러 개 당을 수 있는 리스트 생성
    def __init__(self):
        self.points = []

    #리스트에 point 추가 메서드
    def insertPoint(self, p):   #p:Point 객체
        self.points.append(p)   #리스트에 좌표 하나 추가

    #리스트 반환(전체검색)하는 메서드
    def selectAll(self):
        return self.points

    #검색 메서드
    def select(self, x, y):
        for p in self.points:
            if x==p.x and y==p.y:
                return p

    #수정 메서드
    def update(self, p):#p는 Point 객체로 x,y,info 값을 담아 온다
        p1 = self.select(p.x, p.y)
        if p1 == None:
            print('없는 좌표')
        else:
            p1.info = p.info

    def update2(self, x, y, info): #x,y는 수정하고 싶은 좌표. info는 새 info 값
        p = self.select(x, y)
        if p == None:
            print('없는 좌표')
        else:
            p.info = info

    #삭제 메서드
    def delete(self, x, y):#x,y: 삭제할 좌표
        p = self.select(x, y)
        if p == None:
            print('없는 좌표')
        else:
            self.points.remove(p)

#기능 구현 클래스
class Service:
    #생성자: dao 객체 생성
    def __init__(self):
        self.dao = Dao()

    #x,y를 입력받아 Point(좌표) 객체를 생성해서 반환
    def makePoint(self):
        x = int(input('x좌표:'))
        y = int(input('y좌표:'))
        '''
        p = Point(x, y)
        return p
        '''
        return Point(x, y)#info:''

    #addPoint():좌표추가기능
    def addPoint(self):
        print('추가할 좌표입력')
        p = self.makePoint()
        self.dao.insertPoint(p)

    #printPoints():모든 좌표 출력
    def printPoints(self):
        points = self.dao.selectAll()# 좌표 전체 검색
        for p in points:
            p.printPoint()



    #좌표 검색
    def getPoint(self):
        print('검색할 좌표입력')
        p = self.makePoint()
        p1 = self.dao.select(p.x, p.y)
        if p1==None:
            print('없는 좌표')
        else:
            p1.printPoint()

    def getPoint2(self):
        print('검색할 좌표입력')
        x = int(input('x좌표:'))
        y = int(input('y좌표:'))
        p = self.dao.select(x, y)
        if p == None:
            print('없는 좌표')
        else:
            p.printPoint()

    #좌표 수정
    def editPoint(self):
        print('수정할 좌표입력')
        p = self.makePoint()
        p.info = input('new info:')
        self.dao.update(p)

    # 좌표 삭제
    def delPoint(self):
        print('삭제할 좌표입력')
        p = self.makePoint()
        self.dao.delete(p.x, p.y)

#메뉴에 따라 기능 실행
class Menu:
    def __init__(self):
        self.service = Service()

    def run(self):
        while True:
            m = int(input('1.좌표추가 2.좌표검색 3.수정 4.삭제 5.전체출력 6.종료'))
            if m == 1:
                self.service.addPoint()
            elif m == 2:
                self.service.getPoint2()
            elif m == 3:
                self.service.editPoint()
            elif m == 4:
                self.service.delPoint()
            elif m == 5:
                self.service.printPoints()
            elif m == 6:
                break
def main():
    m = Menu()
    m.run()

main()