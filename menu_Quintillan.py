def activity1(): 
      print("""
      This code uses 'print' to create a diamond shape
      
      code:
      print("\ t\ t       * \ n\ t\ t     *  
       *\ n\ t\ t   *   *   *\ n \ t       *   *
         *   *   *\ n\ t\ t   *   *   *\ n\ t\ t     
         *   *\ n\ t\ t       * ")
      """)

def activity3():
      print("""
      This program uses 'variable' to create question and will then be compiled later
      code:
      name = input("Please input your name:")
      gender = input("Please input your gender:")
      address = input("Please input your address:")
      telephone = input("Please input your telephone number:")
      cellphone = input("Please input your cellphone number:")
      birthday = input("Please input your birthday:")
      civil_status = input("Please input your civil status:")
      birth_place = input("Please input your birth place:")
      citizenship = input("Please input your citizenship:")
      height = input("Please input your height:")
      weight = input("Please input your weight:")
      religion = input("Please input your religion:")
      occupation = input("Please input your occupation:")
      language = input("Please input languages that you speak:")

      elementary = input("Please input your school in Elementary:")
      elemgrad = input("When did you graduate?:")
      high_school = input("Please input your school in High School:")
      hsgrad = input("When did you graduate?:")
      college = input("Please your school in College:")
      collegegrad = input("When did you graduate?:")
      degree = input("Please input the degree/s you achieved:")
      company = input("Please input your company name:")
      position = input("Please input your position:")
      companyfrom = input("When did you start:")
      companyto = input("When did you leave:")

      charrefname = input("Please input the name of your characther reference:")
      charcompany = input("Please input his/her company:")
      charposition = input("Please input his/her position:")
      charcontact = input("Please input his/her number:")

      print("")
      print("\ t\ t\ t\ t\ t\ t-----BIODATA-----")
      print(" ")
      print("PERSONAL INFORMATION")
      print("")
      print("Name: "+name)
      print("Gender: "+gender)
      print("Address: "+address)
      print("Telephone number: "+telephone)
      print("Cellphone: "+cellphone)
      print("Birthday: "+birthday)
      print("Civil Status: "+civil_status)
      print("Place of Birth: "+birth_place)
      print("Citizenship: "+citizenship)
      print("Height: "+height)
      print("Weight: "+weight)
      print("Religion: "+religion)
      print("Occupation: "+occupation)
      print("Languages or dialect spoken or written: " +language)

      print("")
      print("EDUCATIONAL BACKGROUND")
      print("")
      print("Elementary: "+elementary)
      print("Year graduated: "+elemgrad)
      print("")
      print("High School: "+high_school)
      print("Year graduated: "+hsgrad)
      print("")
      print("College: "+college)
      print("Year graduated: "+collegegrad)
      print("Degree achieved: "+degree)

      print("")
      print("EMPLOYMENT RECORD")
      print("")
      print("Company: "+company)
      print("Position: "+position)
      print("From: "+companyfrom)
      print("To: "+companyto)

      print("")
      print("CHARACTHER REFERENCE")
      print("")
      print("Name: "+charrefname)
      print("Company: "+charcompany)
      print("Position: "+charposition)
      print("Number: "+charcontact)
      """)

def code_challenge2():
      
     print(""" 
     print("      *   \n    * * *    \n  * * * * *     \n* Hi, Rica  *\n  * * * * *   \n    * * *   \n      *	")
     """)

def activity4():
      print("""
      This program uses 'variable' with 'operators' to execute it's task

      code:
      number1 = eval(input("Please input a number-->"))
      number2 = eval(input("Please input a number-->"))

      answer = number1 + number2

      print("The sum of" ,number1, "+" ,number2, "is",answer)
      """)

def code_challenge5():
      print("""
      This code converts Celcius to Farentheit
      
      code:
      print("")
      print("FARENHEIT TO CELCIUS CONVERTER")
      print("==============================")

      farenheit = eval(input("Please input the temperature in farenheit-->"))
      celcius = ((farenheit - 32) * 5 ) / 9 #formula

      print(f"{farenheit} degrees farenheit converted to celcius is {round(celcius,2)} degrees") 
      
      """)
            
def activity6():
      print("""
      This program will store the first number then it will be added with next number
            
      code:
            x = 5

            print("")

            print(x)

            x += 5

            print(x)

            x += 10

            print(x)

            x += 15

            print(x)

            x += 20

            print(x)

            x += 25

            print(x)

            x += 30

            print(x)

            x += 35

            print(x)

            x += 40

            print(x)

            x += 45

            print(x)

            x += 50

            print(x)

            x += 55

            print(x)

      """)
      
