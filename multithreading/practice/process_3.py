# Memory is not shared among processes, for sharing memories there are some 
# data structures which are shared among process like
# Array, Value - ctype(means it neads data type and size whatever is necessary)

import os
import multiprocessing

def cal_square(mylist, result):
	
	for idx, item in enumerate(mylist):
		result[idx] = item * item

	print(f"cal_square result = {result[:]}")

if __name__ == "__main__":

	result = multiprocessing.Array('i', 5)  # shared memory
	
	p = multiprocessing.Process(target=cal_square, args=([1,2,3,4,5], result))

	p.start()
	p.join()

	print(f"main result = {result[:]}")
