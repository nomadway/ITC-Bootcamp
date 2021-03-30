

# Создайте 4 функции: add(), substract(), multiply(), divide() 
# которые будут принимать по 2 аргумента и возвращать результат: 
# сложения, вычитания, умножения и деления

# def multiply(c,n):
#     return c * n

# print(multiply(25,5))

#ADD
def add(number_1, number_2):

	sum = number_1 + number_2
	return sum 
	

print(add(10, 20))

##SUB
def substract (num_1, num_2):
	sum = num_1 - num_2
	return sum


print(substract( 100, 50))

##MULT
def multiply (num_3, num_4):
	sum = num_3 * num_4
	return sum
	

print(multiply(2, 5))

##DIV
def divide (num_5, num_6):
	sum = num_5/num_6
	return sum
	

print(divide(10, 5))