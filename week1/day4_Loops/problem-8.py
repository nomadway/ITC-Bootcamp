#Example-1

'''#1. write a variable with number
num = 100

#2. Is this number a three digit number?
"""num1=int(input("Enter your number:"))"""
if(num < 1000 and num > 99):
    print("It's a 3 digit number")
else:
    print("is not a 3 digit number")

#3. Is it EVEN or ODD number?
if (num // 2) != 0:
	print("100 is an EVEN number")
else:
	print("100 is an ODD number")

#4 Can 100 be divided by 31 without remainder
if (num % 17) != 0 or (num > 150) and (num == 13**2):
	print("Show the number") '''


	#Example-2

num = int(input("Enter number: "))

if 100 < num and 999 > num:
	while True:
			print("It's a THREE digit number: ", num)
			break

if num > 0 and num % 2 == 0: 
	while True: 
			print("It's an even number: ", num)
			break

if num % 31 == 0: 
	while True: 
			print("Can be divided by 31 without remainder: ", num)
			break

if num > 100 and num % 17 == 0 or num > 150 and num == 13**2:
	while True: 
			print("The longest condition: ", num)
			break

else:
	while True: 
			print("There is no such number.")
			break










