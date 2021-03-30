# Напишите функцию которая спрашивает число N и генерирует вам List состоящий из N разных элементов.

# Напишите функцию которая спрашивает число N и генерирует вам List состоящий из N разных элементов.


import random

def rand_numlist(a):
    k = []
    i = 0
    while i < a:
        k.append(random.randint(1,1000))
        i+=1
    print(k)


a = int(input('input number: '))
rand_numlist(a)