import unittest
import rectangle_perimeter
import sys

class TestPerimeter(unittest.TestCase):

	def test_perimeter(self):
		self.assertEqual(rectangle_perimeter.get_perimeter(4, 5), 18)

	# def test_error(self):
	# 	self.assertRaises(ValueError, rectangle_perimeter.get_perimeter, 4, 0)

	# we can write test_error like this as well
	# def test_error(self):
	# 	with self.assertRaises(ValueError):
	# 		rectangle_perimeter.get_perimeter(4, 0)

	# we can skip a particular test
	# @unittest.skip('Temporarily skipping this test')
	# def test_error(self):
	# 	with self.assertRaises(ValueError):
	# 		rectangle_perimeter.get_perimeter(4, 0)

	# we can also skip the test with if condition
	# @unittest.skipIf(sys.version_info[0] < 3, 'requires python version 3 or higher')
	# def test_error(self):
	# 	with self.assertRaises(ValueError):
	# 		rectangle_perimeter.get_perimeter(4, 0)

	# we can also skip the test with Unless condition
	@unittest.skipUnless(sys.platform.startswith('linux'), 'requires linux os')
	def test_error(self):
		with self.assertRaises(ValueError):
			rectangle_perimeter.get_perimeter(4, 0)

if __name__ == '__main__':
	unittest.main()