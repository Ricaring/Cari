odd = 0 
even = 0 
sum = 0 
for i in range(10):
	i = eval(input(f"Enter a number {i+1}: ")) 
	if i %2 == 0: 
		odd += i 
	else: 
		even += i 
	sum += i
	
print(f"The sum of all Even number is:{sum}")