def code_challenge4():
      print("""
      This program will ask for 2 numbers that will be used for different operations
            
      code:
      number1 = eval(input("Please input the first number -->"))
      number2 = eval(input("Please input the second number -->"))

      sum = number1 + number2
      difference = number1 - number2
      product = number1 * number2
      qoutient = number1 / number2
      exponent = number1 ** number2
      remainder = number1 % number2
      floor_division = number1 // number2


      print("")
      print("Result:")
      print("")
      print("The sum of",number1,"+",number2,"is = ",sum)
      print("")
      print("The difference of",number1,"and",number2,"is = ",difference)
      print("")
      print("The product of",number1,"and",number2,"is = ",product)
      print("")
      print("The qoutient of",number1,"and",number2,"is = ",qoutient)
      print("")
      print(number1,"exponent by",number2,"is = ",exponent)
      print("")
      print("The remainder of",number1,"and",number2,"is = ",remainder)
      print("")
      print("The floor division of",number1,"and",number2,"is = ",floor_division)

      """)
      
def activity7():
      print("""
      This program adds 1 count to gold if the mineral is gold
            
      code:
      gold =  0
      miner = input("Please input your name: ")

      isGold = input("Is the mineral gold? ") 

      if isGold.lower() == "yes":
            gold +=1
            print(f"Hi! {miner}, Your total number of gold is {gold}")
      else:
            print(f"Hi! {miner}, Your total number of gold is {gold}")
            """)
            
def activity8():
      print("""
      This program will let the user access the sytem if the password is correct
            
      code:
      password = input("Please input your password--->")

      if password.lower() == "Jewel06":
            print("Access Granted, Please continue using the system.")
            print("	-----System exit-----")
      elif password.lower() == "Cayrey":
            print("Access Granted, Please continue using the system.")
            print("	-----System exit-----")
      elif password.lower() == "102504":
            print("Access Granted, Please continue using the system.")
            print("	-----System exit-----")
      elif password.lower() == "password":
            print("Access Granted, Please continue using the system.")
            print("	-----System exit-----")

      else:
            print("Wrong password, Please try again.")
            print("	-----System exit-----")
            """)
            
def activity9():
      print("""
      This program will evaluate your Age based on what you will input
            
      code:
            age = eval(input("Please input your age: "))

            if age <= 7:
                  print("=======")
                  print("Toddler")

            if age >=8 and age <=13:
                  print("=======")
                  print("Pre teen")

            if age >=14 and age <=18:
                  print("=======")
                  print("Teenager")

            if age >=19 and age <=31:
                  print("=======")
                  print("Early adulthood")

            if age >=32 and age <=45:
                  print("=======")
                  print("Mid adulthood")

            if age >=46 and age <=59:
                  print("=======")
                  print("Post adulthood")

            if age >=60:
                  print("=======")
                  print("Senior")

      """)
      
def activity10():
      print("""
      This program evaluates your Student Status
            
      code:
            name = input("Please input your name: ")
            isStudent = input("Are your currently enrolled in DLL?: (yes / no): ")

            if isStudent.lower() == "yes":
                  yearlevel = input("What year level are you in?\ n\ nF - Freshmen\ nS -
                  Sophomore\ nJ - Junior\ nR - Senior\ n\ nPlease input your answer: ")

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
      """)
      
def code_challenge6():
      print("""
      This program computes your final grade
      
      code:            
      print("\nFINAL GRADE COMPUTATION")
      
      name = input("STUDENT'S FULL NAME: ")
      
      prelim = float(input("Enter your prelim grade: "))
	  midterm = float(input("Enter your midterm grade: "))
  	semifinals = float(input("Enter your semifinals grade: "))
  	finals = float(input("Enter your finals grade: "))
  	quiz = float(input("Enter your quiz grade: "))
  	project = float(input("Enter your project grade: "))

  	if (65 <= prelim <= 100) and (65 <= 			midterm <= 100) and (65 <= semifinals <= 100) and (65 <= finals <= 100) and (65 <= quiz <= 100) and (65 <= project <= 100):
  	final_grade = (prelim * 0.15) + (midterm * 0.15) + (semifinals * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.25)
  	if final_grade >= 75:
  		print("You nailed it, you have passed the exam!")
  	else:
  		print("Apologies, you have failed the exam.")
  		""")
  		      
