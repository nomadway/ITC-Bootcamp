num = -100
num2 = num

ifCont = 0
while num <= 100:
    if num % 13 == 0 and num % 2 == 0:
        print(num, num ** 2)
        ifCont += 1
    num += 1
print(ifCont)

ifCont2 = 0
while num2 <= 100:
    if num2 % 2 == 1:
        ifCont2 += 1
        print(num2)
    num2 += 7
print(ifCont2)



'''num = -100
num2 = num
ifCont = 0
ifCont2 = 0


while num <= 100:
	if num % 13 == 0 and num % 2 == 0:   #1 uslovie 
		print(num, num**2)
		ifCont +=1
	num+=1
print(ifCont)	

while num2 <= 100:
	if num2 % 2 == 1:
		ifCont2 += 1
		print(num2)

	num2 += 7
print(ifCont2)'''




