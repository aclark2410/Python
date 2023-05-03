# *args = parameter that will pack all arguments into a tuple.
#         Useful so that a function can accept a varying amount of arguments.

def add(num1, num2):
    sum = num1 + num2
    return sum

print(add(1,2))

# The arguments in the function can be replaced with *args

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9))