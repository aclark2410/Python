import os

# Moving a file to another destination. It is possible to do the same for a direcrory (folder)

source = "C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\test.txt"

destination = "C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\test folder\\test.txt"

# First we check if the file is already present in our destination path
try:
    if os.path.exists(destination):
        print("This file already exists here")
    
    # If it is not already in our destination path we move the source path to the location passing in them as the two arguments
    else:
        os.replace(source,destination)
        print(source + " has been moved")


except FileNotFoundError:
    print("Source was not found")


