# Nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function


# This is a long winded way of doing these operations

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

# We can write a nested function 

print(round(abs(float(input("Enter a whole positive number: ")))))


