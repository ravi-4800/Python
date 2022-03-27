import socket
from product import Product
import pickle
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.bind((socket.gethostname(), 7777))

	s.listen()
	print('server is running. waiting for connection...')

	client, addr = s.accept()
	products = [Product('P001', 'Bottle', 20),
				Product('P002', 'Bottle', 20),
				Product('P003', 'Bottle', 20),
				Product('P004', 'Bottle', 20),
				Product('P005', 'Bottle', 20)]
	for product in products:
		client.send(pickle.dumps(product))
		print(product.pid)
		time.sleep(2)

