import socket, os

class Server:
    ip='localhost'
    port=6666

    def __init__(self, path):
        self.path = path
        self.server_soc = None
        self.client_soc = None

    def mkDir(self):#업로드용 디렉토리 생성(처음 한번만)
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((Server.ip, Server.port))
        self.server_soc.listen()

    def upload(self):
        print('업로드 기능')
        data = self.client_soc.recv(1024)  # 파일명 전송받음
        #전송받은 파일명 저장
        f_name = data.decode()
        print('f_name', f_name)
        #파일명 중복체크 및 중복 파일명 변경
        f_list = os.listdir(self.path)
        for f in f_list:
            if f_name == f:
                s = f_name.split('.')
                f_name = s[0] + '_1.' + s[1]#s[0]:파일명, s[1]:확장자

        #전송받은 파일명으로 파일 쓰기모드 오픈
        f = open(self.path+'/' + f_name, 'w', encoding='utf-8')
        data = self.client_soc.recv(1024)  #파일내용전송받음. 파일크기 최대 1024
        body = data.decode()
        print('body:', body)
        f.write(body)#전송받은 내용을 오픈한 파일에 복사
        f.close()

    def download(self):
        print('다운로드')
        flist = os.listdir(self.path)
        file_names = ''
        for idx, i in enumerate(flist):
            name = str(idx)+'. '+ i + '\n'
            file_names += name

        self.client_soc.sendall(file_names.encode(encoding='utf-8'))

        num = self.client_soc.recv(10).decode()
        num = int(num)
        msg = '/'
        if num<0 or num>=len(flist):
            msg = '잘못된 번호로 다운로드 중단'
            print(msg)
            self.client_soc.sendall(msg.encode(encoding='utf-8'))
            return

        self.client_soc.sendall(msg.encode(encoding='utf-8'))

        print('다운로드 선택 파일 번호:', num)
        self.client_soc.sendall(flist[num].encode())
        f = open(self.path+'/'+flist[num], 'r', encoding='utf-8')
        content = f.read()
        self.client_soc.sendall(content.encode(encoding='utf-8'))
        f.close()

    def run(self):
        self.mkDir()
        self.open()
        self.client_soc, addr = self.server_soc.accept()#대기
        while True:
            m = self.client_soc.recv(10)#클라이언트가 선택한 메뉴 수신
            m = m.decode()
            print('선택메뉴:', m)
            if m=='1':
                self.upload()
            elif m=='2':
                self.download()
            elif m=='3':
                break
        self.server_soc.close()
        self.client_soc.close()

def main():
    s = Server('up')
    s.run()

main()
