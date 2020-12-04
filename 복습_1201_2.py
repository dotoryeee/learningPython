#한 사람의 이름, 나이저장
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):#object 클래스. 객체를 설명하는 메서드. 현재 객체를 설명하는 문자열을 반환하는 메서드
        return 'name:'+self.name+' / age:'+str(self.age)

#저장소 작업. 저장소 작업만 구현. 사용자 입출력은 하지마라
class Dao:
    def __init__(self):
        #5명만 저장
        self.datas = []

    def insert(self, p):
        try:
            if len(self.datas)>=5:
                raise Exception('5명 까지만 저장 가능')
            self.datas.append(p)
        except Exception as e:
            print(e)
            print('추가 취소')

    def select(self, name):
        for i in self.datas:    #i는 요소. Person객체
            if i.name == name:
                return i

    def update(self, p):#파라메터로 Person 객체 받음. p에는 수정할 사람의 이름과 새 나이
        person = self.select(p.name)
        if person==None:
            print('없는 사람')
        else:
            person.age = p.age

    def delete(self, name):
        person = self.select(name)
        if person == None:
            print('없는 사람')
        else:
            self.datas.remove(person)

    def selectAll(self):
        return self.datas

#사용자 기능 구현. 사용자 입출력(UI).1명의 정보를 저장.

class Service:
    def __init__(self):
        self.dao = Dao()

    # 추가=>1명 이름.나이를 입력 받는다=>입력받은 데이터로 Person 객체생성=> 저장소에 저장
    def addPerson(self):
        name = input('name:')
        try:
            age = int(input('age:'))
            p = Person(name, age)
            self.dao.insert(p)
        except Exception as e:
            print(e)
            print('잘못된 나이로 인해서 추가 중담됨')


    #검색:1.이름입력 2.저장소에서 찾는다 3.찾은 값을 출력
    def getPerson(self):
        name = input('name:')
        p = self.dao.select(name)
        if p==None:
            print('없는 사람')
        else:
            print(p)

    def printAll(self):
        l1 = self.dao.selectAll()
        for i in l1:
            print(i)

    #edit:1.수정할 사람 이름,나이 입력 2.입력받은 값으로 Person 객체 생성 3.저장소에서 수정작업
    def editPerson(self):
        name = input('수정할 사람 name:')
        age = int(input('new age:'))
        p = Person(name, age)
        self.dao.update(p)

    def delPerson(self):
        name = input('삭제할 사람 name:')
        self.dao.delete(name)

def main():
    s = Service()
    s.addPerson()
    s.addPerson()
    s.addPerson()
    s.addPerson()
    s.addPerson()
    s.addPerson()
    s.printAll()
main()


