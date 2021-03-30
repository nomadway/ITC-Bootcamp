
s = open("problem3.txt", "r")
s.read("Hello Monday!")
s.close()

if "w" in s.read():
	print("Yes")
else:
	print("No") 