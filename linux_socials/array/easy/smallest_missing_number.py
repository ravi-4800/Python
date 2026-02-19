def smallest_missing_number(arr=None):

	left, right = 0, len(arr) - 1

	while left <= right:
		mid = (left + right) // 2

		if arr[mid] == mid:
			left = mid + 1

		elif arr[mid] > mid:
			right =  mid - 1
			
	return left


print(smallest_missing_number([0, 1, 3, 6, 8]))
print(smallest_missing_number([4, 5, 6]))
print(smallest_missing_number([0, 1, 2, 3]))