def code_challenge7():
      print("""
      This program helps you with your grocery

      code:
      print("\nGROCERIES APP")
      
      name = input("Name of the item: ")
	price = float(input("Price of the item: "))
	amount_paid = float(input("Amount paid: ")) 
	customer_age = int(input("Enter customer age: "))

	discount_percentage = 0.123
	discount_amount = price * 				discount_percentage
	
	if 61 <= customer_age <= 150:
		senior_discount_percentage = 0.052
		senior_discount_amount = total_price* senior_discount_percentage
		discount_amount = senior_discount_amount
		print(f"Senior Discount: {senior_discount_percentage:.2f}% ({senior_discount_amount:.2f} php)")
	
	total_price = price + discount_amount
	
	change = amount_paid - total_price

	print(f"Hi, you purchased a {name}.")
	print(f"Price: {price:.2f} php")
	print(f"Discount: {discount_percentage:.2f}% ({discount_amount:.2f} php)")
	print(f"Total: {total_price:.2f} php")
	print(f"Amount Paid: {amount_paid:.2f} php")
	print(f"Change: {change:.2f} php")
	
	""")

def activity11():
      print("""
      This program will loop a certain code for a given amount of iteration
      
      code:            
       for x in range(1, 25):
       	print("God is good")
	   	print("All the time")
      """)

def activity12_help():
      print("""
      This program counts from 1 to 10
      
      code:
            for x in range(10, 0, -1):
            print(x)

      """)
      
def activity13():
      print("""
      This program solves the factorial of a number for you
      
      code:
      
      num = eval(input(f"Enter a number: "))
      factorial = 1

      for x in range(num, 0, -1):
      factorial *= x
      print(f"The factorial of {num} is {factorial}")
      
      """)  

def activity14():
      print("""
      This program will count to 10 with a line of *
            
      code:
      for x in range(0,11):
            print(x, end =" ")
            for y in range(0,11):
                  print("*", end =" ")
            print()
      """)
      
def activity15():
      print("""
      This program runs an acute triangle
      
      code:

      for x in range(0, 11,):
            print(x, end =" ")
            for y in range(0,x):
                  print("*", end =" ")
            print()
      """)
      
def activity17():
      print("""
      This program creates a multiplication table based on 
      the number of columns
      
      code:
      column = eval(input("Enter number of columns: "))
      for x in range(1,11):
      for y in range(1, column+1):
            print(f"{x} x {y} = {x * y}", end="\t")
      print()
      """)
      
def activity18():
      print("""
      This program generates a number of triangle
      based on the amount given
      
      code:
      nt = eval(input("Enter number of triangles: "))
      for x in range(1,5):
      for r in range(1, nt+1):
            for y in range(1, x+1):
                  print("*", end=" ")
            for z in range(5, x, -1):
                  print(" ", end=" ")
            print(end=" ")
      print()
      """)

def code_challenge8():
      print("""
      This program asks for 10 numbers and will
      display the summation of all numbers
            
      code:
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
	""")
	
def code_challenge9():
      print("""
      This program inversed version of acute triangle
      
      code:
      		for x in range(1, 6): 
		for z in range(1, x+1):
			print(" ", end= " ") 
		for y in range(6, x, -1): 
			print("*", end= " ")
		print()
		""")		
		
def code_challenge10():
      print("""
      This program generates a diamond
      
      code:
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
	""")
	
def code_challenge12():
      print("""
      This program creates an arrow sign
            
      code:
      	for x in range (6, 0, -1):
		for z in range(1, x+1):
			print(" ", end= " ")
		for y in range(6, x, -1):
			print("*", end= " ")
		for a in range(6, x, -1):
			print("*", end=" ")
		print() 
	
	for x in range (1, 6): 
		for z in range(1, 6): 
			print(" ", end= " ") 
		for y in range (1, 3): 
			print("*", end=" ") 
		print()
		""")
		
def code_challenge13():
      print("""
      This program creates diamond but using nummbers
      
      code:
      	for x in range (1, 6): 
		for y in range(6, x, -1): 
			print(" ", end=" ") 
		for z in range(x, 1, -1): 
			print (z, end=" ") 
		for a in range(1, x+1): 
			print(a, end=" ") 
		print ()
		
	for x in range(5, 0, -1):
		for y in range(6, x, -1):
			print(" ", end=" ")
		for z in range(x, 1, -1):
			print(z, end=" ")
		for a in range(1, x+1):
			print(a, end=" ")
		print()
		""")
		
