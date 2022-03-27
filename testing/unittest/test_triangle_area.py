import unittest
import triangle_area

class Testing(unittest.TestCase):

	# or we can also write this function name
	def runTest(self):
		result = triangle_area.triangle(10, 5)
		print('Hi')
		self.assertEqual(result, 25)

	# function must start with test to be executed
	def test_triangle(self):
		result = triangle_area.triangle(10, 5)
		print('Hello')
		self.assertEqual(result, 25)

if __name__ == '__main__':
	unittest.main()