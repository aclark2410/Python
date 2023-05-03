# list = used to store multiple lists within a single variable

food = ["pizza", "hamburgers", "hotdog", "spaghetti"]

print(food)


# Changing items in list can be done by assigning new variable to the index of the list

food[0] = "sushi"

print(food[0])


# Loop through the list and print all items in the list

for i in food:
    print(i)


# If we want to add an item to the end of the list we can use append

food.append("ice cream")

print(food)


# If we want to remove a particular item in the list we can use remove

food.remove("hotdog")

print(food)


# If we want to remove the last element we can use pop

food.pop()

print(food)


# If we want to insert an item at a particular index we can use insert

food.insert(0, "cake")

print(food)


# If we want to sort a list either alphabetically or numerically we can use sort

food.sort()

print(food)


# If we want to clear all of the items in a list we can use clear

food.clear()

print(food)