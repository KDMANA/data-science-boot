'''
assign variable user_number where the user is asked to input a number
use while function to allow the program to run continuously
if function with break if the number is '-1' to stop requesting numbers from the user
remove -1 from list and calculate the average
print out the average
'''
# Create an empty list to store user-entered numbers
user_numbers = []
user_input = ()

# Store all input values until -1 is inputted.
while user_input != -1:
    user_input = int(input("Please enter a number (-1 to stop): "))
    user_numbers.append(user_input)

    if user_input == -1:
        break

# Remove -1 from list and calculate the average
user_numbers.pop()
print(user_numbers)

# Calculate the average
user_average = int(sum(user_numbers) / len(user_numbers))

# Display the numbers entered and the calculated average
print(f"The numbers entered: {user_numbers}")
print(f"The average of the numbers entered is {user_average:.2f}.")