def activity19():
      print("""
      This program will continue to ask for name until the user 
            ends the program
      
      code:
      isContinue = True 

      while isContinue == True:
      name = input("Give me a name ---> ")

      if name.lower() == "stop":
            print("Loop Terminated")
            break
            isContinue == False 
      else:
            print(f"Hi, {name}")
      continue
      """)
      
def activity20():
      print("""
      Thisi program creates a triangle until
            the  user ends it

      code:
      isContinue = True 

      nt = 0
      while isContinue == True:
      ask = input("Gusto mo bang gumawa ng isa pang triangle (oo/hindi)")

      if ask.lower() == "stop":
            print("Program terminated")
            break
            isContinue == False 
      
      else:
            nt += 1
            for a in range(1,6):
                  for d in range(1,nt+1):
                  for b in range(1,a+1):
                        print("*",end=" ")
                  for c in range(6,a,-1):
                        print(" ",end=" ")
                  print(end=" ")
                  print()
            continue    
            
      """)
      
def code_challenge14():
      print("""
      This program will ask for a number and 
            will only stop if the user inputs 0

      code:
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
		 
		 """)
		 
def code_challenge15():
      print("""
      This program creates triangle until the user
            stops it

      code:
      	tuloy = True
	no = 0
	while tuloy:
		ask = input("Do you wish to create a new triangle (yes/no) ")
		
		if ask.lower() == "no":
		  	print("program / loop terminated")
		  	break
		elif ask.lower() == "yes":
		  	no += 1
		  	for x in range(1,6):
		  	       	   	for r in range(1, no+1):
		  	       	   		for y in range(1,x+1):
		  	       	   			print("^",end =" ")
		  	       	   		for z in range(6,x,-1):
		  	       	   			print(" ",end=" ")
		  	       	   		print()
		  	       	   	continue
		else:
		  	print("Invalid answer, please only answer 'yes' or ' no' ")
		  	continue
		  	
		""")
		
def activity25():
      print("""
      This program creates a list of fruits
      
      code:      
      fruits = ["apples","oranges","star-apple","guyabano","sour soup"]
      print(fruits)

      print(f"My favorite fruit growing up is {fruits[2]}")
      fruits.append("Longgan")
      print(fruits)
      fruits.insert(3,"banana")
      print(fruits)                       
      """)
      
def activity22():
      print("""
      This program is a mini menu
            
      code:
      def panghello():
      print("HELLO IT1A")

      def activity2():
            num1 = eval(input("Please enter a number: "))
            num2 = eval(input("Please enter another number: "))
            print(num1, "Floor divided to ",num2, "=",num1 // num2)

      isContinue = True
      while isContinue:
            print("SELECT FROM THE FOLLOWING CODE \n1 = PANGHELLO 
            \n2 = DIVISION PROGRAM\n3 = EXIT")

            ask = input("Which program would you like to run, 
            select from the option above: ")

            if ask == "1":
                  panghello()
                  continue
            elif ask == "2":
                  activity2()

            elif ask == "3":
                  print("PROGRAM TERMINATED")
                  break

            else:
                  print("Invalid Choice")
                  continue
      """)
      
def activity23():
      print("""
      This program implements the help() code
      def factorial(number):
            This function's purpose is to compute / calculate the factorial of any number 
            fact = 1 
            for x in range(number,0,-1):
                  fact *= x
                  return fact

      print(f"The factorial of 13 is {factorial(13)}")
      help(factorial)
      help(print)
      """)
      
