
###OBJECT ORIENTED PROGRAMMIN IN PYTHON - Beginner Crash Course
#https://www.youtube.com/watch?v=-pEs-Bss8Wc 

#position, name, age, level, salary

# soft_eng1["Software Engineer", "Uran", "21", "mid level", "$120,000"]
# soft_eng2["Software Engineer", "Mary", "31", "junior", "$85,000"]


# ####********SECTION-1 
# #class

# class SoftwareEngineer:

# 	def __init__(self, name, age, level, salary): 
# 		#instance attributes
# 		self.name = name
# 		self.age = age
# 		self.level = level
# 		self.salary = salary 

# #instance 
# soft_eng1 = SoftwareEngineer("Uran", "37", "mid level", "$120,000")

# print(soft_eng1.name, soft_eng1.salary)


# ####********SECTION-2	FUNCTIONS IN CLASSES 

# soft_eng1 = ["Software Engineer", "Uran", "21", "mid level", "$120,000"]
# soft_eng2 = ["Software Engineer", "Mary", "31", "junior", "$85,000"]


# class SoftwareEngineer:

# 	def __init__(self, name, age, level, salary): 
# 		#instance attributes
# 		self.name = name
# 		self.age = age
# 		self.level = level
# 		self.salary = salary 

# 		#instance method 
# 	def code(self):
# 		print(f"{self.name}, is writing code.")

# 	def code_in_language(self, language):
# 		print(f"{self.name}, is writing code in {language}.")

# 	def __str__(self): 
# 		information = f"name = {self.name}, age = {self.age}, level = {self.level}, salary = {self.salary}."
# 		return information
	
# 	def __eq__(self, other):
# 		return self.name == other.name and self.age == other.age 
	
# 	@staticmethod 
# 	def entry_salary(age):
# 		if age < 25:
# 			return 5000
# 		if age < 30:
# 			return 7000
# 		return	15,000






# #instance 
# soft_eng1 = SoftwareEngineer("Uran", 37, "senior", "$180,000")
# soft_eng2 = SoftwareEngineer("Mary", 25, "junior", "$85,000")
# soft_eng3 = SoftwareEngineer("John", 32, "middle", "$130,000")

# soft_eng1.code()
# soft_eng2.code()
# soft_eng1.code_in_language("Python...")
# soft_eng2.code_in_language("JavaScript...")

# print(soft_eng1.entry_salary(20))
# print(SoftwareEngineer.entry_salary(25))

# # print (soft_eng1.information())


#SECTION 2 RECAP:
# instance method(self)
# can take arguments and can return values
# special "dunder" method (__str__ and __eq__)
# staticmethod


##****************SECTION - 3  INHERITENCE********************#####
#Inheritence (Parent class, Child class) is when one class takes on the method and attributes of another class.
#CHild classes are derived from PARENT classes and inherit all of PARENT'S attributes and methods, but can also
#extend and override attributes and methods that are unique to themseles (Child classes). 

#Parent class/inherits/extends, overrides 
# class Employee:
# 	def __init__(self, name, age, salary):
# 		self.name = name
# 		self.age = age 
# 		self.salary = salary


# 	def work(self):
# 		print(f"{self.name} is working really hard....")



# #Child class 
# class SoftwareEngineer(Employee):
# 	def __init__(self, name, age, salary, level):
# 		super().__init__(name, age, salary)
# 		self.level = level

# 	def debug(self):				#creating a function specific only to Child class - SoftwareEngineer
# 		print(f"{self.name} is debugging.....")

		


# class Designer(Employee):
	
# 	def draw(self):					#creating a function specific only to Child class - Designer 
# 		print(f"{self.name} is drawing.....")


# se = SoftwareEngineer("Max", 25, 6000, "Junior")
# # print(se.name, se.age)
# se.work()
# se.debug()


# d = Designer("Philipp", 27, 7000)
# d.work()
# d.draw()

