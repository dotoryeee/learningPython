import socket, os

class Client:
    ip = 'localhost'
    port = 6666

    def __init__(self, path):
        self.client_soc = None
        self.path = path

    def conn(self):
        self.client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc.connect((Client.ip, Client.port))

    def upload(self):
        flist = os.listdir('./')
        for idx, i in enumerate(flist):
            print(idx,'. ',i)

        while True:
            num = int(input('업로드 할 파일의 번호 입력'))
            if 0<=num<len(flist):
                break

        self.client_soc.sendall(flist[num].encode())
        f = open(flist[num], 'r', encoding='utf-8')
        content = f.read()
        self.client_soc.sendall(content.encode(encoding='utf-8'))
        f.close()

    def download(self):
        #파일목록 받음. 파일번호전송. 파일명받음. 파일내용받음
        files = self.client_soc.recv(1024).decode()
        print(files)
        num = input('다운로드 할 파일의 번호 입력')
        self.client_soc.sendall(num.encode())

        err_msg = self.client_soc.recv(1024).decode()
        if err_msg!='/':
            print(err_msg)
            return

        f_name = self.client_soc.recv(1024).decode()

        f = open(self.path + '/' + f_name, 'w', encoding='utf-8')
        data = self.client_soc.recv(1024)  # 파일내용전송받음. 파일크기 최대 1024
        body = data.decode()
        print('body:', body)
        f.write(body)  # 전송받은 내용을 오픈한 파일에 복사
        f.close()

    def run(self):
        self.conn()
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

        menu_str = '1.업로드 2.다운로드 3.종료'
        while True:
            m = input(menu_str)
            self.client_soc.sendall(m.encode())
            if m=='1':
                self.upload()
            elif m=='2':
                self.download()
            elif m=='3':
                break

def main():
    c = Client('down')
    c.run()

main()