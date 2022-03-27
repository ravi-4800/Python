# communication between processes
# 1. Using Queue

import multiprocessing

def sender(conn, msgs):
	for msg in msgs:
		conn.send(msg)
	conn.close()

def receiver(conn):
	while True:
		msg = conn.recv()
		if msg == 'END':
			break
		print(msg)

if __name__ == "__main__":
	
	msgs = ['hello', 'how', 'hru', 'END']
	parent_conn, child_conn = multiprocessing.Pipe()

	p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
	p2 = multiprocessing.Process(target=receiver, args=(child_conn,))
	

	p1.start()
	p2.start()

	p1.join()
	p2.join() 



