gold =  0
miner = input("Please input your name: ")

isGold = input("Is the mineral gold? ")

if isGold.lower() == "yes":
	       gold +=1
	       print(f"Hi! {miner}, Your total number of gold is {gold}")
else:
	print(f"Hi! {miner}, Your total number of gold is {gold}")