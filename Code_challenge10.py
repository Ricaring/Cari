for x in range(1, 6): 
	for y in range(5, x, -1): 
		print(" ", end=" ") 
	for z in range(x, 1, -1): 
		print("*", end=" ") 
	for a in range(1, x+2): 
		print("*", end=" ") 
	print()