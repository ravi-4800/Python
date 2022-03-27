def foo(n, k):
	if n == 1:
		return 1
	elif n == 2 or n == 3 or n == 4:
		return k + 1
	else:
		if (n - 2) % 3 == 0:
			return ((n-2)//3)*k + k +1 
		elif (n - 3) % 3 == 0:
			return ((n-3)//3)*k + k +1
		else:
			return ((n-4)//3)*k + k +1

print(foo(8, 3))































# import os
# import multiprocessing

# result = []

# def cal_square(mylist):
# 	global result
# 	for item in mylist:
# 		result.append(item*item)

# 	print(f"cal_square result = {result}")

# if __name__ == "__main__":
	
# 	p = multiprocessing.Process(target=cal_square, args=([1,2,3,4,5],))

# 	# cal_square([1,2,3,4,5])

# 	p.start()
# 	p.join()

# 	print(f"main result = {result}")
