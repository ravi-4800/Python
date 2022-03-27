import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.connect((socket.gethostname(), 7777))

	while True:
		msg = s.recv(1024)

		if not msg:
			print('No more msgs')
			break
		product = pickle.loads(msg)
		print(product.pid)
		print(product.pname)
		print(product.pprice)