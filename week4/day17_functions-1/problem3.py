# Создайте функцию сложения, затем функцию вычитания двух чисел...
# Создайте 3-ю функцию которая вызывает первые 2 внутри себя.

def sum(a,b):
    print(a+b)
def minus(a,b):
    print(a-b)
def minusplus():
    sum(2,4)
    minus(5,1)
minusplus()