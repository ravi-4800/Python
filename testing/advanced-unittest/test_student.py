import unittest
from student import Student

class TestStudent(unittest.TestCase):

	def test_mail(self):

		s1 = Student('Chris', 'Evans', 28000)
		s2 = Student('Robert', 'Downey', 25000)

		self.assertEqual(s1.mail, 'Chris.Evans@xyz.com')
		self.assertEqual(s2.mail, 'Robert.Downey@xyz.com')

		s1.first = 'John'
		s2.first = 'James'

		self.assertEqual(s1.mail, 'John.Evans@xyz.com')
		self.assertEqual(s2.mail, 'James.Downey@xyz.com')

	def test_fullname(self):
		
		s1 = Student('Chris', 'Evans', 28000)
		s2 = Student('Robert', 'Downey', 25000)

		self.assertEqual(s1.fullname, 'Chris Evans')
		self.assertEqual(s2.fullname, 'Robert Downey')

		s1.first = 'John'
		s2.first = 'James'

		self.assertEqual(s1.fullname, 'John Evans')
		self.assertEqual(s2.fullname, 'James Downey')

	def test_apply_hike(self):
		
		s1 = Student('Chris', 'Evans', 28000)
		s2 = Student('Robert', 'Downey', 25000)

		s1.apply_hike()
		s2.apply_hike()

		self.assertEqual(s1.stipend, 29400)
		self.assertEqual(s2.stipend, 26250)

if __name__ == '__main__':
	unittest.main()