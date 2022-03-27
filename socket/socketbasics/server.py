import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
	s.bind((socket.gethostname(), 7777))
	s.settimeout(5)
	s.listen()
	print('server is running. waiting for connection...')
	try:
		client, addr = s.accept()

		print(client)
		print(addr)

		client.send(bytes('Hello World! This is Ravi', 'utf-8'))
	except socket.timeout:
		print('time out. try to send request in 5 secs')

