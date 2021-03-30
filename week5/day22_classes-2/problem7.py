
# PPROBLEM-7. Students room:
# ﻿

# Implement Students room using OOP:

# Copy
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# ﻿
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>


#VERSION-1 

class StudentsRoom:

	def __init__(self, name, age, major):
		self.name = name
		self.age = age
		self.major = major 


   	def __repr__(self):
   		return (f"\nname {self.name} age {self.age} major {self.major}")

Steve = StudentsRoom("Steven Schultz", 23, "English")
Johnny = StudentsRoom("Jonathan Rosenberg", 24, "Biology")
Penny = StudentsRoom("Penelope Meramveliotakis", 21, "Physics")

print(Steve)
print(Johnny)
print(Penny)


##VERSION-2

# class Student:
    
#     def __init__(self, name, age, major):
#         self.name = name
#         self.age = age
#         self.major = major


#     def output(self):
#         return "name: ",self.name, "age: ",str(self.age),"major: ",self.major

# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(" ".join(Steve.output()))
# print(" ".join(Johnny.output()))
# print(" ".join(Penny.output()))