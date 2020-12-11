import socket
ip = 'localhost'
port = 5555

#udp 소켓 오픈
client_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('msg:')
    client_soc.sendto(msg.encode(), (ip, port))
    if msg == '/stop':
        break
    data, addr = client_soc.recvfrom(1024)
    print(addr, ' recv msg:'+data.decode())
