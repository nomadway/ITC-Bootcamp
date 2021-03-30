
# 2)Airplane
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекAта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying

# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.

class Airplane():

    def init(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        message_take = f"{self.make} {self.model} was take off."
        return message_take

    def fly(self, km):
        self.odometer += km
        message_fly = f"{self.make} flew {self.odometer}km at a speed of {self.max_speed}km/h."
        return message_fly

    def land(self):
        self.is_flying = False
        message_land = f"{self.make} has landed, it's odometer shows {self.odometer}km."
        return message_land

go = Airplane("Boeing", "747", "2019", 600)
print(go.take_off())
print(go.fly(500))
print(go.fly(500))
print(go.land())
