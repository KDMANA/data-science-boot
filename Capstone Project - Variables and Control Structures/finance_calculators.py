'''
print the 'investment' definition 
print the 'bond' definition
ask user to input their chosen calculation either investment or bond
use '.lower()' function for case insensitivity
if function for calculation type and interest type
elif function to personalise selection for user
else function for error message for calculation and interest choice 
'''

import math

# User selection for investment or bond calculator (case-insensitive)
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# .lower() to convert user input to lowercase for case-insensitive comparison
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Investment calculator
if user_choice == "investment":
    principle = float(input("Enter the amount that you are depositing: "))
    rate = float(input("Enter the annual interest rate as a percentage (do not include symbols like %): ")) / 100
    time = int(input("Enter the number of years you are investing for: "))
    
    interest = input("Please enter 'simple' or 'compound' to choose the type of interest: ").lower()
    
    # Calculate simple interest for investment
    if interest == "simple":
        simple_interest = round(principle * (1 + rate * time), 2)
        print(f"The simple interest earned on the investment is £{simple_interest} after {time} years at a rate of {rate * 100}%.")

    # Calculate compound interest for investment
    elif interest == "compound":
        compound_interest = round(principle * math.pow((1 + rate), time), 2)
        print(f"The compound interest earned on the investment is £{compound_interest} after {time} years at a rate of {rate * 100}%.")

    else:
        print("Invalid entry! Please enter 'simple' or 'compound' and try again.")

# Bond calculator
elif user_choice == "bond":
    principle = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the annual interest rate as a decimal (do not include symbols like %): ")) / 100 / 12
    time = int(input("Enter the number of months it will take to repay the bond: "))

    # Calculate the monthly repayment amount on a home loan
    monthly_repayment = round((rate * principle) / (1 - rate) ** -time, 2)
    
    print(f"The monthly payment on your home loan will be £{monthly_repayment:.2f}.")

else:
    print("Invalid entry! Please enter 'investment' or 'bond' from the menu above to proceed.")
