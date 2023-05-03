# Lambda Function = function written in 1 line using lambda keyboard
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)

# Here is an example of a simple function

def double(x):
    return x*2

print(double(5))

# We can re-write this using a lambda function

double_functon = lambda x: x*2

print(double_functon(5))

# Here is another example with two parameters

multiply_function = lambda x, y: x*y

print(multiply_function(4, 2))

# Here is a more complex example with three parameters

three_multiply = lambda x, y , z: 2*x + 3*y -4*z

print(three_multiply(3,5,2))

# We can also pass in boolean statements

age_check = lambda age: True if age > 18 else False

print(age_check(17))