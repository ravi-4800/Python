import unittest
from student import Student

class TestStudent(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('\nsetUpClass\n')
		cls.s1 = Student('Chris', 'Evans', 28000)
		cls.s2 = Student('Robert', 'Downey', 25000)

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')

	def setUp(self):
		print('\nsetUp')

	def tearDown(self):
		print('tearDown	')

	def test_mail(self):

		print('test_mail')
		self.assertEqual(self.s1.mail, 'Chris.Evans@xyz.com')
		self.assertEqual(self.s2.mail, 'Robert.Downey@xyz.com')

	def test_fullname(self):

		print('test_fullname')
		self.assertEqual(self.s1.fullname, 'Chris Evans')
		self.assertEqual(self.s2.fullname, 'Robert Downey')

	def test_apply_hike(self):

		print('test_apply_hike')
		self.s1.apply_hike()
		self.s2.apply_hike()

		self.assertEqual(self.s1.stipend, 29400)
		self.assertEqual(self.s2.stipend, 26250)

if __name__ == '__main__':
	unittest.main()