import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.bind((socket.gethostname(), 9999))

	s.listen(5)

	print('Server is up and listening ...')

	client, address = s.accept()

	with open('server_files/pexels-photo-6801447.jpeg', 'rb') as image:

		batch = image.read(40960)

		while batch:
			client.send(batch)
			batch = image.read(40960)
			print('One batch is sent.')
print('The whole file has been sent.')