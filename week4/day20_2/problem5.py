

##PROBLEM-5

"""
'С помощью рекурсии выведите числа фибоначи'
"""

def recur_fibo(x):
   if x <= 1:
       return x
   else:
       return(recur_fibo(x-1) + recur_fibo(x-2))

print (recur_fibo(15))