def code_challenge16():
      print("""
      This program is a mini bank program
      
      code:
      	balance = 0
access = False
transaction = True

def denomination():
        one_th = balance // 1000
        one_th_change = balance % 1000
        print(f"1000 \t=\t {one_th}")
        fiveh = one_th_change // 500
        fiveh_change = one_th_change % 500  
        print(f"500 \t=\t {fiveh}")
        twoh = fiveh_change // 200
        twoh_change = fiveh_change % 200
        print(f"200 \t=\t {twoh}")
        oneh = twoh_change // 100
        oneh_change = twoh_change % 100
        print(f"100 \t=\t {oneh}")
        fifty = oneh_change // 50
        fify_change = oneh_change % 50
        print(f"50 \t=\t {fifty}")
        twenty = fify_change// 20
        twenty_change = fify_change % 20
        print(f"20 \t=\t {twenty}")
        ten = twenty_change // 10
        ten_change = twenty_change % 10
        print(f"10 \t=\t {ten}")
        five = ten_change // 5
        five_change = ten_change % 5
        print(f"5 \t=\t {five}")
        one = five_change // 1
        one_change = five_change % 1
        print(f"1 \t=\t {one}")
        
def balance_inquiry():
        print(f"\nYour balance across all account is ₱{balance}")
        print("Here is the denomination: \n")
        denomination()

def deposit():
        amount = eval(input("Enter an amount to be deposited: "))
        if amount < 0:
            print("That's not a valid amount")
            return 0
        else:
            print(f"You have successfully deposited an amount worth ₱{amount}, to see total balance and denomination, check balance inquiry.")
            return amount
            
def withdraw():
        amount = eval(input("Enter amount to be withdrawn: "))
        if amount > balance:
            print("Insufficient funds")
            return 0
        elif amount < 0:
            print("Amount must be greater than 0")
            return 0
        else:
            print(f"You have successfully withdrawn an amount worth ₱{amount}, to see total balance and denomination, check balance inquiry.")
            return amount
            
def account():
        create = input("Welcome to Bank A, Would you like to create an account? (yes / no) ")
        if create.lower() == "yes":
            bank_name = input("Enter your name: ")
            print(f"Good to see you here {bank_name}!, You may now access the bank features")
        else: 
            print("Thank you for visiting!")
            access = False
            
def open_account():
        another = input("Would you like to open another account? (yes / no) ")
        if another == "yes":
            name = input("Please enter the name of your account: ")
            print(f"Good to see you here {name}!, You may now access the bank features")
        else:
            return
            
        while transaction:
        	print("\n===== Welcome to Bank A! =====\n")
        	
        	print("0.Create Account")
        	print("1.Open another account")
        	print("2.Show Balance")
        	print("3.Deposit")
        	print("4.Withdraw")
        	print("5.Exit")
        print("\n===============================\n")
        choice = input("Enter your choice (0-5): ")
        
        if choice =="0":
            account()
            access = True
        elif choice == "1":
            if access == False:
                print("Please create an account first")
            else:
                open_account()
        elif choice == '2':
            if access == False:
                print("\nPlease create an account first")
            else:
                print("You are accessing the balance inquiry feature.")
                balance_inquiry()
        elif choice == '3':
            if access == False:
                print("\nPlease create an account first")
            else:
                print("You are accessing the deposit feature.")
                balance += deposit()
        elif choice == '4':
            if access == False:
                print("\nPlease create an account first")
            else:
                print("You are accessing the withdraw feature.")
                balance -= withdraw()
                
        elif choice == '5':
            transaction = False
        else:
            print("\nThat is not a valid choice")
            
        print("\nThank you! Have a nice day!")
        """)
        
def start():
      print("--- PYTHON PROGRAM MENU  ---")
      user = input("To access the program, Please enter your name: ")
      print(f"Hello {user}, You may now access the program")
      main_menu()

def display_menu():
      print(f""" 
      ======================================================
                              MENU 
         1 - print statements                              
         2 - variables                                     
         3 - operators                                     
         4 - conditional statements                        
         5 - loops                                        
         6 - lists                                         
         7 - functions                                     
         8 - exit                                  
      ======================================================   
      """)
      


def print_statements_option1():
      print()
      activity1()
      return print_statements_menu()

def print_statements_option2():
      return main_menu()

def print_statements_menu():
      print("\nACCESSING PRINT STATEMENTS MENU")
      print(""""
      HOW DOES PRINT WORK?
      The Python print() function takes in any number of parameters, and prints them out on one line of text. The items are each converted to text form, separated by spaces, and there is a single '\n' at the end (the "newline" char).
      You can pass variables, strings, numbers, or other data types as one or more parameters when using the print() function.
      Then, these parameters are represented as strings by their respective str() functions. To create a single output string, the transformed strings are concatenated with spaces between them""")
      print("\nPython print() function prints the message to the screen or any other standard output device.")
      print("\nChoose from options below:")
      print("1. Sample program")
      print("2. Return")
      print_choice = input("Enter your choice: ")
      print_choice_option(print_choice)
      return 

def print_choice_option(print_choice):
      if print_choice == "1":
            print_statements_option1()
      if print_choice == "2":
            print_statements_option2()
      else:
            print("Invalid Choice")

