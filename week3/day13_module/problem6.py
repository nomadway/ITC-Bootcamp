

import random

list1 = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", 
 "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

listTeam = 3
l = []
l1 = []
l2 = []
l3 = []
i = 1
while i <= listTeam:
    h = random.choice(list1)
    l.append(h)
    

    for x in range(int(len(list1))):
        if list1 == l:
            del list1[x]
            break

    i += 1
print(l)
i = 1
while i <= listTeam:
    h = random.choice(list1)
    l1.append(h)
    

    for x in range(int(len(list1))):
        if list1 == l1:
            del list1[x]
            break

    i += 1
print(l1)
i = 1
while i <= listTeam:
    h = random.choice(list1)
    l2.append(h)
    

    for x in range(int(len(list1))):
        if list1 == l2:
            del list1[x]
            break

    i += 1
print(l2)
i = 1
while i <= listTeam:
    h = random.choice(list1)
    l3.append(h)
    

    for x in range(int(len(list1))):
        if list1 == l3:
            del list1[x]
            break

    i += 1
print(l3)






