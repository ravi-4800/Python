# synchronization

import os
import multiprocessing

def withdraw(balance, amount, lock):
	for _ in range(amount):
		lock.acquire()
		balance.value = balance.value - 1
		lock.release()

def deposit(balance, amount, lock):
	for _ in range(amount):
		lock.acquire()
		balance.value += 1
		lock.release()

if __name__ == "__main__":

	for _ in range(10):
		balance = multiprocessing.Value('i', 100)
		lock = multiprocessing.Lock()

		p1 = multiprocessing.Process(target=deposit, args=(balance, 100000, lock))
		p2 = multiprocessing.Process(target=withdraw, args=(balance, 100000, lock))

		p1.start()
		p2.start()

		p1.join()
		p2.join()

		print(f"balance = {balance.value}")

