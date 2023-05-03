# map() = applies a function to each item in an iterable (list, tuple, etc.)

# map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

# We will convert of all of the prices of these items from Dollars to Euros
# First we create a function that will leave the first index (clothes items) and multiple the price by the conversion rate

convert_to_euros = lambda data: (data[0], data[1]*0.82)

# We map the function to the list but we also want to produce another list so we wrapped the map function in a list

store_euros = list(map(convert_to_euros, store))

for i in store_euros:
    print(i)