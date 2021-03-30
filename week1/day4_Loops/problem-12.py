
tuple1 = ("abc", "hello", "123", "3.4", "true", "bye", "yes", "now", "car", "plane", "bottle", "news", "phone", "glass", "paper")

tuple2 = tuple(tuple1[x:x + 3]
	for x in range(0, len(tuple1), 3):
		print(x)




#print (str(tuple2))








