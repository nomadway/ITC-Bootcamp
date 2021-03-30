
# 3)Car
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”

# class Car():

# 	def __init__(self, make, model, year, odometer, fuel):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer = 0
# 		self.fuel = 70 

# 	def drive(self):

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def __add_distance(self, distance):
        self.odometer += distance
        print(str(self.odometer) + ' km we traveled')

    def drive(self, distance):
        consumption = self.fuel * 10
        if distance > consumption:
            print('Need to fill the tank')
        else:
            Car.__add_distance(self, distance)
            will_use = distance // 10
            Car.__subtract_fuel(self, will_use)

    def __subtract_fuel(self, will_use):
        self.fuel -= will_use
        print(str(self.fuel) + ' gasoline is none')


my_car = Car('lada', 'kalina', 2004)
my_car.drive(500)
my_car.drive(50)


