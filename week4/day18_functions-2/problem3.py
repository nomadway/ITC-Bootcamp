

# Напишите функцию которая принимает 2 Dictionary и добавляет втрорую Dictionary к первой.


# Version1 

# def akm(a,b):
#   a.update(b)
#   print(a)
# a={input(''):input('')}
# b={input(''):input('')}
# print(a,b)


#Version 2

# def dic(a,b):
#     a.update(b)
#     print(a)

# a = {input(''): input()}
# b = {input(''): input()}

# dic(a,b)



# Version 3 
# def sum_dict(*args, **kwargs):
# 	a = []
# 	for key, value in kwargs.items():
# 		dict_1 = {key: value}
# 		a.append(dict_1)
# 		# a.append(value)
# 	print(a)	

# sum_dict(car= "ferrari", color= "white")	




#VERSION 4


# dict1 = {"car": "bentley", "year": 2020}
# dict2 = {"car": "ferrari", "year": 2015}

# def two_dict(dict1, dict2):

#    dict3 = {**dict1, **dict2}
#    for key, value in dict3.items():
#        if key in dict1 and key in dict2:
#                dict3[key] = [value , dict1[key]]
#    return dict3

# dict3 = two_dict(dict1, dict2)
# print('Dictionary 3 :')
# print(dict3)


