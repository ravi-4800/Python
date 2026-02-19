# def sort(arr):

# 	c0, c1, c2 = 0, 0, 0
# 	for num in arr:
# 		if num == 0:
# 			c0 += 1
# 		elif num == 1:
# 			c1 += 1
# 		else:
# 			c2 += 1
# 	return [0] * c0 + [1] * c1 + [2] * c2


def sort(arr):

	l, m, h = 0, 0, len(arr) - 1

	while m <= h:

		if arr[m] == 0:
			arr[l], arr[m] = arr[m], arr[l]
			l += 1
			m += 1   # important (take a note of it)

		elif arr[m] == 1:
			m += 1

		else:
			arr[m], arr[h] = arr[h], arr[m]
			h -= 1

	return arr

print(sort([2, 0]))
print(sort([0, 1]))
print(sort([0, 1, 2, 0, 1, 2]))
print(sort([1, 2, 0, 0, 1, 2]))
