def hello():
    print("Hello")

# We can assign the function to a variable and it can be used as an alternative object

hi = hello()

hi

# Alternatively we can remove the brackets around the hello function and assign them to the variable and create another function that will inherit
# the properties of the original function

hi = hello

hi()

# This works because both the original object and the new object have the same memory address