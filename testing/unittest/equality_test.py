import unittest

class EqualityTest(unittest.TestCase):

	def test_equal(self):
		self.assertEqual(2, 4-2)

	def test_not_equal(self):
		self.assertNotEqual(5, 4-2)

if __name__ == '__main__':
	unittest.main()