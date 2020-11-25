import os

def init():
    if not os.path.isdir('memo'):
        os.mkdir('memo')
    os.chdir('memo')
    print('작업 폴더 : ', os.getcwd())

def filecheck(filename):
    li = os.listdir("./")
    tmp = filename + '.txt'
    if tmp in li:
        return True
    else:
        return False

def readMemo():
    print(f'저장된 메모 목록 : {os.listdir("./")}')
    filename = input('읽고싶은  파일명 : ')
    if filecheck(filename) is True:
        print('-' * 50)
        onRead =  open(f'{filename}.txt','r', encoding='utf-8')
        print(onRead.read(), end='')
        print('-'*50)
        onRead.close()
    else:
        print('file not found')

def createMemo(filename):
    print(f'{filename}.txt 메모 작성을 시작합니다')
    memoControl = open(f'./{filename}.txt', 'w+', encoding='utf-8')
    line = 1
    while True:
        contents = input(f'{line}번줄 작성중.. 멈추려면 stop 입력 : ', )
        line+=1
        if contents.upper() == 'STOP':
            break
        memoControl.write(f'{contents}\n')

def newMemo():
    filename = input('저장할 메모 이름 : ' )
    if filecheck(filename) is True:
        ask = input('이미 존재하는 파일입니다. 덮어쓸까요?(Y/N) : ')
        while True:
            if ask.upper() == 'Y':
                createMemo(filename)
                break
            elif ask.upper() == 'N':
                break
    else:
        createMemo(filename)

def menu():
    while True:
        select = input('1.읽기 2.쓰기 3.종료 ')
        if select == '1':
            readMemo()
        if select == '2':
            newMemo()
        if select == '3':
            break

def main():
    init()
    menu()

main()