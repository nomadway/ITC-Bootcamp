
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
#1 Dobavte v menu napitki kak klyuch DRINKS
menu.update(drinks = '')
print(menu)

#2 dobati' coca-cola, sprite 
'''menu.update(drinks = 'Cola' 'Sprite' 'Fanta')
print(menu)'''

menu["drinks"] = ["COla", "Fanta", "Sprite"]
print(menu)