# 1)Student
# Создайте класс Student, конструктор которого имеет параметры name, lastname
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
# Программирование.”

class student():

    def init(self, name, lastname, departament,year_of_entrance):
        self.name=name  
        self.lastname=lastname
        self.departament=departament
        self.year_of_entrance=year_of_entrance

    def get_student_info(self):
        print(f'Меня зовут {self.name} фамилия {self.lastname} окончил учебу {self.departament}на факультете{self.year_of_entrance}')

s= student('вася','иванов',2017,'программиста')
s.get_student_info()