import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

	server_name = input('Enter server name: ')

	sock.bind((socket.gethostname(), 9999))

	sock.listen(5)
	print(server_name, 'is up. Listening for connections...\n')

	client, address = sock.accept()
	print('Connection to', address, 'established\n')
	print('Client object:', client, '\n')

	client_name_raw = client.recv(1024)
	client_name = client_name_raw.decode()

	client.send(server_name.encode())

	while True:

		send_msg = input(server_name + ' : ')
		client.send(send_msg.encode())

		if send_msg.lower() == 'bye':
			break

		recv_msg = client.recv(1024)
		recv_msg = recv_msg.decode()
		print(client_name, ':', recv_msg)

