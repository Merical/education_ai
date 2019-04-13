import socket
# ip_port = ('127.0.0.1', 8080)
ip_port = ('192.168.43.167', 8080)
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(ip_port)
sk.listen(5)

print('Waiting for message ...')
while True:
    clientsocket, addr = sk.accept()
    data = clientsocket.recv(102400)
    print(data.decode())
    clientsocket.close()
