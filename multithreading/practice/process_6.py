# pooling

import os
import multiprocessing

def cal_square(num):
	print(f"square of {num} is {num * num}")
	return num * num

if __name__ == "__main__":
	
	numbers = [1, 2, 3, 4, 5, 6, 7]

	pool = multiprocessing.Pool()

	res = pool.map(cal_square, numbers)

	print(f'res = {res}')


