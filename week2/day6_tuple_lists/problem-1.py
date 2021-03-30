
#Version1 
#create empty list
empty_list = []

print(empty_list)

#fill the list with the below info in the order provided
name = "X-man"
dob = "150 years old"
lang = "python"

empty_list.extend([name, dob, lang])

print(empty_list)



#version 2

list1 = []
print(list1)

list1.append("X-Man")
list1.append("150 years old")
list1.append("python")
print(list1)