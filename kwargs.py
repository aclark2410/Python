# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of 
#            keyword arguments


#Example of function with fixed keyword arguments

def hello(first_name, last_name):
    print("Hello " + first_name + " " + last_name)

hello("Andew", "Clark")


# Example of function with varying number of keyword arguments (***kwargs)

def hi(**kwargs):
    #print("Hello " + kwargs["first_name"] + " " + kwargs["middle_name"])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")


hi(first_name="Andrew", middle_name="Kennenth", last_name="Clark")