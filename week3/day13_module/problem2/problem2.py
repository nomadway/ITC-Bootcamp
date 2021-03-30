
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]


import random

list1 = []
i = 0
random.choice(names)
while i<4:
	list1.append(random.choice(names))
	i=i+1
print(list1)