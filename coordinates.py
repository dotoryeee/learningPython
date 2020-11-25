class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printPoint(self):
        print(f'({self.x}, {self.y})', end='\t')



def main():
    p = [0]*3
    p[0] = point(3, 4)
    p[1] = point(7,8)
    p[2] = point(12,56)

    for i in p:
        point.printPoint(i)

main()