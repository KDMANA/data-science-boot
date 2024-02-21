'''
assign variable "string1" with the given sentence
print "string1" using the replace function to replace "!" with a blank space
print "string1" using the upper function to capitalise sentence
print "string1" using negative indexing to reverse the sentence
'''
# Initial string
string1 = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replace '!' with a space
string1 = string1.replace("!", " ")
print("String after replacing '!':", string1)

# Print the string in uppercase
print("Uppercase version of the string:", string1.upper())

# Print the string in reverse
print("String in reverse:", string1[::-1])