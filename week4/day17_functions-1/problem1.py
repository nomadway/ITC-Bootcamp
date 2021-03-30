
# Создайте функцию которая которая берёт лист делит его пополам и обе стороны разворачивает в противоположную сторону. Пример:
# Оригинальный Лист:
# list_1 = ['name', 'age', '1', '19']
# Изменённый Лист:
# list_1 = ['age', 'name', '19', '1']



#VERSION 0

# def twicelistrev():
#     a = input().split()
#     print((list(reversed(a[:(int(len(a)) // 2)]))) + (list(reversed(a[(int(len(a)) // 2)::]))))

# twicelistrev()


#VERSION 1

# def unf():
#     list_1 = ['name', 'age', '1', '19']
#     a = list_1[0:2]
#     b = list_1[2:4]
#     t = a.reverse()
#     r = b.reverse()
#     print(a, b)
# unf()

#VERSION 2 

# def reverse(): 

# 	list1 = ['name', 'age', '1', '19']
# 	order = [1, 0, 3, 2]

# 	list1 = [list1[i] for i in order]
	   
# 	print(list1)

# reverse()


#VERSION 3
# def split_list(list_1_list):
#     half=len(list_1_list)//2
#     return list_1_list[:half], list_1_list[half:]
# list_1 =['name','age','1','19']

# list_2,list_3=split_list(list_1)
# print(split_list(list_1))
# list_2.reverse()
# list_3.reverse()
# mergedlist=list_2+list_3
# print(mergedlist)











