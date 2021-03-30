# 4)ContactList
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name

# class ContacList(list):
#     def init(self,*args):
#         self.new_list = []
#         for i in args:
#             self.new_list.append(i)

#     def search_by_name(self,name):
#         for i in self.new_list:
#             if i == name:
#                 print(f'{i}')
#             else:
#                 pass

# all_contacts = ContacList('Adilet','Ryspek','Sanjar','Alina','Adilet')
# all_contacts.search_by_name('Adilet')