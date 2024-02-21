'''
create a list called 'menu' and [include 4 cafe items that are sold]
create a dictionary called 'stock'
the 'stock' includes the prices of the 4 cafe items
create a dictionary called 'price to include these prices on menu
assign the variable to equal the 'total_stock' in the cafe
use loop through dictionaries and lists
item_value = (stock[items] * price[items])
sum  all item values together
print the result of the calculation
'''

# Assign a list called 'menu' with 4 cafe items.
menu = ['coffee', 'cake', 'cappuccino', 'latte']

# Create a dictionary called 'stock' with stock of cafe items.
stock = {'coffee': 40, 'cake': 12, 'cappuccino': 30, 'latte': 35}

# Create a dictionary called 'price' with prices of cafe items.
price = {'coffee': 3.8, 'cake': 2.8, 'cappuccino': 3.3, 'latte': 3.6}

# Calculate total stock worth in cafe.
total_stock = sum(stock[item] * price[item] for item in menu)

# Print result with f-string.
print(f"The total stock value in the cafe is work £{total_stock: .2f}")
