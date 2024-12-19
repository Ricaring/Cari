print("FAHRENHEIT TO CELCIUS CONVERTER PROGRAM") 
print("=============") 

fahrenheit = eval(input("Enter temperature in Fahrenheit ---> ")) 

celcius = ((fahrenheit - 32) *5) /9 

print(fahrenheit, "degrees Fahrenheit converted to celcius is" , celcius, "degrees" )
print(f" {fahrenheit}degrees Fahrenheit converted to celcius is {celcius} degrees")
print(round(celcius, 2))
print(f" {fahrenheit}degrees Fahrenheit converted to celcius is {round(celcius, 2)} degrees")