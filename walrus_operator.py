# Walrus Operator :=

# Assigns values to variables a part of a larger expression

happy = True

print(happy)

# This can be combined into one statement

print(happy := True)

# The following example can be written in a more efficient way

foods = list()

while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)


# We can write the same program using less lines of code with the Walrus Operator

food = list()

while food := input("What food do you like?: ") != "quit":
    foods.append(food)
