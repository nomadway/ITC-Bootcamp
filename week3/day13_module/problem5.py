

import os
import random

#sozdat' pustoy katalog na DESKTOPE 
os.mkdir ("/home/buranidze/Desktop/abc")

#sozdaite 5 random files v papke  abc v DESKTOPE

i = 0
while i < 5:
	a = random.randint(1, 1000)
	os.mknod(f"/home/buranidze/Desktop/abc/t(a).txt")

	i += 1
print(i)





