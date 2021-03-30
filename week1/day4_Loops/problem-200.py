ini_tuple = (1, 2, 3, 4, 8, 12, 3, 34, 
             67, 45, 1, 1, 43, 65, 9, 10) 
  
# printing initial tuple 
print ("initial list", str(ini_tuple)) 
  
# code to group 
# tuple into size 4 tuples 
res = tuple(ini_tuple[x:x + 4]  
      for x in range(0, len(ini_tuple), 4)) 
  
# printing result 
print ("resultant tuples", str(res)) 