def main_menu():
      isContinue = True
      while isContinue:
            display_menu()
            choice = input("Enter your choice: ")     
            if choice == '1':
                  print("You chose option 1: Print statements.")
                  print_statements_menu()
            if choice == '2':
                  print("You chose option 2: Variables.")
                  variables_menu()
            if choice == '3':
                  print("You chose option 3: Operators.")
                  operators_menu()
            if choice == '4':
                  print("You chose option 4: Conditional statements.")
                  conditionalstatements_menu()
            if choice == '5':
                  print("You chose option 5: Loops.")
                  loops_menu()
            if choice == '6':
                  print("You chose option 6: Lists.")
                  lists_menu()
            if choice == '7':
                  print("You chose option 7: Functions.")
                  function_menu()
            if choice == "8":
                  print("Program Terminated, You may now close it. ")
                  sys.exit()
            else:
                  print("Invalid choice. Please try again.")
        
        
def variables_menu():
      print("""\nACCESSING VARIBLES MENU
      HOW DOES VARIABLES WORK?
      
      In Python, variables are names associated with concrete objects or values stored in your computer's memory.
      By associating a variable with a value, you can refer to the value using a descriptive name and reuse it as many times as needed in your code. Variables behave as if they were the value they refer to.
      Variables are containers for storing data values.
      Choose from the options below:
            
      1. Sample Programs
      2. Return
      """)
      variable_choice = input("Enter your choice: ")
      variables_option(variable_choice)
      return 
      
def  variables_option(variable_choice):
      if variable_choice == "1":
            variable_choice_option1()
      if variable_choice == "2":
            main_menu()

def variable_choice_option1():
      print("You're accessing the sample programs using variable.")
      print("Choose from the option below")
      print("""
      1. Bio - data
      2. Putting a name on the center of a diamond
      3. Return
      """)
      variable_sampleprogramchoice = input("Enter your choice: ")
      variable_sampleprogram(variable_sampleprogramchoice)
      return variable_sampleprogramchoice

def variable_choice_option2():
      variables_menu()
def variable_sampleprogram(variable_sampleprogramchoice):
      if variable_sampleprogramchoice == "1":
            activity3()
            return variable_choice_option1()
      if variable_sampleprogramchoice == "2":
            code_challenge2()
            return variable_choice_option1()
      else:
            print("Invalid Choice")

def operators_menu():
      print("""
      ACCESSING OPERATORS MENU
      
      Python operators are special symbols or keywords used to perform operations on variables and values. 
      These operators allow for various functionalities, from basic arithmetic operations like addition, subtraction, multiplication, and division to more complex comparisons and logical operations.
      Operators are used to perform operations on variables and values.
      Choose from the options below:
      	
      1. Sample programs
      2. Return
      """)
      operators_choice = input("Enter your choice: ")
      operators_choice_options(operators_choice)
      return

def operators_choice_options(operators_choice):
      if operators_choice == "1":
            operators_choice_option1()
      elif operators_choice == "2":
            return main_menu()
      else:
            print("Invalid choice")


def operators_choice_option1():
      print("\nYou're accessing the sample programs using operators on python")
      print("Choose from the option below")
      print("""
      1. Adding two numbers
      2. Temperature Converter
      3. Multiplication table using addition assignment operator
      4. Two numbers in all operators 
      5. Return
      """)
      operators_sampleprogramchoice = input("Enter your Choice: ")
      operators_sampleprogram(operators_sampleprogramchoice)
      return operators_sampleprogramchoice

def operators_sampleprogram(operators_sampleprogramchoice):
      if operators_sampleprogramchoice == "1":
            activity4()
            operators_choice_option1()
      elif operators_sampleprogramchoice == "2":
            code_challenge5()
            operators_choice_option1()
      elif operators_sampleprogramchoice == "3":
            activity6()
            operators_choice_option1()
      elif operators_sampleprogramchoice == "4":
            code_challenge4()
            operators_choice_option1()
      elif operators_sampleprogramchoice == "5":
            operators_menu()
      else:
            print("Invalid Choice")

def conditionalstatements_menu():
      print("""
      In Python, conditional statements allow you to execute different blocks of code based on certain conditions. 
      The most common types of conditional statements are if, elif (else if), and else. 
      These statements enable decision-making in your program.
      Conditional statements in Python are used to execute certain blocks of code based on specific conditions. 
      These statements help control the flow of a program, making it behave differently in different situations.
      
      1. Sample programs
      2. Return
      """)
      conditionalstatements_choice = input("Enter your choice:")
      conditionalstatements_option(conditionalstatements_choice)
      return conditionalstatements_choice
      
