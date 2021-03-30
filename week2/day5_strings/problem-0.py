
'''txt = "Hello Jessica. Let's dine tonight."
txt1 = len(txt)
lower_case = txt.lower()
upper_case = txt.upper()
cutlen = txt1 - (txt1//2)
printABC = lower_case[:cutlen] + upper_case[cutlen:]
print(printABC) '''



#Write the same sentences above using Loops

'''txt = "Hello Jessica. Let's dine tonight."
d = txt.split()
r = len(d)

for g in range(r//2):
	print(d[g].upper(), end='')
s = r -r // 2
while s < r:
	print(d[s].lower(), end='')
	s+=1'''




