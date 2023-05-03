# reduce() = apply a function to an iterable and reduce it to a single cumulative value
#            performs function on first two elements and repeats process until 1 value remains.

# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]

# We want to reduce this list so that only 1 cumulative value remains (i.e "HELLO")

# Since reduce() performs the function on the first two elements and repeats the process we only need two variables in our function

combine_function = lambda x, y: x + y   # You can use any expression here (i.e x*y, x/y etc.) as long as it is in the correct context because here we can only add strings together

word = functools.reduce(combine_function, letters)

print(word)

# Here is a different example using numbers, we want to find the factorial of 5 therefore we must multiple all of the numbers in the list together

factorial = [5,4,3,2,1]

# This will multiply 5 x 4 = 20, then it will multiply 20 x 3 = 60, then 60 x 2 = 120, and finally 120 x 1 = 120

multiple_function = lambda x, y: x*y

result = functools.reduce(multiple_function, factorial)

print(result)