def conditionalstatements_option(conditionalstatements_choice):
      if conditionalstatements_choice == "1":
            conditionalstatements_option1()
      elif conditionalstatements_choice == "2":
            main_menu()


def conditionalstatements_option1():
      print("""
      You're accessing the conditional statements sample programs
      Choose from the option below:
            
      1. Gold program
      2. Password program
      3. Stage of life program
      4. DLL student status
      5. Final Grade computation
      6. Groceries program
      7. Return
      """)
      conditionalstatements_option1_choice = input("Enter your Choice: ")
      conditionalstatements_sampleprogram(conditionalstatements_option1_choice)
      return conditionalstatements_option1_choice

def conditionalstatements_sampleprogram( conditionalstatements_option1_choice):
      if  conditionalstatements_option1_choice == "1":
            activity7()
            conditionalstatements_option1()
      elif  conditionalstatements_option1_choice == "2":
            activity8()
            conditionalstatements_option1()
      elif  conditionalstatements_option1_choice == "3":
            activity9()
            conditionalstatements_option1()
      elif  conditionalstatements_option1_choice == "4":
            activity10()
            conditionalstatements_option1()
      elif  conditionalstatements_option1_choice == "5":
            code_challenge6()
            conditionalstatements_option1()
      elif  conditionalstatements_option1_choice == "6":               
            code_challenge7()
            conditionalstatements_option1()
      elif  conditionalstatements_option1_choice == "7":
            conditionalstatements_menu()
      else:
            print("Invalid Choice")

def loops_menu():
      print("""
      ACCESSING MENU FOR LOOPS
      
       Python loops are fundamental constructs that allow you to execute a block of code repeatedly. 
      There are primarily two types of loops in Python: for loops and while loops. 
      Each serves different purposes and is used based on the specific requirements of your program.
      
      For Loops
      Definition: A for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in that sequence.
            
      While Loops
      Definition: A while loop continues to execute as long as a specified condition is true.
      A for loop is a control flow statement for specifying iteration, which allows code to be executed repeatedly. 
      A for loop has two parts: a header specifying the iteration, and a body which is executed once per iteration.
      Choose from the options below:
            
      1. Sample programs
      2. Return
      """)
      loops_menu_choice = input("Enter your choice: ")
      loops_choice_option(loops_menu_choice)
      return

def loops_choice_option(loops_menu_choice):
      if loops_menu_choice == "1":
           loops_choice_option1()
      elif loops_menu_choice == "2":
            main_menu()
      else:
            print("Invalid Choice")
            

def loops_choice_option1():
      print("""
      You're accessing sample programs using loops.
      Choose from the option below:
            
      1. For loops
      2. While loops
      3. Return
      """)
      loops_choice_option1_choice = input("Enter your choice: ")
      loops_sampleprograms(loops_choice_option1_choice)
      return loops_choice_option1_choice

def  loops_sampleprograms(loops_choice_option1_choice):
      if loops_choice_option1_choice == "1":
            for_loops()
      elif loops_choice_option1_choice == "2":
            while_loops()
      elif loops_choice_option1_choice == "3":
            loops_menu()
      else:
            print("Invalid Choice")

def for_loops(): 
      print("""
      You're accessing For loop sample programs
      Choose from the option below:
            
      1. Lyrics loop  
      2. Countdown
      3. Factorial using loop
      4. Countdown with *
      5. Right angle triangle program
      6. Multiplication table
      7. Triangle generator
      8. Input 10 numbers
      9. Inverted Triangle
      10. Diamond
      11. Diamond with tip
      12. Arrow
      13. Diamond but numbers
      14. Return
      """)
      for_loops_choice = input("Enter your choice: ")
      for_loops_menu(for_loops_choice)
      return for_loops_choice

def for_loops_menu(for_loops_choice):
      if for_loops_choice == "1":
            activity11()
            for_loops()
      elif for_loops_choice == "2":
            activity12()
            for_loops()
      elif for_loops_choice == "3":
            activity13()
            for_loops()
      elif for_loops_choice == "4":
            activity14()
            for_loops()
      elif for_loops_choice == "5":
            activity15()
            for_loops()
      elif for_loops_choice == "6":
            activity17()
            for_loops()
      elif for_loops_choice == "7":
            activity18()
            return for_loops()
      elif for_loops_choice == "8":
            code_challenge8()
            for_loops()
      elif for_loops_choice == "9":
            code_challenge9()
            for_loops()
      elif for_loops_choice == "10":
            code_challenge10()
            for_loops()
      elif for_loops_choice == "11":
            code_challenge11()
            for_loops()
      elif for_loops_choice == "12":
            code_challenge12()
            for_loops()
      elif for_loops_choice == "13":
            code_challenge13()
            for_loops()
      elif for_loops_choice == "14":
            loops_choice_option1()
      else:
            print("Invalid Choice")

