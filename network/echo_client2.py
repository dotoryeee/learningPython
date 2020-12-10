import socket
import threading

def sendMsg(soc):#키보드 입력받아 클라이언트로 메시지 전송하는 쓰레드에서 사용할 함수
    while True:
        msg = input('msg:')
        soc.sendall(msg.encode())
        if msg == '/stop':
            break
    print('클라이언트 메시지 입력 쓰레드 종료')

def recvMsg(soc):#클라이언트 메시지 받아오는 쓰레드에서 사용할 함수
    while True:
        data = soc.recv(1024)
        msg = data.decode()
        print('server msg:', msg)
        if msg == '/stop':
            break
    print('클라이언트 리시브 쓰레드 종료')

class UniChatCient:
    server_host = 'localhost'  #server ip. localhost. or  127.0.0.1
    server_port = 8888         #server port

    def __init__(self):
        self.client_soc = None

    def conn(self):
        self.client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc.connect((UniChatCient.server_host, UniChatCient.server_port))

    def run(self):
        self.conn()
        t = threading.Thread(target=sendMsg, args=(self.client_soc,))
        t.start()
        t2 = threading.Thread(target=recvMsg, args=(self.client_soc,))
        t2.start()

def main():
    us = UniChatCient()
    us.run()

main()
