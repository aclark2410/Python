# Exception = events detected during execution thatinterupt the flow of a program

# Example

#numerator = int(input("Enter a number to divide: "))

#denominator = int(input("Enter a number to divide by: "))

#result = numerator/denominator

#print(result)

# If numerator = 5 and denominator = 0, it will cause as error: ZeroDivisionError: division by zero

# If we suspect that the inputs of a block of code could cause an exception we can create a condition to handle it

try: 
    numerator = int(input("Enter a number to divide: "))

    denominator = int(input("Enter a number to divide by: "))

    result = numerator/denominator

# This except condition will handle zero division errors

except ZeroDivisionError as e:
    print("You cannot divide by zero")

# This except condition will handle incorrect value entry (i.e entering a letter instead of a number)

except ValueError as e:
    print("Enter only a numerical value")

# This except condition will catch any other non-specific errors 

except Exception as e:
    print("Something went wrong")

# If there are no errors an else statement can be included at the end

else:
    print(result)

# The code within the finally cause will always execute regardless of the error handling

finally: 
    print("This will always execute at the end")