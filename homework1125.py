#한명의 주소 담는 그릇
class Member:
    def __init__(self, name, tel, addr):#한명의 이름, 전화, 주소 담을 수있는 멤버변수 정의하고 생성자로 받아온 값 멤버에 할당
        self.name = name
        self.tel = tel
        self.addr = addr

    def printMember(self):#멤버변수 출력
        print('name:', self.name)
        print('tel:', self.tel)
        print('address:', self.addr)

class Dao:#저장소(리스트)에 추가,검색, 수정, 삭제,출력 기능을 구현한 클래스. 저장소와 관련된 기능제공 클래스
    def __init__(self):
        self.datas = []#생성자에서 Member 객체들을 저장할 리스트 생성

    def addMember(self):#주소록에 한명 추가하는 함수
        #한명 정보를 입력받음
        name = input('name:')
        tel = input('tel:')
        addr = input('address:')
        #입력받은 name, tel, addr로 Member 객체 생성
        x = Member(name, tel, addr)
        self.datas.append(x)

    def printAll(self):
        for i in self.datas:
            i.printMember()

    def getMember(self):#검색
        pass

    def editMember(self):#수정.
        pass

    def delMember(self):#삭제
        pass

class Menu:
    def __init__(self):
        self.dao = Dao()

    def run(self):
        while True:
            m = int(input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.종료'))
            if m == 1:
                self.dao.addMember()
            elif m == 2:
                self.dao.getMember()
            elif m == 3:
                self.dao.editMember()
            elif m == 4:
                self.dao.delMember()
            elif m == 5:
                self.dao.printAll()
            elif m == 6:
                break

def main():
    m = Menu()
    m.run()

main()