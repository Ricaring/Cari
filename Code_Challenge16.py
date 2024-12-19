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