###****POLYMORPHISM***#### (means MANY SHAPES and is related to INHERITENCE)
#it can use two different class types in the same way. 
#A code can be written for a SUPER CLASS that can also work on SUBCLASSES. 

# employees = [SoftwareEngineer("Max", 25, 6000, "Junior"),
# 			SoftwareEngineer("Lisa", 30, 9000, "Senior"),
# 			Designer("Philipp", 27, 7000)]


# def motivate_employees(employees):
# 	for employee in employees:
# 		employee.work()

# motivate_employees(employees):


##**RECAP:
# inheritence: ChildClass(BaseClass)
# inherit, extend, override
# super().__init__()
# POLYMORPHISM




####****SECTION 4    ENCAPSULATION****#####
#is a mechanism of hiding data implementation. Restricting access to certain info. 


# class SoftEng:

# 	def __init__(self, name, age):
# 		self.name = name				#This is public attribute
# 		self.age = age 					#This is public attribute 
# 		self._salary = None				#This is kept private
# 		self._num_bugs_solved = 0		#This is kept private 

# 	def code(self):
# 		self._num_bugs_solved += 1

# 		#getter	(This should be the only way from outside to access the SALARY attribute)
# 	def get_salary(self):
# 		return self._salary
		
# 		#setter (This should be the only way from outside to access the SALARY attribute)
# 	def set_salary(self, base_value):
# 		self._salary = self.__calculate__salary(base_value)
		

# 	def __calculate__salary(self, base_value):
# 		if self._num_bugs_solved < 10:
# 			return base_value
# 		if self._num_bugs_solved < 100:
# 			return base_value * 2
# 		return base_value * 3



# se = SoftEng("Max", 25)
# print(se.name, se.age)

# se.set_salary(6000)
# print(se.get_salary())



####******SECTION-4   ABSTRACTION*****
#Is a natural extension of encapsulation. Applying abstraction means that each object should only 
#a high level mecahnism for using it. This mechanism should hide internal mechanism details. 


###****SECTION 5  PROPERTIES ****######

# class SoftEng:

# 	def __init__(self):
# 		self._salary = None				#This is kept private
	 
 

# 		#getter	(This should be the only way from outside to access the SALARY attribute)
# 	def salary(self):
# 		return self._salary
		
# 		#setter (This should be the only way from outside to access the SALARY attribute)
# 	def set_salary(self, value):
# 		self._salary = value
		


# se = SoftEng()


# se.salary = 6000
# print(se.salary)











####****OOP PYTHON   TELUSKO YOUTUBE 
# class Computer:
	
# 	def __init__(self, cpu, ram): 
# 		self.cpu = cpu
# 		self.ram = ram


# 	def config(self):
# 		print("config is", self.cpu, self.ram)

# comp1 = Computer("i5", 16)
# comp2 = Computer("Ryazen 3", 8)

# comp1.config()
# comp2.config()

#******************************************
# class Computer:
# 	pass


# c1 = Computer()
# c2 = Computer()

# print(id(c1))
# print(id(c2))



#*************************************

# class Customer:
# 					#parameters
# 	def __init__(self, name, membership_type):
# 		self.name = name
# 		self.membership_type = membership_type
# 		# print("Customer account created!")

# 				#arguments 
# c1 = Customer("John Wick", "Platinum account") #creating object-1
# c2 = Customer("Bruce Lee", "Gold Account")		#creating object-2
# print(c1.name, c1.membership_type)
# print(c2.name, c2.membership_type)


##When there's a long list of customers, it's best to scale the list with proper code.

class Customer:
					#parameters
	def __init__(self, name, membership_type):
		self.name = name
		self.membership_type = membership_type

	def update_membership(self, new_membership):
		self.membership_type = new_membership



customers = [Customer("John Wick", "Platinum account"), 
			Customer("Bruce Lee", "Gold Account")]

print(customers[1].membership_type)
customers[1].update_membership("Platinum Account")  #this upgrades Bruce's Gold account to Platinum.
print(customers[1].membership_type)


