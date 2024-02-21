'''
request input from user for their name and name it "user_name1"
request input from user for their age and name it "user_age1"
request input from user for their house number and name it "user_house_num1"
request input from user for their street name and name it "user_street_name1"
use integer casting function to convert user_age1 and user_house_num1 into a string and print a sentece including all the requested input from user
'''
user_name1 = input("Please enter your name: ")
user_age1 = int(input("Please enter your age: "))
user_house_num1 = int(input("Please enter your house number: "))
user_street_name1 = input("Please enter your street name: ")
print("This is " + user_name1 + ". They are " + str(user_age1) + " years old and live at house number " + str(user_house_num1) + " on " + user_street_name1 + ".")
