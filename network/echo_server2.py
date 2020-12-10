import socket
import threading

def sendMsg(soc):#키보드 입력받아 클라이언트로 메시지 전송하는 쓰레드에서 사용할 함수
    while True:
        msg = input('msg:')
        soc.sendall(msg.encode())
        if msg == '/stop':
            break
    print('서버 메시지 입력 쓰레드 종료')

def recvMsg(soc):#클라이언트 메시지 받아오는 쓰레드에서 사용할 함수
    while True:
        data = soc.recv(1024)
        msg = data.decode()
        print('client msg:', msg)
        if msg == '/stop':
            break
    print('서버 메시지 리시브 쓰레드 종료')


class UniChatServer:
    host = 'localhost'  #server ip. localhost. or  127.0.0.1
    port = 8888         #server port

    def __init__(self):
        self.server_soc = None
        self.client_soc = None

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((UniChatServer.host, UniChatServer.port))
        self.server_soc.listen()

    def run(self):
        self.open()
        print('서버시작')
        self.client_soc, addr = self.server_soc.accept()
        print(addr, '접속완료')
        t = threading.Thread(target=sendMsg, args=(self.client_soc,))
        t.start()
        t2 = threading.Thread(target=recvMsg, args=(self.client_soc,))
        t2.start()

def main():
    us = UniChatServer()
    us.run()

main()




