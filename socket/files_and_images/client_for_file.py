import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.connect((socket.gethostname(), 9999))
	file = open('client_files/received_file.txt', 'wb')

	while True:

		batch = s.recv(40960)

		if not batch:
			print('No more data to receive')
			break

		file.write(batch)
		print('One batch is received.')
	file.close()
print('Whole file received successfully')
		

