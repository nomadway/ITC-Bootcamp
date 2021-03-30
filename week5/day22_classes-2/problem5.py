# 5)AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)

# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.

# Where soldier will fire from a gun and reload, and fire one more time.

class Soldier:
#     def init(self, name, guns):
#         self.name=name
#         self.guns=guns
# class Guns():
#     def shoots(self):
#         print(f'{self.name} shoots from: {self.guns}')
#         self.ammunition = 10
#         while self.ammunition > 0:
#             self.ammunition -= 1
#             print('tigi-tigitishh')

#         if self.ammunition == 0:
#             self.reloads()
#         else:
#             pass


#     def reloads(self):
#         self.reload = input('остановить стрельбу? y/n: ')
#         if self.reload == 'y':
#           self.shoots()
#         else:
#             pass


# class Act_of_Shooting(Soldier, Guns):
#     def init(self, name, gun):
#         Soldier.init(self, name, gun)


# soldier1 = Act_of_Shooting('Ryan', 'AK47')
# soldier1.shoots()