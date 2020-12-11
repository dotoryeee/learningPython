import socket
import os

class LocalController():
    def __init__(self, name, data):
        if not os.path.isdir('downloaded'):
            os.mkdir('downloaded')
        os.chdir('downloaded')
        self.data = data
        self.fileName = name
        self.fileNames = os.listdir('./')

    def dupCheck(self):
        for name in self.fileNames:
            dividedName = name.split('.')
            if dividedName[0] == self.fileName:
                return True#중복시 True 반환

    def writeContent(self):
        openContent = open(f'./{self.fileName}.txt', "w+", encoding="utf-8")
        openContent.write(self.data)
        openContent.close()

    def runController(self):
        check = self.dupCheck()
        if check is not True:
            print('중복된 파일명')
            return
        else:
            self.writeContent()

class Server():
    def __init__(self):
        self.ip = 'localhost'
        self.port = 8888

    def open(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen()

    def runServer(self):
        self.open()
        print('서버 시작')
        while True:
            client_socket, address = self.server_socket.accept()
            print(f'{address}에 연결됨')
            ask = '파일명 : '
            client_socket.sendall(ask.encode())
            title = client_socket.recv(1024)
            ask = '내용 : '
            client_socket.sendall(ask.encode())
            content = client_socket.recv(1024)
            local_controller = LocalController(title, content)
            local_controller.runController()

def main():
    server = Server()
    server.runServer()

main()

'''
    def upload(soc):
        data = soc.recv(1024)
        fileName = data.decode()
        print(f'f_name : {fileName}')
        f_list = dir_list()
        for file in f_list:
            if fileName == file:
                s = fileName.split('.')
                fileName = s[0] + '_1' + s[1]
        file = open('refs/' + fileName, 'w')
        data = soc.recv(1024)
        body = data.decode()
        print(f'body : {body}')
        file.write(body)
        file.close()
'''