# Создайте функцию которая принмает тип данных dictionary, 
# но возвращает два Tuple в одном из них все ключи, в другом только значения.

def dictup(**k):
    a = []
    b = []
  
    for key, value in k.items():
        a.append(key)
        b.append(value)   
    print(tuple(a))
    print(tuple(b))
dictup( name = 'azim', level = 'begginer')