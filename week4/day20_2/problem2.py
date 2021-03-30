#PROBLEM-2

"""
Попросить пользователя ввести текст. В результате вывести процент букв 
в верхнем регистре (заглавные) и в нижнем регистре (прописные).
"""


# ##VERSION-1

# # def text_mixed()

# text_capital = input("Enter in CAPITAL: ")
# print(text_capital)

# text_upper  = input("Enter in Upper: ")
# print(text_upper)
	
# percentage_cap = (len(text_capital) / (len(text_capital) + len(text_upper)) ) * 100
# percentage_up = (len(text_upper) / (len(text_upper) + len(text_capital)) ) * 100

# print(f" Percent in 'CAPITAL' letters is {percentage_cap}. And percent in 'Upper' letters is {percentage_up}.")

# # text_mixed()



# VERSION -2 

def upper_lower():

	text = input("Enter a sentence: ")
	print("Percent in Capital Letters:", sum(1 for c in text if c.isupper())/len(text)*100)
	print("Percent in Lower letters: ", sum(1 for c in text if c.islower())/len(text)*100) 
upper_lower()