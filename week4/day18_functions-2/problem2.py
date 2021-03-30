
# Написать Функцию которая принимает предложение как аргумент, 
# считает количество букв и возвращает сколько символов он ввёл. 
# НЕ ИСПОЛЬЗОВАТЬ функцию len()


def song_txt(song_name):
	a = 0
	for i in song_name:
		a = a + 1
	return a


print(song_txt("When september ends!"))