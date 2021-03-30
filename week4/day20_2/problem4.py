
###PROBLEM-4

"""
"Напишите функцию которая принимает в себя словарь где ключи это номера а значения страны. 

Попросите пользователя ввести страну или ключ и выдайте ему результат."
d = {'1': 'kyrgyzstan', '2': 'kazahstan'}
"""
d = {'1': 'kyrgyzstan', '2': 'kazahstan'} 

def country(name):
	x = input("Enter 'Key' or 'Value': ")
	for key, value in name.items():
		if key in x:
			print(value)
		if value in x:
			print(key)

country(d)


