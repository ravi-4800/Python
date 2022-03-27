import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

	client_name = input('Enter client name: ')

	sock.connect((socket.gethostname(), 9999))
	sock.send(client_name.encode())

	server_name_raw = sock.recv(1024)
	server_name = server_name_raw.decode()
	print(f'You have connected to the server {server_name}')

	while True:

		recv_msg = sock.recv(1024)
		recv_msg = recv_msg.decode()
		print(server_name + ' : ' + recv_msg)

		send_msg = input(client_name + ' : ')
		sock.send(send_msg.encode())

		if send_msg.lower() == 'bye':
			break


