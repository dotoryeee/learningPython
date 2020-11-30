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
        print(name, '생성됨')

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

    def 백만볼트(self):
        print('백만볼트 공격~~~')

#숙제. 파이리 꼬부기를 피카추를 참고해서 완성
#프로그램이 시작되자마자 캐릭터 선택
#메뉴돌림(1.밥먹기 2.잠자기 3.놀기 4.운동하기 5.상태확인 6.종료)

class Gobook(PocketMon):
    def __init__(self):
        super().__init__(20, '꼬부기')

    def eat(self):
        super().eat()
        self.hp += 3

    def sleep(self):
        super().sleep()
        self.hp += 5

    def play(self):
        self.hp -= 4
        self.exp += 5
        self.level_check(15)
        return super().play()

    def exc(self):
        self.hp -= 8
        self.exp += 10
        self.level_check(15)
        return super().play()#False: 캐릭터 사망: 게임종료

    def 물대포(self):
        print('물대포 공격~~')

class Lee(PocketMon):
    def __init__(self):
        super().__init__(40, '이상해씨')

    def eat(self):
        super().eat()
        self.hp += 10

    def sleep(self):
        super().sleep()
        self.hp += 15

    def play(self):
        self.hp -= 14
        self.exp += 15
        self.level_check(30)
        return super().play()

    def exc(self):
        self.hp -= 18
        self.exp += 20
        self.level_check(30)
        return super().play()#False: 캐릭터 사망: 게임종료

    def 넝쿨(self):
        print('넝쿨공격~~')

class Menu:
    def __init__(self):
        self.ch = None #변수의 타입이 고정이 아니므로 피카추를 담아도 되고 꼬부기 담아도 된다

    def selectCh(self):#캐릭터를 선택하는 함수. 선택한 객체를 생성해서 멤버변수 ch에 저장
        m = int(input('1.피카추(기본) 2.꼬부기 3.이상해씨'))
        if m == 2:
            self.ch = Gobook()
        elif m == 3:
            self.ch = Lee()
        else:
            self.ch = Picachu()

    def run(self):#메뉴 돌리는 함수.
        flag = True
        while flag:
            m = int(input('1.밥먹기 2.잠자기 3.놀기 4.운동하기 5.상태확인 6.종료 7.특기공격'))
            if m == 1:
                self.ch.eat()
            elif m == 2:
                self.ch.sleep()
            elif m == 3:
                flag = self.ch.play()
            elif m == 4:
                flag = self.ch.exc()
            elif m == 5:
                self.ch.printInfo()
            elif m == 6:
                flag = False
            elif m == 7:
                #피카추=>백만볼트()
                #꼬부기=>물대포()
                #이상해씨=>넝쿨()
                #다형성을 하다보면 타입을 정확하게 모를 때가 있다. 그 객체의 타입을 확인하는 함수 isinstance().
                if isinstance(self.ch, Picachu):
                    self.ch.백만볼트()
                elif isinstance(self.ch, Gobook):
                    self.ch.물대포()
                elif isinstance(self.ch, Lee):
                    self.ch.넝쿨()

        print('게임 종료')

def main():
    m = Menu()
    m.selectCh()
    m.run()

main()