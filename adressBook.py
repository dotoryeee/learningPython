datas={}    #여러 사람의 정보를 저장. {'name':'aaa', 'tel':'111', 'addr':'asdf'}
cnt=1       #저장된 사람 수 카운팅. datas에 새 항목 추가할 때 키로 사용.
titles = ['name', 'tel', 'addr']
#딕셔너리는 방번호 없음.
def addMember():
    global cnt
    mem = {}    #빈 딕셔너리 생성. 추사하려는 사람의 이름, 전화, 주소를 담기 위해
    for i in titles:
        mem[i]=input(i+': ')    #mem['name']=input('name: ')
    datas[cnt]=mem  #새 항목 datas에 추가. dict[키]=값 . datas[2]={'name':'aaa', 'tel':'111','addr':'asdf'}
    cnt+=1  #한 사람 추가 했으므로 cnt를 1증가

def printMember(d): #1명 출력. 1명의 딕셔너리를 파라메터로 받음.
    for i in d: #파라메터로 받은 딕셔너리의 모든 요소, 'name', 'tel', 'addr'을 i에 하나씩 할당
        print(i, ': ', d[i])    #d[i]: i키의 값. 만약 i가 'name'이면 d['name']은 'aaa'를 의미
    print('=============')

def printAll():#datas 전체 출력
    for i in datas:#datas의 모든 요소. i: 1, 2, 3.... / 1, 2, 3은 방번호가 아니라 키값
        printMember(datas[i])  #printMember()로 한명씩 정보 출력

def printKeys():
    print('등록된 번호')
        print(i, end=', ')
    print()
def search():#검색결과가 있으면 튜플(key, val)반환. 없으면 None을 반환
    num = int(input('번호를 입력하시오'))
    try:
        mem = datas[num]#mem:{'name':'aaa', 'tel':'111', 'addr':'asdf'}
        printMember(mem)
        return num, mem #num:키값, mem:키의 값(한명의 정보가 있는 딕셔너리). 튜플 형태로 반환
    except KeyError:
        print('없는 번호')

def editMember():
    printKeys()
    t = search()#검색결과가 있으면 튜플=>t[0]:키값(번호), t[1]:{'name':'aaa', 'tel':'111', 'addr':'asdf'}
    if t!=None:
        t[1]['tel'] = input('new tel:')
        t[1]['addr'] = input('new addr:')

def delMember():
    printKeys()
    t = search()
    if t != None:
        del datas[t[0]]

def menu():
    while True:
        m = int(input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.종료'))
        if m==1:
            addMember()
        elif m==2:
            search()
        elif m==3:
            editMember()
        elif m==4:
            delMember()
        elif m==5:
            printAll()
        elif m==6:
            break

def main():
    menu()

