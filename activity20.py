isContinue = True
	
nt = 0
while isContinue == True:
		ask = input("Gusto mo bang gumawa ng isa pang triangle (oo/hindi)")
		
		if ask.lower() == "hindi":
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