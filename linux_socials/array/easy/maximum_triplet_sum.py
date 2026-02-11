# def maximum_triplet_sum(arr):

# 	len_arr = len(arr)
# 	if len_arr < 3:
# 		return Exception("Length of array should be greater than or equal to 3.")

# 	max_sum = float('-inf')
# 	for num1 in arr:
# 		for num2 in arr[1:]:
# 			for num3 in arr[2:]:
# 				if not (num1 == num2 or num2 == num3 or num1 == num3):
# 					max_sum = max(max_sum, num1 + num2 + num3)

# 	return max_sum




def maximum_triplet_sum(arr):

	len_arr = len(arr)
	if len_arr < 3:
		return Exception("Length of array should be greater than or equal to 3.")

	first_max = arr[0]
	second_max = float("-inf")
	third_max = float("-inf")

	for num in arr:

		if num == first_max or num == second_max or num == third_max:
			continue

		if num > first_max:
			third_max = second_max
			second_max = first_max
			first_max = num

		elif num > second_max:
			third_max = second_max
			second_max = num

		elif num > third_max:
			third_max = num

	if second_max == third_max:
		return Exception("needs at least three distinct values.")

	return first_max + second_max + third_max


print(maximum_triplet_sum([3, 15, 2, 8, 9, 1]))
print(maximum_triplet_sum([25, 3, 12, 7, 20, 1]))


