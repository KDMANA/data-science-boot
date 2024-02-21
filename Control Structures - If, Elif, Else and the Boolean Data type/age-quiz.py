'''
request input from the user for their age 
use the integer casting function to convert the variable "age"
using the if function to set the conditions 
use elif function to add additional conditions
use else function for an input if all these conditions are false
'''

# Get the user's age as an integer input
age = int(input("Please enter your age: "))

# Check different age ranges and conditions
if age >= 40:
    print("You're over the hill.")
elif age >= 101:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st birthday!")
else:
    print("Age is but a number.")
