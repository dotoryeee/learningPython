class clothes:
    def __init__(self):
        self.fabric = ''

    def printFabric(self):
        print(f'원단 : {self.fabric}')

class onePiece(clothes):
    def __init__(self):
        super().__init__()
        self.fabric = '쉬폰'
        self.length = 'long'

    def printLength(self):
        print(f'길이 : {self.length}')

class shirt(clothes):
    def __init__(self):
        super().__init__()
        self.fabric = 'silk'
        self.pattern = 'check'

    def printPattern(self):
        print(f'패턴 : {self.pattern}')

def main():
    clothes1 = onePiece()
    clothes2 = shirt()

    clothes1.printFabric()
    clothes1.printLength()
    print()
    clothes1.printFabric()
    clothes2.printPattern()

main()