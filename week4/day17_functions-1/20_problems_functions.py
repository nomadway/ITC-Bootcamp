
# 1. Write a Python function to find the Max of three numbers.


# ##VERSION 1 

# a = 10
# b = 20
# c = 50

# # def max_of_two(a, b):
# # 	if a > b:
# # 		return a
# # 	return b

# # def max_of_three(a, b, c):
# # 	return max_of_two(a, max_of_two(b, c))
# # print(max_of_three(a, b, c))


# ###SHORTER VERSION-2
# def max_of_three():
# 	print(max(a,b,c))

# max_of_three()



# 2. Write a Python function to sum all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 

# #Version-1
# def sum_all():
# 	list1 = [8,2,39,5]
# 	print(sum(list1))
# sum_all()

# Version-2
def sum_all():
	list1 = [8,2,39,5]
	a = 0
	for list2 in list1:
		a = a + list2

	print(a)
sum_all()


	

