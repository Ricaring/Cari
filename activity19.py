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