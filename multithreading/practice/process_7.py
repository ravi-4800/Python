# communication between processes
# 1. Using Queue

import multiprocessing

def cal_square(numbers, queue):
	for num in numbers:
		queue.put(num*num)

def print_square(queue):
	while not queue.empty():
		print(queue.get())

if __name__ == "__main__":
	
	numbers = [1, 2, 3, 4, 5, 6, 7]
	queue = multiprocessing.Queue()

	p1 = multiprocessing.Process(target=cal_square, args=(numbers, queue))
	p2 = multiprocessing.Process(target=print_square, args=(queue,))

	p1.start()
	p1.join()

	p2.start()
	p2.join() 



