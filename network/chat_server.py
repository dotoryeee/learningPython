import socket
import threading

def receiveMsg(soc):
    while True:
        data = soc.recv(1024)
        newMsg = data.decode()
        print(f'새 매세지 : {newMsg}')
        if newMsg == '/stop':
            soc.sendall(('/stop').encode())
            break
    print('수신 스레드 종료')

class ChatServer:
    server_address = 'localhost'
    server_port = 8888

    def __init__(self):
        self.server_soc = None
        self.client_soc = None

    def serverOpen(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((ChatServer.server_address, ChatServer.server_port))
        self.server_soc.listen()

    def run(self):
        self.serverOpen()
        print('server startup')
        self.client_soc, address = self.server_soc.accept()
        print(f'{address} 연결됨')
        t = threading.Thread(target=receiveMsg, args=(self.client_soc,))
        t.start()

def main():
    server = ChatServer()
    server.run()

main()