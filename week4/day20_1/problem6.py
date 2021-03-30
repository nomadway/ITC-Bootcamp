# Напишите функцию которая спрашивает у пользователя login и password. 
# Напишите декоратор который шифрует эти данные и возвращает вам зашифрованные данные. 
# (Можете воспользоваться функцией ord и char, можете загуглить...)




#Step-1

def login(shop): 
	user = input("Enter username: ")
	passw = input("Enter password: ")
	shop(user, passw)

#Step-2

@login
def dycript(user, passw):
	i = 0
	for x in user:
		print(i + ord(x))
		break
	e = 0
	for y in passw:
		print(e + ord(y))
		break







