
#udalit' vse schetnye indeksy do 10


names = ['Jack', 'Jimmy', 'Jackson', 
'Jhon', 'Jackson', 'Jhon',  'Jimmy', 
'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 
'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 
'Jimmy', 'Jack', 'Jackson', 'Jhon',]

#original list
print(names)

for x in range(0, len(names[12]), 2):
	if x % 2 == 0:
		print(names[x])

	#version 2. Easy and simple. But impractical. 

		'''#names.pop(0)
		names.pop(2)
		names.pop(4)
		names.pop(6)
		names.pop(8)
		print(names)'''
	










