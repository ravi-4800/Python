def sqrt(x):

	if x <= 1: return x

	left, right = 1, x

	while left <= right:

		mid = (left + right) // 2
		square = mid * mid

		if square == x:
			return mid

		elif square < x:
			ans = mid
			left = mid + 1

		else:
			right = mid - 1

	return ans

print(sqrt(0))
print(sqrt(1))
print(sqrt(2))
print(sqrt(8))
print(sqrt(25))
print(sqrt(17))
