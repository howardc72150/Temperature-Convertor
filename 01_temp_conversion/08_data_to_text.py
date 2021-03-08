import re

# Data to be outputted
data = ['I', 'love', 'computers']

# Get filename can't be blank or invalid.
# assume valid data for now.

has_errrors = True
while has_errrors == True:
    has_errrors = False
    filename = input("Enter a filename (don't include the extension): ")

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue
        elif letter == " ":
            problem = "(no spaces allowed)"
        else:
            problem = "(no {}'s allowed)".format(letter)
        
        has_errrors = True
    
    if filename == "":
        problem = "can't be blank"
        has_errrors = True
    
    if has_errrors == True:
        print("Invalid filename - {}".format(problem))
        print()
    else:
        print("You entered a valid filename")

# Add .txt extension
filename = filename + ".txt"

# Create file to hold data
f = open(filename, "w+")

# Add new line at end of each item
for item in data:
    f.write(item + "\n")

# Close file.
f.close()