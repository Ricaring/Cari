for x in range(7, 0, -1): 
	for z in range(1, x+1): 
		print(" ", end= " ") 
	for y in range(7, x, -1): 
		print("*", end= " ")
	for a in range(6, x, -1): 
		print("*", end= " ")
	print()
	
for x in range (1, 7): 
	for z in range(1, x+2): 
		print(" ", end= " ")
	for y in range(6, x, -1): 
		print("*", end= " ") 
	for a in range(5, x, -1): 
		print("*", end= " ") 
	print()