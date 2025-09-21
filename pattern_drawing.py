# pattern_drawing.py

# Prompt user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to control rows
while row < size:
    # Use for loop to print stars in each row
    for col in range(size):
        print("*", end="")  # print without new line
    print()  # move to next line after each row
    row += 1
