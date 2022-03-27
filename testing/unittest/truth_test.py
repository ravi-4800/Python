import unittest

class TruthTest(unittest.TestCase):

	def test_assert_true(self):
		self.assertTrue((5*2) == 10)

	def test_assert_false(self):
		self.assertFalse((5*2) == 2)

if __name__ == '__main__':
	unittest.main()