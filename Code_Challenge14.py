# continue to ask user for a number
# summation at the end of loop

con = True
sum = 0
while con == True:
	num = eval(input("Please enter a number --> (put 0 to stop) "))
	if num > 0:
	       sum += num
	       continue
        
	else:
	       print("\nLoop has stopped")
	       print(f"The summation of all the numbers you entered is {sum}")
	       break
	       con = False