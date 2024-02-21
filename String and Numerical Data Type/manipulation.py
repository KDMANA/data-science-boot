'''
request a sentence from the user and assign the variable as "str_manip"
use the len function to calculate the length of "str_manip"
assign the last letter of the sentence to "last char"
print "last char"
replace "last_char" with "@" using the replace function
use indexing to find the first 3 letters and assign that to "first_3_letters"
use indexing to find the last 2 letters and assign that to "last_2_letters"
assign both "first_3_letters" and last_2_letters to "new_word1" 
print new_word1
'''

# Get a sentence from the user
str_manip = input("Please enter a sentence: ")

# Print the length of the sentence
print("Length of the sentence:", len(str_manip))

# Get the last character of the sentence
last_char = str_manip[-1]

# Print the last character
print("Last character of the sentence:", last_char)

# Replace the last character with '@' and print the modified sentence
modified_sentence = str_manip.replace(last_char, "@")
print("Modified sentence:", modified_sentence)

# Get the first 3 letters and last 2 letters of the sentence
first_3_letters = str_manip[:3]
last_2_letters = str_manip[-2:]

# Combine the first 3 letters and last 2 letters to create a new word
new_word = first_3_letters + last_2_letters
print("New word created:", new_word)