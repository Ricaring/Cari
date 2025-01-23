def factorial(number):
            fact = 1
            for x in range(number,0,-1):
                  fact *= x
                  return fact
                  
print(f"The factorial of 13 is {factorial(13)}")
help(factorial)
help(print)