# Задание 6:
#     Дано четырехзначное число. Верно ли, что цифры в нем расположены по убыванию? 
#     Например, 4311 - нет, 4321 - да, 5542 - нет, 5631 - нет, 9871 - да.


number = input("Enter number: ")

descending = True

for i in range(len(number)-1):
    if int(number[i]) <= int(number[i+1]):
        descending = False
        break

if descending:
    print(number, '- yes')
else:
    print(number, '- no')