import socket

HOST = '127.0.0.1' #client ip
PORT = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode("Funcionando"))
data = s.recv(1048)

print(data.decode())
