def panghello():
      print("HELLO IT1A")

      def activity2():
            num1 = eval(input("Please enter a number: "))
            num2 = eval(input("Please enter another number: "))
            print(num1, "Floor divided to ",num2, "=",num1 // num2)

      isContinue = True
      while isContinue:
            print("SELECT FROM THE FOLLOWING CODE \n1 = PANGHELLO \n2 = DIVISION PROGRAM\n3 = EXIT")
           
            ask = input("Which program would you like to run, select from the option above: ")

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