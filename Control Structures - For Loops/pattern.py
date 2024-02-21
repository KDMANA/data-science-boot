'''
Set the first iteration of the progran to "*" 
Use a for loop to print the remaining stars 9 rows by indexing 10
Use if-else statement to determine the number of stars
depending on if the pattern is increasing or decreasing
'''

stars = "*"  # Use a single asterisk as the first iteration

# Use the for loop to iterate 10 times
for i in range(0, 10):
    print(stars)  # Print the current value of stars
    
    # Use if-else to change star for the next iterations
    if i < 4:
        stars = stars + "*"
    else:
        stars = stars[:-1]
