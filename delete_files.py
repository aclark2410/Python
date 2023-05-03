import os
import shutil

path = "C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\test.txt"

directory = "C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\test folder\\test.txt"

# Delete file

try: 
    os.remove(path)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to delete that")

# Delete empty directory

try: 
    os.rmdir(directory)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to delete that")

except OSError:
    print("You cannot delete it using that function")


# Delete directory and all of its contents 

try:
    shutil.rmtree(directory)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to delete that")

except OSError:
    print("You cannot delete it using that function")
