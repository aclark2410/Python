# Scope = The region that a variable is recognised.
#         A variable is only available from inside the region it is created.
#         Global and locally scoped versions of a variable can be created.

name = "Andrew"         # this will be used inside of the function if the variable name is not defined inside of the function.

def display_name():
    name = "Clark"      # local scope (available only inside of this function)
    print(name)


print(name)             # this would only print out the global version of the name which is outside of the function
display_name()