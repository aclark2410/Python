# copyfile() = copies contents of a file

# copy() = copyfile() + permission mode + destination can be a directory

# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile("C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\test.txt", "C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\testCopy.txt") # arguments(src,destination)