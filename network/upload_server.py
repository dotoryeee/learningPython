import socket, os

class Server:
    ip='localhost'
    port=6666

    def __init__(self, path):
        self.path = path
        self.server_soc = None
        self.client_soc = None

    def mkDir(self):
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
        f_name = data.decode()
        print('f_name', f_name)
        f_list = os.listdir(self.path)
        for f in f_list:
            if f_name == f:
                s = f_name.split('.')
                f_name = s[0] + '_1.' + s[1]

        f = open(self.path+'/' + f_name, 'w', encoding='utf-8')
        data = self.client_soc.recv(1024)  # 파일크기 최대 1024
        body = data.decode()
        print('body:', body)
        f.write(body)
        f.close()

    def download(self):
        print('다운로드')

    def run(self):
        self.mkDir()
        self.open()
        self.client_soc, addr = self.server_soc.accept()
        while True:
            m = self.client_soc.recv(10)
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
