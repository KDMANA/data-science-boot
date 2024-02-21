'''
Request user to assign a integer to "num1",
request user to assign a integer to "num2"
request user to assign a integer to "num3"
assign "sum1" to the sum of num1, num2 and num3
print sum1 by converting it with the integer casting function
print both calculations with the integer casting function
'''
# Get three integers from the user
num1 = input("Please enter the first integer: ")
num2 = input("Please enter the second integer: ")
num3 = input("Please enter the third integer: ")

# Calculate the sum of the three integers
sum1 = int(num1) + int(num2) + int(num3)

# Print the sum of the three integers
print("Sum of the three integers:", sum1)

# Print the result of subtracting the second integer from the first integer
print("Difference between the first and second integers:", int(num1) - int(num2))

# Print the result of multiplying the third integer by the first integer
print("Product of the third and first integers:", int(num3) * int(num1))

# Print the result of dividing the sum of the integers by the third integer
print("Division of the sum by the third integer:", int(sum1) / int(num3))
