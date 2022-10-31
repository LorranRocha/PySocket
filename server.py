import socket, os, pty

HOST = 'localhost'
PORT = int(input("Digite a porta na qual o cliente se conectará: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #	Abre conexão TCP
s.bind((HOST, PORT))
s.listen()
print("Aguardando conexão com cliente...")
conn, ender = s.accept()

os.system('clear')

print('Conectado em {}'.format(ender))
pty.spawn("/bin/bash")

while True:
	data = conn.recv(1048)
	if not data:
		print("Fechando conexão")
		conn.close()
		break
	conn.sendall(data)
