import random

# Generate a random integer between two given numbers

x = random.randint(1,6)

print(x)

# Generate a random number between 0 and 1

y = random.random()

print(y)

# Choose a random choice from a given a non-empty sequence i.e list, set

myList = ["Rock", "Paper", "Scissors"]

z = random.choice(myList)

print(z)

# Shuffle a non-empty sequence

random.shuffle(myList)

print(myList)