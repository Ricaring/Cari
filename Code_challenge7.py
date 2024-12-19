name = input("Name of the item: ")
price = float(input("Price of the item: "))
amount_paid = float(input("Amount paid: ")) 
customer_age = int(input("Enter customer age: "))

# Calculate the discount 
discount_percentage = 0.123
discount_amount = price * discount_percentage

# Calculate senior discount if applicable
if 61 <= customer_age <= 150:
	senior_discount_percentage = 0.052
	senior_discount_amount = total_price* senior_discount_percentage
	discount_amount += senior_discount_amount
	print(f"Senior Discount: {senior_discount_percentage:.2f}% ({senior_discount_amount:.2f} php)")
	
# Calculate the total price 
total_price = price + discount_amount

# Calculate the change 
change = amount_paid - total_price

# Receipt
print(f"Hi, you purchased a {name}.")
print(f"Price: {price:.2f} php")
print(f"Discount: {discount_percentage:.2f}% ({discount_amount:.2f} php)")
print(f"Total: {total_price:.2f} php")
print(f"Amount Paid: {amount_paid:.2f} php")
print(f"Change: {change:.2f} php")