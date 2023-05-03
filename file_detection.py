import os

# Check if a file location exists

path = "C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists")

else:
    print("That location doesn't exist")

# Check if a file is a file

if os.path.isfile(path):
    print("That is a file")

else:
    print("That is not a file")

# Check if a directory (folder) is a directory

folder = "C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\test folder"

if os.path.isdir(folder):
    print("This is a directory")

else:
    print("This is not a directory")

