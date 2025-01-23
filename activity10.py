name = input("Please input your name: ")
isStudent = input("Are your currently enrolled in DLL?: (yes / no): ")

if isStudent.lower() == "yes":
		yearlevel = input("What year level are you in?\n\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\n\nPlease input your answer: ")
		
		if yearlevel.lower() == "f":
			print(f"\nHi, {name}, Freshmen, Welcome to DLL")
			
		if yearlevel.lower() == "s":
			print(f"\nHi, {name}, Sophomore, Welcome back to DLL")
			
		if yearlevel.lower() == "j":
			print(f"\nHi, {name}, Junior, Welcome back to DLL")
			
		if yearlevel.lower() == "r":
			print(f"\nHi, {name}, Senior, Welcome back to DLL")

else:
		print("\nThank you for using the system, you may now close it.\n")