#피카추 파이리 꼬부기
'''
hp(생명)
exp(경험치)0.
level-1
name-

밥먹기()-hp증가.
잠자기()-hp증가
운동하기()-hp감소=>hp가 0이냐?죽었음 / exp증가=>레벨업 조건
놀기()-hp감소=>hp가 0이냐?죽었음 / exp증가=>레벨업 조건
상태정보()-hp(생명) exp(경험치)0. level 출력력
'''
class PocketMon:
    def __init__(self, hp, name):
        self.hp = hp
        self.exp = 0
        self.lv = 1
        self.name = name

    def eat(self):
        print(self.name, '밥먹음')

    def sleep(self):
        print(self.name, '잠잠')

    def play(self):#hp를 확인. 살았으면 True반환. 죽었으면 메시지 출력하고 False반환
        print(self.name, '놀기')
        flag = self.hp > 0
        if not flag:
            print(self.name, '캐릭터가 죽었습니다')
        return flag

    def exc(self):
        print(self.name, '운동함')
        flag = self.hp > 0
        if not flag:
            print(self.name, '캐릭터가 죽었습니다')
        return flag

    def printInfo(self):
        print(self.name, '상태정보')
        print('hp:', self.hp)
        print('exp:', self.exp)
        print('level:', self.lv)

    def level_check(self, max):
        print(self.name, '레벨체크')
        if self.exp >= max:
            self.lv += 1
            self.exp -= max
            print(self.name, '레벨업 되었습니다.')

class Picachu(PocketMon):
    def __init__(self):
        super().__init__(30, '피카추')

    def eat(self):
        super().eat()
        self.hp += 5

    def sleep(self):
        super().sleep()
        self.hp += 10

    def play(self):
        self.hp -= 8
        self.exp += 6
        self.level_check(20)
        return super().play()

    def exc(self):
        self.hp -= 15
        self.exp += 10
        self.level_check(20)
        return super().play()#False: 캐릭터 사망: 게임종료

#숙제. 파이리 꼬부기를 피카추를 참고해서 완성
#프로그램이 시작되자마자 캐릭터 선택
#메뉴돌림(1.밥먹기 2.잠자기 3.놀기 4.운동하기 5.상태확인 6.종료)
