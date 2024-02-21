'''
ask user to input a string
assign the string as 'user_input' and use split()
create a for loop with if-else statements to alternate characters
use join() to join all altered characters to result_string
print the result 'result_string'
'''
# Ask the user to input a string
user_string = input("Please enter a word or a sentence: ")

# Assign alternate_string for the output list 
alternate_string = []
i = 0  # Set initial iteration to 0

# Iterate through each character in the input string
for char in user_string:
    # Append each character to alternate_string with alternating case
    if i % 2 == 0:
        alternate_string.append(char.lower())
    else:
        alternate_string.append(char.upper())

    i += 1

# Join the characters to form the result string
result_string = ''.join(alternate_string)

# Print the result
print(result_string)