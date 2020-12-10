import socket
import threading

def sendMsg(soc):
    while True:
        newMsg = input('새 매세지 : ')
        soc.sendall(newMsg.encode())
        if newMsg == '/stop':
            break
    print('msg transfer thread shutdown')

def receiveMsg(soc):
    while True:
        data = soc.recv(1024)
        receivedData = data.decode()
        print(f'세 매세지 수신 : {receivedData}')
        if receivedData == '/stop':
            break
    print('msg receive thread shutdown')

class ChatClient:
    server_address = 'localhost'
    server_port = 8888

    def __init__(self):
        self.client_soc = None

    def conn(self):
        self.client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_soc.connect((ChatClient.server_address, ChatClient.server_port))

    def run(self):
        self.conn()
        t = threading.Thread(target=sendMsg, args=(self.client_soc,))
        t.start()
        t2 = threading.Thread(target=receiveMsg, args=(self.client_soc,))
        t2.start()
def main():
    chat = ChatClient()
    chat.run()

main()