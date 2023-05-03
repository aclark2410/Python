# How to write files

text = "Yooo\nThis is some text\nhave a good one!"

# Using 'w' after the file location we choose write mode that will overwrite the existing text in a file

with open("C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\test.txt", 'w') as file:
    file.write(text)

new_text = "see ya!"

# Using 'a' after the file location we choose to append new text on to the existing text in a file.

with open("C:\\Users\\AndrewClark\\OneDrive - Invenics Ltd\\Desktop\\test.txt", 'a') as file:
    file.write(new_text)