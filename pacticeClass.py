class student:
    sum, avg = 0, 0
    def __init__(self, name, ID, score1, score2, score3):
        self.name = name
        self.ID = ID
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.calcScore()

    def calcScore(self):
        global sum
        global avg
        sum = self.score1 + self.score2 + self.score3
        avg = sum // 3

    def printCalc(self):
        print(f'{self.name}의 총점 : {sum} / 평균 : {avg}')

def main():
    stu1 = student('a','1',12, 23, 45)
    stu1.printCalc()

    stu2 = student('b','2', 34, 45, 43)
    stu2.printCalc()

    stu3 = student('c','3', 45, 56, 12)
    stu3.printCalc()

main()