def while_loops(): 
      print("""
      You're accessing While loop sample programs
       from the option below:
      1. Hello <name>
      2. Infinite triangle generator
      3. Input infinite number with summation at the end
      4. Infinite triangle
      5. Return
      """)
      while_loops_choice = input("Enter a number: ")
      while_loops_menu(while_loops_choice)
      return while_loops_choice

def  while_loops_menu(while_loops_choice):
      if while_loops_choice == "1":
            activity19()
            while_loops()
      elif while_loops_choice == "2":
            activity20()
            while_loops()
      elif while_loops_choice == "3":
            code_challenge14()
            while_loops()
      elif while_loops_choice == "4":
            code_challenge15()
            while_loops()
      elif while_loops_choice == "5":
            loops_choice_option1()
      else:
            print("Invalid Choice")

def lists_menu():
      print("""
      ACCESSING MENU FOR LISTS
      Lists are used to store multiple items in a single variable.
      List items are ordered, changeable, and allow duplicate values.
      List items are indexed, the first item has index [0], the second item has index [1] etc.
      Ordered
      When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
      If you add new items to a list, the new items will be placed at the end of the list.  
      Changeable
      The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
      A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ] .
      Choose from the options below:
      1. Sample programs
      2. Return 
      """)
      list_menu_choice = input("Enter your choice: ")
      lists_menu_option(list_menu_choice)
      return list_menu_choice

def lists_menu_option(list_menu_choice):
      if list_menu_choice == "1":
            list_option1()
      elif list_menu_choice == "2":
            main_menu()
      else:
            print("Invalid Choice")


def list_option1():
      print("""   
      You're accessing sample programs using loops 
      Choose from the option below:
            
      1. Fruits list
      2. Return
      """)
      list_option1_choice = input("Enter your choice: ")
      list_sampleprograms(list_option1_choice)
      return list_option1_choice

def list_sampleprograms(list_option1_choice):
      if list_option1_choice == "1":
            activity25()
            list_option1()
      elif list_option1_choice == "2":
            lists_menu()
      else:
            print("Invalid Choice")

def function_menu():
      print("""
      ACCESSING MENU FOR FUNCTIONS 
            Creating a Function
      In Python a function is defined using the def keyword:
            def my_function():
                   print("Hello from a function")
            
      Calling a Function
      To call a function, use the function name followed by parenthesis:
            def my_function():
                   print("Hello from a function")

            my_function()

      Arguments
      Information can be passed into functions as arguments.
      Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
      The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
            def my_function(fname):
                  print(fname + " Refsnes")

            my_function("Emil")
            my_function("Tobias")
            my_function("Linus")
            
      A function is a block of code which only runs when it is called.
      You can pass data, known as parameters, into a function.
      A function can return data as a result.
            
      Choose from the option below:
      1. Sample programs
      2. Return
      """)
      function_menu_choice = input("Enter your choice: ")
      function_menu_option(function_menu_choice)
      return function_menu_choice

def function_menu_option(function_menu_choice):
      if function_menu_choice == "1":
            function_option1()
      elif function_menu_choice == "2":
            main_menu()
      else:
            print("Invalid Choice")

def function_option1():
      print("""
      You're Accessing the sample programs using functions
      
      1. Simple menu
      2. Factorial
      3. Banking program
      4. Return
      """)
      f_option1_choice = input("Enter your choice: ")
      function_sampleprograms(f_option1_choice)
      return f_option1_choice

def function_sampleprograms(f_option1_choice):
      if f_option1_choice == "1":
            activity22()
            function_option1()
      elif f_option1_choice == "2":
            activity23()
            function_option1()
      elif f_option1_choice == "3":
            code_challenge16()
            function_option1()
      else:
            print("Invalid Choice")

print("FINAL PROJECT for ITCS102")
print("QUINTILLAN, RICA M. \nBSIT-2A")
strt = input("Would you like to access the program? (yes/no): ")
if strt.lower() == "yes":
      start()
elif strt.lower() == "no":
      print("Thank you for coming, You may now close the program. ")
      sys.exit()
else:
      print("Invalid choice, Please try again.")		