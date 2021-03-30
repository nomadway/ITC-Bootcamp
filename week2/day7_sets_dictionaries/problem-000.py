
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}

#1 Dobavit v menu "beshbarmak" kotoryi stoit 130 som
menu["beshmarmak"] = 130
print(menu)

#2 Pomenyat tsenu lagmana na 135 
menu.update({"lagman" : 135})
print(menu)

#3 Udalit borsh 
menu.pop("borsh")
print(menu)