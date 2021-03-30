
# Напишите функцию которая генерирует 100 рандомных чисел в диапазоне от 10 до 50 и возвращает их в листе. 
# Напишите ДЕКОРАТОР для этой функции которая удалит все дубликаты в первой функции и вернёт всё так же лист.


import random

def remove_duplicate(hello):				#Step 3
	a = []
	for c in hello():
		if c not in a:
			a.append(c)
	print(a)					

@remove_duplicate					#Stp 2
def rand_num():						#Step 1
	y = []
	for i in range(100):
		x = random.randint(10, 50)
		y.append(x)
	return y 







