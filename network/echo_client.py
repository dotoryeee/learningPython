import socket

HOST = 'localhost'
PORT = 8888

#통신할 소켓 오픈 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#서버에 연결요청. server ip, port
client_socket.connect((HOST, PORT))

while True:
    msg = input('msg:')
    client_socket.sendall(msg.encode())

    data = client_socket.recv(1024)
    print('Received', data.decode())
    if msg=='/stop':
        break

client_socket.close()
