import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.connect((socket.gethostname(), 9999))
	image = open('client_files/received_image.png', 'wb')

	while True:

		batch = s.recv(40960)

		if not batch:
			print('No more data to receive')
			break

		image.write(batch)
		print('One batch is received.')
	image.close()
print('Whole file received successfully')
		

