import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.connect((socket.gethostname(), 7777))

	msg = s.recv(1024)

	print(msg.decode('utf-8'))
