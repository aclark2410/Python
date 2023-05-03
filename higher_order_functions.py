# Higher Order Functions = a function that either:
#                          1) accepts a function as an argument
#                          2) returns a function
#                          This works because in Python functions are treated as objects

# Example of 1)
# The loud() and quiet() functions can be used as arguments in the hello() function. The return statement of the 

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)

hello(loud)

hello(quiet)


# Example of 2)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)

print(divide(10))

