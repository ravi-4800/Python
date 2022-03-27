class Student:

	stipend_hike_rate = 1.05

	def __init__(self, first, last, stipend):

		self.first = first
		self.last = last
		self.stipend = stipend

	@property
	def mail(self):
		return f"{self.first}.{self.last}@xyz.com"
	
	@property
	def fullname(self):
		return f"{self.first} {self.last}"
	
	def apply_hike(self):
		self.stipend = int(self.stipend) * self.stipend_hike_rate

