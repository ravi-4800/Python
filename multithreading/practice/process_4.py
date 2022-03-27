# Manager class for arbitraty data structures like list, tuple, dictionary,
# Array, Value

import os
import multiprocessing

def add_new_num(records, num):
	records.append(num)
	print(f"add_new_num = {records}")

def print_numbers(records):
	print(f"records = {records}")

if __name__ == "__main__":

	# records = list([1,2,3,4])
	with multiprocessing.Manager() as manager:
		records = manager.list([1,2,3,4])  # shared memory with complex data stucture
	
		p1 = multiprocessing.Process(target=add_new_num, args=(records, 5))
		p2 = multiprocessing.Process(target=print_numbers, args=(records,))

		p1.start()
		p1.join()

		p2.start()
		p2.join()

