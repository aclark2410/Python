# str.format() = optional method that gives users 
#                more control when displaying output

animal = "cow"
item = "moon"

# A basic string containing variables

print("The " + animal + " jumped over the " + item)

# Can be re-written using placeholders and .format([0], [1], [2], ...)

print("The {0} jumped over the {1}".format(animal, item))

# Can be written more efficiently using keyword arguments instead of declaring the variables outside of the print() statement

print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))

# Alternative the string can be saved as a variable and the .format() method can be directly applied to the variable

text = "The {} jumped over the {}"

print(text.format(animal, item))

# To print out a number to a desired significant figure, this function will also round the number. 

number = 1000

print("The number is {:.2f}".format(number))

# Alternative inputs include: comma separateion, binary representation, octal and hexadecimal numbers, and scientific representation

print("The large number is {:,}".format(number))

print("The number in binary is {:b}".format(number))
      
print("The number in octal repsentation is {:o}".format(number))

print("The number in hexadecimal repsentation is {:X}".format(number))

print("The number in scientific repsentation is {:E}".format(number))

