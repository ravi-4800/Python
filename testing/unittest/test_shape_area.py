import unittest
import shape_area

class Testing(unittest.TestCase):

	def test_triangle(self):
		self.assertEqual(shape_area.triangle(10, 5), 25)

	def test_rectangle(self):
		self.assertEqual(shape_area.rectangle(7, 6), 42)

	def test_square(self):
		self.assertEqual(shape_area.square(5), 25)

if __name__ == '__main__':
	unittest.main()


# To run individual test, we use
# python -m unittest test_shape_area.Testing.test_triangle test_shape_area.Testing.test_triangle -v
# -v = verbose mode
# -q = quite mode