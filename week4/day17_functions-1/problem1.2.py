

# import random 

# # def gen_numb():

# # 	list1 = [1, 4, 5, 7, 9, 0]

# # 	a = "04444"

# # 	for num in range(len(list1)):
# # 		b = random.choice(list1)
# # 		a += str(b)
# # 	print(a)

# # gen_numb()


import random 

def gen_numb():

	list1 = [1, 4, 5, 7, 9, 0]

	a = ""

	for num in range(len(list1)):
		b = random.choice(list1)
		a = a + str(b)
	print(a+"04444")

gen_numb()
