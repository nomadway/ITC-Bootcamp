
# 1) Находим минимальное положительное целое число, которого нет в списке. 
# Если список содержит только отрицательные числа, верните 1. 
# Все элементы являются целыми числами:
# Пример: [1,2,3,4,6] - Ответ 5
# Пример: [1,2,3] - Ответ 4
# Пример: [-1, -2, -6] - Ответ 1
# '''

def min1(a):  
    for i in range(1, max(a)):
        if i not in  a:
            return i
print(min1([1,2,3,4,6])) 


def min2(b):
    for x in range(1, len(b)+2):
        if x not in b:
            return x
print(min2([1,2,3]))


def min3(a):
    for i in range(1, len(a)+1):
        if i not in  a:
            return i
print(min3([-1, -2, -6])) 