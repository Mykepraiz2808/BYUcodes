"""
Welcome to the Meal Price Calculator!
This program helps you calculate the total cost of a meal, including sales tax,
and determines the change based on the payment provided.
"""

# Prompt user for meal prices
child_meal_price = float(input("What is the price of a child's meal? $"))
adult_meal_price = float(input("What is the price of an adult's meal? $"))


# Prompt user for quantity of people
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

# Compute and display the subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
print(f"Subtotal: ${subtotal:.2f}")

# Ask for the sales tax rate
sales_tax_rate = float(input("What is the sales tax rate? (as a percentage): "))

# Compute and display the sales tax
sales_tax = (subtotal * sales_tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")

# Compute and display the total price
total_cost = subtotal + sales_tax
print(f"Total Cost: ${total_cost:.2f}")

# Ask for the payment amount
payment_amount = float(input("What is the payment amount? $"))

# Compute and display the change
change = payment_amount - total_cost
print(f"Change: ${change:.2f}")