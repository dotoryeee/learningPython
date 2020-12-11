#udp는 비 연결 지향 / 신뢰성 없음
import socket
ip = 'localhost'
port = 5555
#udp 서버 소켓 오픈
server_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_soc.bind((ip, port))
#listen()도 없고 accept()도 없다

while True:
    data, addr = server_soc.recvfrom(1024)#udp 패킷을 받는 함수
    #data: 메시지, addr: 상대방 주소(ip, port)
    print('상대방 주소:', addr)
    msg = data.decode()
    if msg == '/stop':
        break
    print('client msg:', msg)
    server_soc.sendto(data, addr)# data:전송 메시지, addr:메시지 받을 주소(ip, port)




