

# Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить. 
# А затем записывает это всё в файл на рабочем столе menu.txt

def food_drink():
	a = input("Enter food and drink: ")

	r = open("/home/buranidze/Desktop/foodfood.txt", "w")
	r.write(a)

	r.close()


food_drink()





