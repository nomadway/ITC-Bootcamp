
# Нужно создать класс который принимет модель ноутбука(Acer, Asus, ...) и возвращает 
# полную комплектацию ноутбука со всеми характеристиками.
# В характеристики должны входить:
# Процессор
# Оперативная Память
# Видео карта
# Жёсткий Диск
# Материнская плата
# Размер экрана
# Для каждой характеристики создайте внутри класса функцию которая добавляет по одной характеристики к Dictionary.
# В итоге Ваш класс должен вернуть Dictionary в котором перечислены: 
# Модель Ноутбука и его Характеристики. 

###VERSION 1 
class Laptop:
	def __init__(self, processor, memory, card, disk, board, size):
		self.processor = processor
		self.memory = memory
		self.card = card
		self.disk  = disk
		self.board = board
		self.size = size 

	def get_HP_info(self):
		print({
			"processor": self.processor,
			"memory": self.memory,
			"card": self.card,
			"disk": self.disk,
			"board": self.board,
			"size": self.size})

l = Laptop("Intel", "8GB", "double", "500 mgb", "super size", "14 inch")
l.get_HP_info() 

###VERSION-2 ####NOT working with **Kwargs 

# class Laptop:
# 	def __init__(self, processor, memory, card, disk, board, size):
# 		self.processor = processor
# 		self.memory = memory
# 		self.card = card
# 		self.disk  = disk
# 		self.board = board
# 		self.size = size 



# print(f"This is {self.processor}. Its RAM memory is {self.memory}. It has {self.card} card. The laptop's disk size is {self.disk} and the mother board is {self.board}. HP's screen size is {self.size}.")