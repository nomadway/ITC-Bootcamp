

a = open ('password.txt', 'w')
login = input ('Enter login: ')
password = input ('Enter password: ')
a.write (f'Hello , your login ID is {login} ? Your password is {password} ?')
a.close()
with open ('password.txt','r') as file:
    print (file.read())



