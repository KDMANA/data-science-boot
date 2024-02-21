'''
assign variables "swimming", "cycling" and "running" with user input
sum all variables to assign to the variable "triathlon"
print out the value of triathlon
use if function to set the conditions of the award
use elif for additional conditions for the award
use else function if all conditions are not true for no award
'''
# Get the time taken for swimming from the user
swimming = input("Please enter the time taken to complete swimming (minutes): ")

# Display a message about the completed swimming event
print("You have completed the swimming event in " + str(swimming) + " minutes.")

# Get the time taken for cycling from the user
cycling = input("Please enter the time taken to complete cycling (minutes): ")

# Display a message about the completed cycling event
print("You have completed the cycling event in " + str(cycling) + " minutes.")

# Get the time taken for running from the user
running = input("Please enter the time taken to complete running (minutes): ")

# Display a message about the completed running event
print("You have completed the running event in " + str(running) + " minutes.")

# Calculate the total time taken for the triathlon
triathlon = int(swimming) + int(cycling) + int(running)

# Display the total time taken for the triathlon
print("The total time taken to complete the triathlon is " + str(triathlon) + " minutes.")

# Check the total time and provide awards based on specific ranges
if triathlon <= 100:
    print("Congratulations, you are awarded the Provincial Colours!")
elif 101 <= triathlon <= 105:
    print("Congratulations, you are awarded the Provincial Half Colours!")
elif 106 <= triathlon <= 110:
    print("Congratulations, you are awarded the Provincial Scroll!")
else:
    print("Sorry, you have not qualified for an award.")
