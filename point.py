class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printPoints(self):
        print(f'{self.x}, {self.y}')

class DAO():
    def __init__(self):
        self.points = []

    def insertPoint(self, point):
        self.points.append(point)

    def selectAll(self):
        return self.points

class Service:
    def __init__(self):
        self.newPoint = DAO()
        self.point = point()

    def addPoint(self):
        self.newPoint.insertPoint(input('x좌표 입력 : '))
        self.newPoint.insertPoint(input('y좌표 입력 : '))


