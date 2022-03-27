import os
import multiprocessing

def cal_square(num):
	print(f"cal_square process_id: {os.getpid()}")
	print(f"square of {num} = {num * num}")

def cal_cube(num):
	print(f"cal_cube process_id: {os.getpid()}")
	print(f"cube of {num} = {num * num  * num}")

if __name__ == "__main__":

	print(f"main process_id: {os.getpid()}")
	
	p1 = multiprocessing.Process(target=cal_square, args=(5,))
	p2 = multiprocessing.Process(target=cal_cube, args=(5,))

	p1.start()
	p2.start()

	print(f"main process_id of p1: {p1.pid}")
	print(f"main process_id of p2: {p2.pid}")

	p1.join()
	p2.join()
