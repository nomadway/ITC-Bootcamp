
class Student:
	def __init__(self, name, age, education):	
		self.name = name
		self.age = age
		self.education = education


	def get_student_info(self):
		print(f"This is {self.name} he is {self.age}. He studies at {self.education}.")

s = Student("Rustam", 18, "BGU")
s.get_student_info()
