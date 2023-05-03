# Keyword arguments = arguments preceded by an identifier when we pass them to a function,
#                     the order of the arguments doesn't matter, unlike positional arguments,
#                     Python knows the names of the arguments that our function receives.


def hello(first_name, middle_name, last_name):
    print("Hello " + first_name + " " + middle_name + " " + last_name)

hello(first_name="Andrew", middle_name="Kenneth", last_name="Clark")