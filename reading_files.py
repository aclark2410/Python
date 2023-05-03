# How to read files 

# This block of code will open and read the contents of a file and then close it

with open("C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\test.txt") as file:
    print(file.read())

# If the user enters a wrong file location we can use exception handling

try:
    with open("C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\test.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("That file was not found")
    
