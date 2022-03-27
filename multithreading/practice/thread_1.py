





























# import threading
# import os
# import time


# def foo1():
# 	print("foo1")
# 	print(f"foo1: {threading.current_thread().name}")
# 	time.sleep(2)

# def foo2():
# 	print('foo2')
# 	print(f"foo2: {threading.current_thread().name}")
# 	time.sleep(2)

# if __name__ == "__main__":

# 	start_time = time.time()

# 	for _ in range(3):
# 		t1 = threading.Thread(target=foo1)
# 		t2 = threading.Thread(target=foo2)

# 		t1.start()
# 		t1.join()

# 		t2.start()
# 		t2.join()

# 	print(f"mian: {threading.current_thread().name}")

# 	end_time = time.time()
# 	print(f"time = {end_time - start_time}")

# 	# t1 = threading.Thread(target=foo1)
# 	# t2 = threading.Thread(target=foo2)


