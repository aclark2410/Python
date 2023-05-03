# Nested loops = The 'inner loop' will finish all of it's iterations before
#                finishing one iteration of the 'outer loop'

rows = int(input("How many rows?: "))

columns = int(input("How many columns?: "))

symbol = input("Enter a symbol to use: ")


# Outer for loop
for i in range(rows):
    # Inner for loop
    for j in range(columns):
        print(symbol, end="")
    print()
