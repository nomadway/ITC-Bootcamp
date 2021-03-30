# Напишите программу которая определяет ПРОСТЫЕ ЧИСЛА. 
# Простое число - это число которое делится только на себя и на 1.

def numb():
    num = int(input("Please write any numbers: "))
    
    for i in range(num):
        try:
            if num / num == 1 and num / 1 == num:
                return f"{num} - this is simple number"
        
print(numb)