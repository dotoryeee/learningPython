import socket, os

class Client:
    ip = 'localhost'
    port = 6666

    def __init__(self):
        self.client_soc = None

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

    def run(self):
        self.conn()
        menu_str = '1.업로드 2.다운로드 3.종료'
        while True:
            m = input(menu_str)
            self.client_soc.sendall(m.encode())
            if m=='1':
                self.upload()
            elif m=='2':
                pass
            elif m=='3':
                break

def main():
    c = Client()
    c.run()

main()