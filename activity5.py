print("")
print("FARENHEIT TO CELCIUS CONVERTER")

print("==============================")

farenheit = eval(input("Please input the temperature in farenheit-->"))
celcius = ((farenheit - 32) * 5 ) / 9 #formula

print(f"{farenheit} degrees farenheit converted to celcius is {round(celcius,2)} degrees") 